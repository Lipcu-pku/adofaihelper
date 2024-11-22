"""
A module to help with reading and processing `.adofai` files (in the rhythm game 'A Dance Of Fire And Ice'). 

---

Examples: 

`AskForPath()` to draw a window to select the `.adofai` file
`SaveAsPath()` to draw a window to select the `.adofai` file path to save
`ADOFAI.load(path)` to load the .adofai data as ADOFAI
`ADOFAI.loads(adofai_str)` to load the .adofai string as ADOFAI
"""

import json, os
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import ctypes
from typing import List

from .enums import *
from .settings import *
from .action import *
from .decoration import *

__all__ = [
    'AskForPath', 'SaveAsPath', 'ADOFAI'
]

__version__ = "1.1.7"

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
        if not isinstance(value, dict):
            raise ADOFAIDecodeError('The file is not a dict form')
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

def AskForPath(filetypes=[("ADOFAI files", ("*.adofai", "*.ADOFAI"))]) -> str:
    """
    Select .adofai file

    :return: .adofai file path
    """
    root = Tk()
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
    root.tk.call('tk', 'scaling', ScaleFactor/75)
    root.withdraw()
    return askopenfilename(filetypes=filetypes)

def SaveAsPath(default_name: str | None = None) -> str:
    """
    Select .adofai file saving path

    :param default_name: Default file name
    :return: .adofai file path
    """
    root = Tk()
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
    root.tk.call('tk', 'scaling', ScaleFactor/75)
    root.withdraw()
    return asksaveasfilename(filetypes=[("ADOFAI files", "*.adofai"), ("ADOFAI files", "*.ADOFAI")], initialfile=default_name)

def path_split(FILE_PATH: str) -> tuple:
    """
    Split the sbsolute path into Tuple[DirName, LevelName, Extenstion]

    :param FILE_PATH: the absolute path of the .adofai file. 
    
    :return: Tuple[Level_Dir, Level_Name, Extension]
    """
    level_dir, level = os.path.split(FILE_PATH)
    level_name, extension = os.path.splitext(level)
    return level_dir, level_name, extension

def pathData_to_angleData(pathData: str) -> list:
    """
    To translate the `pathData` in the older version to the `angleData` in the newer version. 

    :param pathData: the `pathData` of the level. 
    
    :return: converted `angleData`. 
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

class ADOFAI:
    def __init__(self, adofai_dict: dict | None = None):
        if adofai_dict is None:
            adofai_dict = {}
        self.angleData : List[int | float] = adofai_dict.get("angleData", pathData_to_angleData(adofai_dict.get("pathData", "")))
        self.settings : SETTINGS = SETTINGS(**adofai_dict.get('settings', {}))
        
        actions = []
        decorations = []
        for action in adofai_dict.get("actions", []):
            if isinstance(a := ACTION.load(**action), Decoration):
                decorations.append(a)
            else:
                actions.append(a)
        self.actions : List[Action] = actions
        self.decorations : List[Decoration] = decorations + [DECORATION.load(**decoration) for decoration in adofai_dict.get("decorations", [])]

    @property
    def value(self) -> dict:
        return {
            "angleData": self.angleData,
            "settings": self.settings.value,
            "actions": [action.value for action in self.actions], 
            "decorations": [decoration.value for decoration in self.decorations]
        }

    def __repr__(self) -> str:
        return f'ADOFAI({self.value})'

    def add_action(self, floor: int | None = None, eventType : str | eventTypes | None = None, **kwargs):
        action = ACTION.load(floor, eventType, **kwargs)
        self.actions.append(action)
    
    def add_decoration(self, eventType : str | eventTypes | None = None, **kwargs):
        decoration = DECORATION.load(eventType, **kwargs)
        self.decorations.append(decoration)
    
    def add_action_from_dict(self, action_dict: dict):
        self.add_action(**action_dict)
    
    def add_decoration_from_dict(self, decoration_dict: dict):
        self.add_decoration(**decoration_dict)

    @property
    def as_adofai(self) -> str:
        """
        export string in `.adofai` form

        :return: string form of `.adofai`
        """
        angleData = self.angleData
        settings = self.settings.value
        actions = [action.value for action in sorted(self.actions, key=lambda action: action.floor)]
        decorations = [decoration.value for decoration in self.decorations]
        output = f'''{{\n\t\"angleData\": {angleData},\n'''

        output += '\t\"settings\": \n\t{\n'
        for key, value in settings.items():
            space = ' ' if key in ['version', 'legacyFlash', 'legacyCamRelativeTo', 'legacySpriteTiles', 'legacyTween'] else ''
            output += f'\t\t\"{key}\": {json.dumps(value, ensure_ascii=False)}{space},\n'
        output = output.rstrip(',\n') + '\n'
        output += '\t},\n'
        
        output += '\t\"actions\": \n\t[\n'
        for action in actions:
            # extracomma = '' if action["eventType"] in ['SetSpeed', 'Twirl', 'SetText', 'SetHitsound', 'PlaySound', 'Hide', 'Pause', 'Hold'] else ','
            line = '{ ' + json.dumps(action, ensure_ascii=False).lstrip('{').rstrip('}') + ' }'
            output += f'\t\t{line},\n'
        output = output.rstrip(',\n') + '\n'
        output += '\t],\n'

        output += '\t\"decorations\": \n\t[\n'
        for decoration in decorations:
            line = '{ ' + json.dumps(decoration, ensure_ascii=False).lstrip('{').rstrip('}') + '  }'
            output += f'\t\t{line},\n'
        output = output.rstrip(',\n') + '\n'
        output += '\t]\n}'

        return output

    def dump(self, FILE_PATH: str, file_replace_warning: bool = True):
        """
        print level in `.adofai` form

        :param FILE_PATH: path to print
        :param file_replace_warning: file replace warning 
        """
        output = self.as_adofai

        if file_replace_warning:
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
    
    @classmethod
    def loads(cls, adofai_string: str):
        """
        load adofai_string as ADOFAI

        :param adofai_string: string data of adofai

        :return: ADOFAI data
        """
        try:
            return cls(ADOFAIParser(adofai_string).parse())
        except ADOFAIDecodeError as e:
            print(f"Error decoding ADOFAI: {e}")
    
    @classmethod
    def load(cls, FILE_PATH: str):
        """
        load file as ADOFAI

        :param FILE_PATH: adofai file path

        :return: ADOFAI data
        """
        try:
            return cls(ADOFAIParser(open(FILE_PATH, 'r', encoding='utf-8-sig').read()).parse())
        except ADOFAIDecodeError as e:
            print(f"Error decoding ADOFAI: {e}")
    
    @property
    def angles(self) -> List[int | float]:
        """返回每一个砖块的旋转角度（考虑了旋转、中旋和三球）"""
