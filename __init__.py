"""
A module to help with reading and processing `.adofai` files (in the rhythm game 'A Dance Of Fire And Ice'). 

---

Examples: 

Use `adofai(path)` to directly read the level at `path` and convert to a `ADOFAI` class. 

There are several parameters in the `ADOFAI` class: `pathData`, `angleData`, `settings`, `settings_dict`, `actions`, `decorations`.

As for the difference between `settings` and `settings_dict`, the former one have further parameters like `version`, `artist` and so on. The Latter one is just the `dict` of settings. 

For lines in `actions` you can also use `action = ACTION(_action)` to get its further parameters, so does the `decorations`. 

You can just use `AskForPath()` to show a window of opening the level, and `SaveAsPath()` to show a window of saving the level. 

You can use `SortActions()` to sort the actions in the order of the floor, as you can see in the default `.adofai` file. 

You can use `ADOFAIprint()` to directly output the level in the `.adofai` format, except for the random extra commas in the actions.
"""

import json, os, re
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import ctypes
# from constants import *

# Prohibit calls to the following funcs

__all__ = [
    'ADOFAI_read', 'pathData_to_angleData', 'AskForPath', 'adofai', 'ADOFAI_print', 'SortActions',
    'ADOFAI', 'ADOFAIDecodeError'
]

true = True
false = False
null = None

class ADOFAIDecodeError(Exception):
    """Exception raised for errors in the ADOFAI decoding process."""
    def __init__(self, message):
        super().__init__(message)

class ADOFAIParser:
    def __init__(self, adofai_string : str):
        self.adofai_string : str = adofai_string
        self.index : int = 0

    def parse(self):
        self._skip_whitespace()
        value = self._parse_value()
        self._skip_whitespace()
        if self.index != len(self.adofai_string):
            raise ADOFAIDecodeError("Extra data")
        return value

    def _skip_whitespace(self):
        while self.index < len(self.adofai_string) and self.adofai_string[self.index].isspace():
            self.index += 1

    def _parse_value(self):
        if self.index >= len(self.adofai_string):
            raise ADOFAIDecodeError("Unexpected end of input")
        char = self.adofai_string[self.index]
        if char == '"':
            return self._parse_string()
        elif char == '{':
            return self._parse_object()
        elif char == '[':
            return self._parse_array()
        elif char in '-0123456789' or self.adofai_string[self.index:self.index+8] == "Infinity":
            return self._parse_number()
        elif self.adofai_string[self.index:self.index+4] == "true":
            self.index += 4
            return True
        elif self.adofai_string[self.index:self.index+5] == "false":
            self.index += 5
            return False
        elif self.adofai_string[self.index:self.index+4] == "null":
            self.index += 4
            return None
        else:
            raise ADOFAIDecodeError(f"Unexpected character: {char}")

    def _parse_string(self):
        self.index += 1  # Skip the opening quote
        start_index = self.index
        while self.index < len(self.adofai_string):
            char = self.adofai_string[self.index]
            if char == '"':
                if self.index > start_index and self.adofai_string[self.index - 1] == '\\':
                    # Skip escaped quote
                    self.index += 1
                    continue
                value = self.adofai_string[start_index:self.index]
                self.index += 1  # Skip the closing quote
                return value.replace('\n', '')
            elif char == '\\':
                self.index += 2  # Skip escaped character
            else:
                self.index += 1
        raise ADOFAIDecodeError("Unterminated string")

    def _parse_number(self):
        if self.adofai_string[self.index:self.index+8] == "Infinity":
            self.index += 8
            return float('inf')
        elif self.adofai_string[self.index:self.index+9] == "-Infinity":
            self.index += 9
            return float('-inf')
        
        start_index = self.index
        if self.adofai_string[self.index] == '-':
            self.index += 1
        while self.index < len(self.adofai_string) and self.adofai_string[self.index].isdigit():
            self.index += 1
        if self.index < len(self.adofai_string) and self.adofai_string[self.index] == '.':
            self.index += 1
            if not self.adofai_string[self.index].isdigit():
                raise ADOFAIDecodeError("Invalid number")
            while self.index < len(self.adofai_string) and self.adofai_string[self.index].isdigit():
                self.index += 1
        if self.index < len(self.adofai_string) and self.adofai_string[self.index] in 'eE':
            self.index += 1
            if self.adofai_string[self.index] in '+-':
                self.index += 1
            if not self.adofai_string[self.index].isdigit():
                raise ADOFAIDecodeError("Invalid number")
            while self.index < len(self.adofai_string) and self.adofai_string[self.index].isdigit():
                self.index += 1
        number_str = self.adofai_string[start_index:self.index]
        return int(number_str) if '.' not in number_str and 'e' not in number_str and 'E' not in number_str else float(number_str)

    def _parse_array(self):
        self.index += 1  # Skip the opening bracket
        array = []
        self._skip_whitespace()
        while self.index < len(self.adofai_string) and self.adofai_string[self.index] != ']':
            self._skip_whitespace()
            array.append(self._parse_value())
            self._skip_whitespace()
            if self.index < len(self.adofai_string) and self.adofai_string[self.index] == ',':
                self.index += 1
                self._skip_whitespace()
        self.index += 1  # Skip the closing bracket
        return array

    def _parse_object(self):
        self.index += 1  # Skip the opening brace
        obj = {}
        self._skip_whitespace()
        while self.index < len(self.adofai_string) and self.adofai_string[self.index] != '}':
            self._skip_whitespace()
            if self.adofai_string[self.index] == '"':
                key = self._parse_string()
                self._skip_whitespace()
                if self.adofai_string[self.index] != ':':
                    raise ADOFAIDecodeError("Expected ':'")
                self.index += 1  # Skip the colon
                self._skip_whitespace()
                obj[key] = self._parse_value()
                self._skip_whitespace()
                if self.index < len(self.adofai_string) and self.adofai_string[self.index] == ',':
                    self.index += 1
                    self._skip_whitespace()
        self.index += 1  # Skip the closing brace
        return obj

def AskForPath() -> str:
    """
    Select .adofai file

    Returns:
        .adofai file path
    """
    root = Tk()
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
    root.tk.call('tk', 'scaling', ScaleFactor/75)
    root.withdraw()
    return askopenfilename(filetypes=[("ADOFAI files", "*.adofai"), ("ADOFAI files", "*.ADOFAI")])

def SaveAsPath(default_name: str|None = None) -> str:
    """
    Select .adofai file saving path

    Returns:
        .adofai file path
    """
    root = Tk()
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
    root.tk.call('tk', 'scaling', ScaleFactor/75)
    root.withdraw()
    return asksaveasfilename(filetypes=[("ADOFAI files", "*.adofai"), ("ADOFAI files", "*.ADOFAI")], title=default_name)

def path_split(FILE_PATH: str) -> tuple:
    """
    Split the sbsolute path into Tuple[<DirName>, <LevelName>, <Extenstion>]

    Parameters:
        FILE_PATH: the absolute path of the .adofai file. 
    
    Returns:
        Tuple[Level_Dir, Level_Name, Extension]
    """
    level_dir, level = os.path.split(FILE_PATH)
    level_name, extension = os.path.splitext(level)
    return level_dir, level_name, extension

def ADOFAI_read(FILE_PATH: str) -> dict|None:
    """
    To read the .adofai file and convert to a <dict>. 

    Parameters:
        FILE_PATH: The absolute path of the `.adofai` file

    Returns:
        a `<dict>` of the content, or `None` due to certain Error.
    """
    try:
        return ADOFAIParser(open(FILE_PATH, 'r', encoding='utf-8-sig').read()).parse()
    except ADOFAIDecodeError as e:
        print(f"Error decoding ADOFAI: {e}")

def pathData_to_angleData(pathData: str) -> list:
    """
    To translate the `pathData` in the older version to the `angleData` in the newer version. 

    Parameters:
        pathData: the `pathData` of the level. 
    
    Returns:
        converted `angleData`. 
    """
    pathDatatrans={'R':0, 'p':15, 'J':30, 'E':45, 'T':60, 'o':75, 'U':90, 'q':105, 'G':120, 'Q':135, 'H':150, 'W':165, 'L': 180, 'x':195, 'N':210, 'Z':225, 'F':240, 'V':255, 'D':270, 'Y':285, 'B':300, 'C':315, 'M':330, 'A':345, '5':555, '6':666, '7':777, '8':888, '!':999}
    angleData=[pathDatatrans[i] for i in pathData]
    for i,angle in enumerate(angleData):
        lastangle=angleData[i-1] if i>=1 else 0
        if angle==555: angleData[i]=(lastangle+72)%360
        if angle==666: angleData[i]=(lastangle-72)%360
        if angle==777: angleData[i]=(lastangle+360/7)%360
        if angle==888: angleData[i]=(lastangle-360/7)%360
    return angleData

def clearFormat(content: str) -> str:
    """
    To clear the format of some `<str>` content. 

    e.g. <size=50> Size </size> -> Size 
    
    Parameters:
        content: `<str>` content to clear format. 
    
    Returns:
        converted '<str>'
    """
    cleared = ''
    inside_tag = False

    for char in content:
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
            continue  # 跳过 '>'
        
        if not inside_tag:
            cleared += char

    return cleared

def boolean(value: any) -> bool:
    """
    To convert the `"Enabled"|"Disabled"` `<bool>` type in the older version to `True|False` in the newer version. 

    Parameters:
        value: `"Enabled"|"Disabled"` in the older version, or `True|False` in the newer version.
    
    Returns:
        boolean type `True|False`.
    """
    if type(value) == bool:
        return value
    else:
        return True if value == 'Enabled' else False

class ADOFAI:
    def __init__(self, adofai_data):
        self.angleData = adofai_data.get("angleData", pathData_to_angleData(adofai_data.get("pathData", "")))
        self.settings = self.DynamicObject(adofai_data.get("settings", {}))
        self.actions = [self.DynamicObject(action) for action in adofai_data.get("actions", [])]
        self.decorations = [self.DynamicObject(decoration) for decoration in adofai_data.get("decorations", [])]

    class DynamicObject:
        def __init__(self, data):
            if isinstance(data, dict):
                self.__dict__["_data"] = data
            else:
                raise ValueError("DynamicObject must be initialized with a dictionary")

        def __getattr__(self, name):
            if name in self._data:
                value = self._data[name]
                if isinstance(value, dict):
                    return ADOFAI.DynamicObject(value)
                elif isinstance(value, list):
                    return [ADOFAI.DynamicObject(item) if isinstance(item, dict) else item for item in value]
                else:
                    return value
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

        def __setattr__(self, name, value):
            if name == "_data":
                super().__setattr__(name, value)
            else:
                self._data[name] = value

        def __getitem__(self, key):
            return self._data[key]

        def __setitem__(self, key, value):
            self._data[key] = value

        def get(self, key, default=None):
            return self._data.get(key, default)
        
        def keys(self):
            return self._data.keys()

        def __repr__(self):
            return repr(self._data)
def SortActions(actions: list)->list:
    """
    To sort the `<list>` actions in the order of the floor, as in the default .adofai file

    ---
    Parameters:
        `actions`: the actions `<list>` to be sorted
    
    ---
    Returns:
        the sorted actions `<list>`
    
    
    """
    actions.sort(key = lambda x: x['floor'])
    return actions

def ADOFAI_print(level: ADOFAI, FILE_PATH: str, info: bool = True) -> None:
    """
    print level in `.adofai` form

    Parameters:
        level: `<ADOFAI>`, level to print
        FILE_PATH: path to print
        info: some warnings and infomation. 
    """
    angleData = level.angleData
    settings = level.settings
    actions = level.actions
    decorations = level.decorations
    output = f'''{{\n\t\"angleData\": {angleData},\n'''

    output += '\t\"settings\": \n\t{\n'
    for setting in list(settings.keys()):
        space = ' ' if setting in ['version', 'legacyFlash', 'legacyCamRelativeTo', 'legacySpriteTiles', 'legacyTween'] else ''
        output += f'\t\t\"{setting}\": {json.dumps(settings[setting])}{space},\n'
    output = output.rstrip(',\n') + '\n'
    output += '\t},\n'
    
    output += '\t\"actions\": \n\t[\n'
    for action in actions:
        # extracomma = '' if action["eventType"] in ['SetSpeed', 'Twirl', 'SetText', 'SetHitsound', 'PlaySound', 'Hide', 'Pause', 'Hold'] else ','
        line = '{ ' + json.dumps(action._data).lstrip('{').rstrip('}') + ' }'
        output += f'\t\t{line},\n'
    output = output.rstrip(',\n') + '\n'
    output += '\t],\n'

    output += '\t\"decorations\": \n\t[\n'
    for decoration in decorations:
        line = '{ ' + json.dumps(decoration._data).lstrip('{').rstrip('}') + '  }'
        output += f'\t\t{line},\n'
    output = output.rstrip(',\n') + '\n'
    output += '\t]\n}'

    if info:
        if os.path.exists(FILE_PATH):
            if input(f'{FILE_PATH} already exists. Do you want to overwrite it? Yes / [No] ') == 'Yes':
                print(output, file=open(FILE_PATH, 'w', encoding='utf-8-sig'))
                print(f'Exported to {FILE_PATH}. ')
            else:
                print('Canceled. ')
                return
        else:
            print(output, file=open(FILE_PATH, 'w', encoding='utf-8-sig'))
    else:
        print(output, file=open(FILE_PATH, 'w', encoding='utf-8-sig'))

def adofai(FILE_PATH: str) -> ADOFAI|None:
    """
    Read the .adofai file at `FILE_PATH` and return a `<ADOFAI>`. 

    ---
    Parameters:
        `FILE_PATH`: the absolute path of `.adofai` file
    
    ---
    Returns:
        Converted `<ADOFAI>`, or `None` due to certain Error
    """
    return ADOFAI(ADOFAI_read(FILE_PATH))

def ADOFAI_TO_DICT(level: ADOFAI) -> dict:
    angleData = level.angleData
    settings = level.settings
    actions = level.actions
    decorations = level.decorations
    return {
        "angleData": angleData,
        "settings": settings,
        "actions": actions,
        "decorations": decorations
    }
