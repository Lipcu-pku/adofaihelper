"""
A module to help with reading and processing `.adofai` files (in the rhythm game 'A Dance Of Fire And Ice'). 

---

Examples: 

Use `adofai(path)` to directly read the level at `path` and convert to a `ADOFAI` class. 

There are several parameters in the `ADOFAI` class: `pathData`, `angleData`, `settings`, `settings_dict`, `actions`, `decorations`.

As for the difference between `settings` and `settings_dict`, the former one have further parameters like `version`, `artist` and so on. The Latter one is just the `dict` of settings. 

For lines in `actions` you can also use `action = ACTION(_action)` to get its further parameters, so does the `decorations`. 

You can just use `AskForPath()` to show a window of opening the level. 

You can use `SortActions()` to sort the actions in the order of the floor, as you can see in the default `.adofai` file. 

You can use `ADOFAIprint()` to directly output the level in the `.adofai` format, except for the random extra commas in the actions.
"""

import json, os, sys
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from adofaihelper.constants import *

# Prohibit calls to the following funcs
sys.modules["builtins"].__dict__['clearFormat'] = None
sys.modules["builtins"].__dict__['boolean'] = None

__all__ = [
    'ADOFAI_read', 'pathData_to_angleData', 'AskForPath', 'adofai', 'ADOFAI_print', 'SortActions',
    'SETTINGS', 'ACTION', 'DECORATION', 'ADOFAI'
]

true = True
false = False
null = None

class ADOFAIParser:
    # This part is writen by GPT-4o

    def __init__(self, adofai_string):
        self.adofai_string = adofai_string
        self.index = 0

    def parse(self):
        self._skip_whitespace()
        value = self._parse_value()
        self._skip_whitespace()
        if self.index != len(self.adofai_string):
            raise ValueError("Extra data")
        return value

    def _skip_whitespace(self):
        while self.index < len(self.adofai_string) and self.adofai_string[self.index].isspace():
            self.index += 1

    def _parse_value(self):
        if self.index >= len(self.adofai_string):
            raise ValueError("Unexpected end of input")
        char = self.adofai_string[self.index]
        if char == '"':
            return self._parse_string()
        elif char == '{':
            return self._parse_object()
        elif char == '[':
            return self._parse_array()
        elif char in '-0123456789':
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
            raise ValueError(f"Unexpected character: {char}")

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
        raise ValueError("Unterminated string")

    def _parse_number(self):
        start_index = self.index
        if self.adofai_string[self.index] == '-':
            self.index += 1
        while self.index < len(self.adofai_string) and self.adofai_string[self.index].isdigit():
            self.index += 1
        if self.index < len(self.adofai_string) and self.adofai_string[self.index] == '.':
            self.index += 1
            if not self.adofai_string[self.index].isdigit():
                raise ValueError("Invalid number")
            while self.index < len(self.adofai_string) and self.adofai_string[self.index].isdigit():
                self.index += 1
        if self.index < len(self.adofai_string) and self.adofai_string[self.index] in 'eE':
            self.index += 1
            if self.adofai_string[self.index] in '+-':
                self.index += 1
            if not self.adofai_string[self.index].isdigit():
                raise ValueError("Invalid number")
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
                    raise ValueError("Expected ':'")
                self.index += 1  # Skip the colon
                self._skip_whitespace()
                obj[key] = self._parse_value()
                self._skip_whitespace()
                if self.index < len(self.adofai_string) and self.adofai_string[self.index] == ',':
                    self.index += 1
                    self._skip_whitespace()
        self.index += 1  # Skip the closing brace
        return obj

# def AskForPath(icon_path: str = default_icon_path) -> str:
def AskForPath() -> str:
    """
    Select .adofai file

    ---
    Parameters:
        `icon_path`: the path of icon to be presented.
    ---
    returns:
        .adofai file path
    """
    root = Tk()
    root.withdraw()
    return askopenfilename(filetypes=[("ADOFAI files", "*.adofai"), ("ADOFAI files", "*.ADOFAI")])

def SaveAsPath() -> str:
    """
    Select .adofai file saving path
    """
    root = Tk()
    root.withdraw()
    return asksaveasfilename(filetypes=[("ADOFAI files", "*.adofai"), ("ADOFAI files", "*.ADOFAI")])

def path_split(FILE_PATH: str) -> tuple:
    """
    Split the sbsolute path into Tuple[<DirName>, <LevelName>, <Extenstion>]

    ---
    Parameters:
        `FILE_PATH`: the absolute path of the .adofai file. 
    
    ---
    Returns:
        Tuple(Level_Dir, Level_Name, Extension)
    """
    level_dir, level = os.path.split(FILE_PATH)
    level_name, extension = os.path.splitext(level)
    return level_dir, level_name

def ADOFAI_read(FILE_PATH: str) -> dict|None:
    """
    To read the `.adofai` file and convert to a `<dict>`. 

    ---
    Parameters:
        `FILE_PATH`: The absolute path of the `.adofai` file
    ---
    Returns:
        a `<dict>` of the content, or `None` due to certain Error.
    """
    return ADOFAIParser(open(FILE_PATH, 'r', encoding='utf-8-sig').read()).parse()

def pathData_to_angleData(pathData: str) -> list:
    """
    To translate the `pathData` in the older version to the `angleData` in the newer version. 

    ---
    Parameters:
        `pathData`: the `pathData` of the level. 
    
    ---
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

    ---
    e.g. <size=50> Size </size> -> Size 
    
    ---
    Parameters:
        `content`: `<str>` content to clear format. 
    
    ---
    Returns:
        converted '<str>'
    """
    cleared = ''
    to_pass, to_add = False, True
    for b in content:
        if b == '<':
            to_pass, to_add = True, False
        if b == '>':
            to_pass, to_add = True, True
        if to_add:
            if to_pass:
                to_pass = False
                continue
            cleared += b
    return cleared

def boolean(value: any) -> bool:
    """
    To convert the `"Enabled"|"Disabled"` `<bool>` type in the older version to `True|False` in the newer version. 

    ---
    Parameters:
        `value`: `"Enabled"|"Disabled"` in the older version, or `True|False` in the newer version.
    
    ---
    Returns:
        boolean type `True|False`.

    """
    if type(value) == bool:
        return value
    else:
        return True if value == 'Enabled' else False

class SETTINGS:
    def __init__(self, settings: dict):
        self.version: int = settings['version']
        self.artist: str = clearFormat(settings['artist'])
        self.specialArtistType: str = settings.get('specialArtistType', "None")
        self.artistPermission: str = settings.get('artistPermission', "")
        self.artistLinks: str = settings.get('artistLinks', "")

        self.song: str = clearFormat(settings['song'])
        self.songFilename: str = settings['songFilename']
        self.author: str = clearFormat(settings['author'])

        self.previewImage: str = settings.get('previewImage', "")
        self.previewIcon: str = settings.get('previewIcon', "")
        self.previewIconColor: str = settings.get('previewIconColor', "")
        self.previewSongStart: str = settings.get('previewSongStart', "")
        self.previewSongDuration: str = settings.get('previewSongDuration', "")

        self.seizureWarning: bool = boolean(settings.get('seizureWarning', False))

        self.levelDesc: str = settings.get('levelDesc', "")
        self.levelTags: str = settings.get('levelTags', "")
        
        self.speedTrialAim: float = settings.get('speedTrialAim', 1.0)
        self.difficulty: str = settings.get('difficulty', "")
        self.requiredMods: list = settings.get('requiredMods', [])

        self.bpm: float = settings['bpm']
        self.volume: int = settings['volume']
        self.offset: int = settings['offset']
        self.pitch: int = settings['pitch']
        self.hitsound: str = settings['hitsound']
        self.hitsoundVolume: int = settings['hitsoundVolume']
        self.countdownTicks: int = settings.get('countdownTicks', 4)
        self.separateCountdownTime: bool = boolean(settings['separateCountdownTime'])

        self.trackColorType: str = settings['trackColorType']
        self.trackColor: str = settings['trackColor']
        self.secondaryTrackColor: str = settings['secondaryTrackColor']
        self.trackColorAnimDuration: float = settings.get('trackColorAnimDuration', 2)
        self.trackColorPulse: str = settings.get('trackColorPulse', "None")
        self.trackPulseLength: int = settings.get('trackPulseLength', 10)
        self.trackStyle: str = settings['trackStyle']
        self.trackTexture: str = settings.get('trackTexture', '')
        self.trackTextureScale: float = settings.get('trackTextureScale', 1)
        self.trackGlowIntensity: int = settings.get('trackGlowIntensity', 100)
        self.trackAnimation: str = settings['trackAnimation']
        self.beatsAhead: float = settings.get('beatsAhead', 4)
        self.trackDisappearAnimation: str = settings['trackDisappearAnimation']      
        self.beatsBehind: float = settings.get('beatsBehind', 4)

        self.backgroundColor: str = settings['backgroundColor']
        self.showDefaultBGIfNoImage: bool = boolean(settings.get('showDefaultBGIfNoImage', True))
        self.showDefaultBGTile: bool = settings.get('showDefaultBGTile', False)
        self.defaultBGTileColor: str = settings.get('defaultBGTileColor', '101121')
        self.defaultBGShapeType: str = settings.get('defaultBGShapeType', 'Disabled')
        self.defaultBGShapeColor: str = settings.get('defaultBGShapeColor', 'ffffff')
        self.bgImage: str = settings['bgImage']
        self.bgImageColor: str = settings['bgImageColor']
        self.parallax: int = settings.get('parallax', 100)
        self.bgDisplayMode: str = settings.get('bgDisplayMode', 'FitToScreen')
        self.imageSmoothing: bool = boolean(settings.get('imageSmoothing', True))
        self.lockRot: bool = boolean(settings.get('lockRot', False))
        self.loopBG: str = boolean(settings.get('loopBG', False))
        self.scalingRatio: int = settings.get('scalingRatio', settings.get('unscaledSize', 100))
        self.relativeTo: str = settings.get('relativeTo', "Player")
        self.position: list[float] = settings.get('position', [0, 0])
        self.rotation: float = settings.get('rotation', 0)
        self.zoom: float = settings.get('zoom', 100)

        self.bgVideo: str = settings.get('bgVideo', '')
        self.loopVideo: bool = boolean(settings.get('loopVideo', False))
        self.vidOffset: int = settings.get('vidOffset', 0)
        
        self.pulseOnFloor: bool = settings.get('pulseOnFloor', True)
        self.floorIconOutlines: bool = boolean(settings.get('floorIconOutlines', False))
        self.stickToFloors: bool = boolean(settings.get('stickToFloors', True))

        self.planetEase: str = settings.get('planetEase', 'Linear')
        self.planetEaseParts: int = settings.get('planetEaseParts', 1)
        self.planetEasePartBehavior: str = settings.get('planetEasePartBehavior', 'Mirror')

        self.defaultTextColor: str = settings.get('defaultTextColor', 'ffffff')
        self.defaultTextShadowColor: str = settings.get('defaultTextShadowColor', '00000050')
        self.congratsText: str = settings.get('congratsText', '')
        self.perfectText: str = settings.get('perfectText', '')

        self.legacyFlash: bool = boolean(settings.get('legacyFlash', False))
        self.legacyCamRelativeTo: bool = boolean(settings.get('legacyCamRelativeTo', False))
        self.legacySpriteTiles: bool = boolean(settings.get('legacySpriteTiles', False))
        self.legacyTween: bool = boolean(settings.get('legacyTween', True))

class ACTION:
    def __init__(self, action: dict):
        self.floor: int = action['floor']
        self.eventType: str = action['eventType']
    
        # SetSpeed
        if self.eventType == 'SetSpeed':
            self.speedType: float = action.get('speedType', 'Bpm')
            self.beatsPerMinute: str = action['beatsPerMinute'] if self.speedType == 'Bpm' else None
            self.bpmMultiplier: float = action.get('bpmMultiplier', 1) if self.speedType == 'Multiplier' else None
            self.angleOffset: float = action.get('angleOffset', 0)

        # Twirl
        elif self.eventType == 'Twirl':
            pass
        
        # Checkpoint
        elif self.eventType == 'Checkpoint':
            self.tileOffset: int = action.get('tileOffset', 0)

        # SetHitsound
        elif self.eventType == 'SetHitSound':
            self.gameSound: str = action.get('gameSound', 'hitsound')
            self.hitsound: str = action['hitsound']
            self.hitsoundVolume: int = action['hitsoundVolume']
        
        # PlaySound
        elif self.eventType == 'PlaySound':
            self.hitsound: str = action['hitsound']
            self.hitsoundVolume: int = action['hitsoundVolume']
            self.angleOffset: float = action.get('angleOffset', 0)
            self.eventTag: str = action['eventTag']
        
        # SetPlanetRotation
        elif self.eventType == 'SetPlanetRotation':
            self.ease: str = action['ease']
            self.easeParts: int = action['easeParts']
            self.easePartsBehavior: str = action.get('easePartsBehavior', 'Mirror')
        
        # Pause
        elif self.eventType == 'Pause':
            self.duration: float = action['duration']
            self.countdownTicks: int = action['countdownTicks']
            self.angleCorrectionDir: int = action['angleCorrectionDir']

        # AutoPlayTiles
        elif self.eventType == 'AutoPlayTiles':
            self.enabled: bool = boolean(action['enabled'])
            self.showStatusText: bool = boolean(action['showStatusText'])
            self.safetyTiles: bool = boolean(action.get('safetyTiles', False))

        # ScalePlanets
        elif self.eventType == 'ScalePlanets':
            self.duration: float = action['duration']
            self.targetPlanet: str = action['targetPlanet']
            self.scale: float = action['scale']
            self.angleOffset: float = action['angleOffset']
            self.ease: str = action['ease']
            self.eventTag: str = action['eventTag']

        # ColorTrack
        elif self.eventType == 'ColorTrack':
            self.trackColorType: str = action['trackColorType']
            self.trackColor: str = action['trackColor']
            self.secondaryTrackColor: str = action['secondaryTrackColor']
            self.trackColorAnimDuration: float = action['trackColorAnimDuration']
            self.trackColorPulse: str = action['trackColorPulse']
            self.trackPulseLength: int = action['trackPulseLength']
            self.trackStyle: str = action['trackStyle']
            self.trackTexture: str = action['trackTexture']
            self.trackTextureScale: float = action['trackTextureScale']
            self.trackGlowIntensity: int = action['trackGlowIntensity']
            if 'floorIconOutlines' in action:
                self.floorIconOutlines: bool = boolean(action['floorIconOutlines'])

        # AnimateTrack
        elif self.eventType == 'AnimateTrack':
            if 'trackAnimation' in action:
                self.trackAnimation: str = action['trackAnimation']
                self.beatsAhead: float = action['beatsAhead']
            if 'trackDisappearAnimation' in action:
                self.trackDisappearAnimation: str = action['trackDisappearAnimation']
                self.beatsBehind: float = action['beatsBehind']

        # RecolorTrack
        elif self.eventType == 'RecolorTrack':
            self.startTile: list = action['startTile']
            self.endTile: list = action['endTile']
            self.gapLength: int = action.get('gapLength', 0)
            self.duration: float = action.get('duration', 0)
            self.trackColorType: str = action['trackColorType']
            self.trackColor: str = action['trackColor']
            self.secondaryTrackColor: str = action['secondaryTrackColor']
            self.trackColorAnimDuration: str = action['trackColorAnimDuration']
            self.trackColorPulse: str = action['trackColorPulse']
            self.trackPulseLength: int = action['trackPulseLength']
            self.trackStyle: str = action['trackStyle']
            self.trackGlowIntensity: int = action.get('trackGlowIntensity', 100)
            self.angleOffset: float = action['angleOffset']
            self.ease: str = action.get('ease', 'Linear')
            self.eventTag: str = action['eventTag']

        # MoveTrack
        elif self.eventType == 'MoveTrack':
            self.startTile: list = action['startTile']
            self.endTile: list = action['endTile']
            self.gapLength: int = action.get('gapLength', 0)
            self.duration: float = action['duration']
            self.positionOffset: list = action.get('positionOffset', [None, None])
            if 'rotationOffset' in action:
                self.rotationOffset: float = action['rotationOffset']
            if 'scale' in action:
                self.scale: list[float] = action['scale']
            if 'opacity' in action:
                self.opacity: float = action['opacity']
            self.angleOffset: float = action['angleOffset']
            self.ease: str = action['ease']
            if 'maxVfxOnly' in action:
                self.maxVfxOnly: bool = boolean(action['maxVfxOnly'])
            self.eventTag: str = action['eventTag']

        # PositionTrack
        elif self.eventType == 'PositionTrack':
            self.positionOffset = action['positionOffset']
            self.relativeTo = action.get('relativeTo', [0, "ThisTile"])
            self.rotation = action.get('rotation', 0)
            self.scale = action.get('scale', 100)
            self.opacity = action.get('opacity', 100)
            self.justThisTile = action.get('justThisTile', False)
            self.editorOnly = action['editorOnly']
            if 'stickToFloors' in action:
                self.stickToFloors = action['stickToFloors']

        # MoveDecorations
        elif self.eventType == 'MoveDecorations':
            self.duration = action['duration']
            self.tag = action['tag']
            if 'visible' in action:
                self.visible = action['visible']
            if 'relativeTo' in action:
                self.relativeTo = action['relativeTo']
            if 'decorationImage' in action:
                self.decorationImage = action['decorationImage']
            if 'positionOffset' in action:
                self.positionOffset = action['positionOffset']
            if 'pivotOffset' in action:
                self.pivotOffset = action['pivotOffset']
            if 'rotationOffset' in action:
                self.rotationOffset = action['rotationOffset']
            if 'scale' in action:
                self.scale = action['scale']
            if 'color' in action:
                self.color = action['color']
            if 'opacity' in action:
                self.opacity = action['opacity']
            if 'depth' in action:
                self.depth = action['depth']
            if 'parallax' in action:
                self.parallax = action['parallax']
            if 'parallaxOffset' in action:
                self.parallaxOffset = action.get('parallaxOffset', [None, None])
            self.angleOffset = action['angleOffset']
            self.ease = action['ease']
            self.eventTag = action['eventTag']
            if 'maskingType' in action:
                self.maskingType = action['maskingType']
            if 'useMaskingDepth' in action:
                self.useMaskingDepth = action['useMaskingDepth']
            if 'maskingFrontDepth' in action:
                self.maskingFrontDepth = action['maskingFrontDepth']
            if 'maskingBackDepth' in action:
                self.maskingBackDepth = action['maskingBackDepth']

        # SetText
        elif self.eventType == 'SetText':
            self.decText = action['decText']
            self.tag = action['tag']
            self.angleOffset = action['angleOffset']
            self.eventTag = action['eventTag']

        # SetObject
        elif self.eventType == 'SetObject':
            self.duration = action['duration']
            self.tag = action['tag']
            if 'planetColor' in action:
                self.planetColor = action['planetColor']
            if 'planetTailColor' in action:
                self.planetTailColor = action['planetTailColor']
            if 'trackAngle' in action:
                self.trackAngle = action['trackAngle']
            if 'trackColorType' in action:
                self.trackColorType = action['trackColorType']
            if 'trackColor' in action:
                self.trackColor = action['trackColor']
            if 'secondaryTrackColor' in action:
                self.secondaryTrackColor = action['secondaryTrackColor']
            if 'trackColorAnimDuration' in action:
                self.trackColorAnimDuration = action['trackColorAnimDuration']
            if 'trackOpacity' in action:
                self.trackOpacity = action['trackOpacity']
            if 'trackStyle' in action:
                self.trackStyle = action['trackStyle']
            if 'trackIcon' in action:
                self.trackIcon = action['trackIcon']
            if 'trackIconAngle' in action:
                self.trackIconAngle = action['trackIconAngle']
            if 'trackRedSwirl' in action:
                self.trackRedSwirl = action['trackRedSwirl']
            if 'trackGraySetSpeedIcon' in action:
                self.trackGraySetSpeedIcon = action['trackGraySetSpeedIcon']
            if 'trackGlowEnabled' in action:
                self.trackGlowEnabled = action['trackGlowEnabled']
            if 'trackGlowColor' in action:
                self.trackGlowColor = action['trackGlowColor']
            self.angleOffset = action['angleOffset']
            self.ease = action['ease']
            self.eventTag = action['eventTag']

        # SetDefaultText
        elif self.eventType == 'SetDefaultText':
            self.duration = action['duration']
            self.angleOffset = action['angleOffset']
            self.ease = action['ease']
            if 'defaultTextColor' in action:
                self.defaultTextColor = action['defaultTextColor']
            if 'defaultTextShadowColor' in action:
                self.defaultTextShadowColor = action['defaultTextShadowColor']
            if 'levelTitlePosition' in action:
                self.levelTitlePosition = action['levelTitlePosition']
            if 'levelTitleText' in action:
                self.levelTitleText = action['levelTitleText']
            if 'congratsText' in action:
                self.congratsText = action['congratsText']
            if 'perfectText' in action:
                self.perfectText = action['perfectText']
            self.eventTag = action['eventTag']

        # CustomBackground
        elif self.eventType == 'CustomBackground':
            self.color = action['color']
            self.bgImage = action['bgImage']
            self.imageColor = action['imageColor']
            self.parallax = action['parallax']
            self.bgDisplayMode = action['bgDisplayMode']
            self.imageSmoothing = action.get('imageSmoothing', True)
            self.lockRot = boolean(action['lockRot'])
            self.loopBG = action['loopBG']
            self.scalingRatio = action.get('scalingRatio', action.get('unscaledSize', 100))
            self.angleOffset = action['angleOffset']
            self.eventTag = action['eventTag']

        # Flash
        elif self.eventType == 'Flash':
            self.duration = action['duration']
            self.plane = action['plane']
            self.startColor = action['startColor']
            self.startOpacity = action['startOpacity']
            self.endColor = action['endColor']
            self.endOpacity = action['endOpacity']
            self.angleOffset = action['angleOffset']
            self.ease = action.get('ease', 'Linear')
            self.eventTag = action['eventTag']

        # MoveCamera
        elif self.eventType == 'MoveCamera':
            self.duration = action['duration']
            if 'relativeTo' in action:
                self.relativeTo = action['relativeTo']
            if 'position' in action:
                self.position = action['position']
            if 'rotation' in action:
                self.rotation = action['rotation']
            if 'zoom' in action:
                self.zoom = action['zoom']
            self.angleOffset = action['angleOffset']
            self.ease = action['ease']
            if 'dontDisable' in action:
                self.dontDisable = action['dontDisable']
            if 'minVfxOnly' in action:
                self.minVfxOnly = action['minVfxOnly']
            self.eventTag = action['eventTag']

        # SetFilter
        elif self.eventType == 'SetFilter':
            self.filter = action['filter']
            self.enabled = boolean(action['enabled'])
            self.intensity = action['intensity']
            self.duration = action.get('duration', 0)
            self.ease = action.get('ease', 'Linear')
            self.disableOthers = boolean(action['disableOthers'])
            self.angleOffset = action['angleOffset']
            self.eventTag = action['eventTag']

        # HallOfMirrors
        elif self.eventType == 'HallOfMirrors':
            self.enabled = boolean(action['enabled'])
            self.angleOffset = action['angleOffset']
            self.eventTag = action['eventTag']

        # ShakeScreen
        elif self.eventType == 'ShakeScreen':
            self.duration = action['duration']
            self.strength = action['strength']
            self.intensity = action['intensity']
            self.ease = action.get('ease', 'Linear')
            self.fadeOut = action['fadeOut']
            self.angleOffset = action['angleOffset']
            self.eventTag = action['eventTag']

        # Bloom
        elif self.eventType == 'Bloom':
            self.enabled = boolean(action['enabled'])
            self.threshold = action['threshold']
            self.intensity = action['intensity']
            self.color = action['color']
            self.duration = action.get('duration', 0)
            self.ease = action.get('ease', 'Linear')
            self.angleOffset = action['angleOffset']
            self.eventTag = action['eventTag']

        # ScreenTile
        elif self.eventType == 'ScreenTile':
            self.duration = action['duration']
            self.tile = action['tile']
            self.angleOffset = action['angleOffset']
            self.ease = action['ease']
            self.eventTag = action['eventTag']

        # ScreenScroll
        elif self.eventType == 'ScreenScroll':
            self.scroll = action['scroll']
            self.angleOffset = action['angleOffset']
            self.eventTag = action['eventTag']

        # SetFrameRate
        elif self.eventType == 'SetFrameRate':
            self.enabled = boolean(action['enabled'])
            self.frameRate = action['frameRate']
            self.angleOffset = action['angleOffset']

        # RepeatEvents
        elif self.eventType == 'RepeatEvents':
            self.repeatType = action.get('repeatType', 'Beat')
            self.repetitions = action['repetitions']
            self.floorCount = action.get('floorCount', 1)
            self.interval = action['interval']
            self.executeOnCurrentFloor = action.get('executeOnCurrentFloor', False)
            self.tag = action['tag']

        # SetConditionalEvents
        elif self.eventType == 'SetConditionalEvents':
            self.perfectTag = action['perfectTag']
            self.hitTag = action['hitTag']
            self.earlyPerfectTag = action['earlyPerfectTag']
            self.latePerfectTag = action['latePerfectTag']
            self.barelyTag = action['barelyTag']
            self.veryEarlyTag = action['veryEarlyTag']
            self.veryLateTag = action['veryLateTag']
            self.missTag = action['missTag']
            self.tooEarlyTag = action['tooEarlyTag']
            self.tooLateTag = action['tooLateTag']
            self.lossTag = action['lossTag']
            self.onCheckpointTag = action['onCheckpointTag']

        # EditorComment
        elif self.eventType == 'EditorComment':
            self.comment = action['comment']

        # Bookmark
        elif self.eventType == 'Bookmark':
            pass

        # Hold
        elif self.eventType == 'Hold':
            self.duration = action['duration']
            self.distanceMultiplier = action['distanceMultiplier']
            self.landingAnimation = action['landingAnimation']

        # SetHoldSound
        elif self.eventType == 'SetHoldSound':
            self.holdStartSound = action['holdStartSound']
            self.holdLoopSound = action['holdLoopSound']
            self.holdEndSound = action['holdEndSound']
            self.holdMidSound = action['holdMidSound']
            self.holdMidSoundType = action['holdMidSoundType']
            self.holdMidSoundDelay = action['holdMidSoundDelay']
            self.holdMidSoundTimingRelativeTo = action['holdMidSoundTimingRelativeTo']
            self.holdSoundVolume = action['holdSoundVolume']

        # MultiPlanet
        elif self.eventType == 'MultiPlanet':
            self.planets = action['planets']

        # FreeRoam
        elif self.eventType == 'FreeRoam':
            self.duration = action['duration']
            self.size = action['size']
            self.positionOffset = action['positionOffset']
            self.outTime = action['outTime']
            self.outEase = action['outEase']
            self.hitsoundOnBeats = action['hitsoundOnBeats']
            self.hitsoundOffBeats = action['hitsoundOffBeats']
            self.countdownTicks = action['countdownTicks']
            self.angleCorrectionDir = action['angleCorrectionDir']

        # FreeRoamTwirl
        elif self.eventType == 'FreeRoamTwirl':
            self.position = action['position']

        # FreeRoamRemove
        elif self.eventType == 'FreeRoamRemove':
            self.position = action['position']
            self.size = action['size']

        # Hide
        elif self.eventType == 'Hide':
            self.hideJudgment = action['hideJudgment']
            self.hideTileIcon = action['hideTileIcon']

        # ScaleMargin
        elif self.eventType == 'ScaleMargin':
            self.scale = action['scale']

        # ScaleRadius
        elif self.eventType == 'ScaleRadius':
            self.scale = action['scale']

class DECORATION:
    def __init__(self, decoration: dict):
        self.eventType = decoration['eventType']
        self.position = decoration['position']
        self.relativeTo = decoration['relateceTo']
        self.pivotOffset = decoration['pivotOffset']
        self.rotation = decoration['rotation']
        self.lockRotation = boolean(decoration['lockRotation'])
        self.scale = decoration['scale']
        self.lockScale = boolean(decoration['lockScale'])
        self.depth = decoration['depth']
        self.parallax = decoration['parallax']
        self.parallaxOffset = decoration['parallaxOffset']
        self.tag = decoration['tag']

        if self.relativeTo == 'Tile':
            self.floor = decoration['floor']

        if self.eventType == 'AddDecoration':
            self.decorationImage = decoration['decorationImage']
            self.tile = decoration['tile']
            self.color = decoration['color']
            self.opacity = decoration['opacity']
            self.imageSmoothing = boolean(decoration['imageSmoothing'])
            self.blendMode = decoration['blendMode']
            self.maskingType = decoration['maskingType']
            self.useMaskingDepth = decoration['useMaskingDepth']
            self.maskingFrontDepth = decoration['maskingFrontDepth']
            self.maskingBackDepth = decoration['maskingBackDepth']
            self.hitbox = decoration['hitbox']
            self.hitboxDetectTarget = decoration['hitboxDetectTarget']
            self.hitboxDecoTag = decoration['hitboxDecoTag']
            self.hitboxTriggerType = decoration['hitboxTriggerType']
            self.hitboxRepeatInterval = decoration['hitboxRepeatInterval']
            self.hitboxEventTag = decoration['hitboxEventTag']
            self.failHitboxType = decoration['failHitboxType']
            self.failHitboxScale = decoration['failHitboxScale']
            self.failHitboxOffset = decoration['failHitboxOffset']
            self.failHitboxRotation = decoration['failHitboxRotation']
            self.components = decoration['components']

        if self.eventType == 'AddText':
            self.decText = decoration['decText']
            self.font = decoration['font']
            self.color = decoration['color']
            self.opacity = decoration['opacity']
        
        if self.eventType == 'AddObject':
            self.objectType = decoration['objectType']
            if self.objectType == 'Planet':
                self.planetColorType = decoration['planetColorType']
                self.planetColor = decoration['planetColor']
                self.planetTailColor = decoration['planetTailColor']
            else:
                self.trackType = decoration['trackType']
                self.trackAngle = decoration['trackAngle']
                self.trackColorType = decoration['trackColorType']
                self.trackStyle = decoration['trackStyle']
                self.trackIcon = decoration['trackIcon']
                self.trackIconAngle = decoration['trackIconAngle']
                self.trackRedSwirl = decoration['trackRedSwirl']
                self.trackGraySetSpeedIcon = decoration['trackGraySetSpeedIcon']
                self.trackSetSpeedIconBpm = decoration['trackSetSpeedIconBpm']
                self.trackGlowEnabled = decoration['trackGlowEnabled']
                self.trackGlowColor = decoration['trackGlowColor']

class ADOFAI:
    def __init__(self, contents: dict):
        # pathData or angleData in the level
        self.pathData = contents.get('pathData', None)
        self.angleData = pathData_to_angleData(contents['pathData']) if 'pathData' in contents else contents['angleData']
        # settings of the level
        self.settings_dict = contents['settings']
        self.settings = SETTINGS(contents['settings'])
        # events in this level
        self.actions = contents['actions']
        # decorations in this level
        self.decorations = contents.get('decorations', [])

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
    actions.sort(key = lambda x: ACTION(x).floor)
    return actions

def ADOFAI_print(level: ADOFAI, path: str, info: bool = True) -> None:
    """
    print level in `.adofai` form

    ---
    Parameters:
        `level`: `<ADOFAI>`, level to print
        `path`: path to print
        `info`: some warnings and infomation. 
    """
    angleData = level.angleData
    settings = level.settings_dict
    actions = level.actions
    decorations = level.decorations
    output = f'''{{\n\t\"angleData\": {angleData},\n'''

    output += '\t\"settings\": \n\t{\n'
    for setting in settings:
        space = ' ' if setting in ['version', 'legacyFlash', 'legacyCamRelativeTo', 'legacySpriteTiles', 'legacyTween'] else ''
        output += f'\t\t\"{setting}\": {json.dumps(settings[setting])}{space},\n'
    output = output.rstrip(',\n') + '\n'
    output += '\t},\n'
    
    output += '\t\"actions\": \n\t[\n'
    for action in actions:
        # extracomma = '' if action["eventType"] in ['SetSpeed', 'Twirl', 'SetText', 'SetHitsound', 'PlaySound', 'Hide', 'Pause', 'Hold'] else ','
        line = '{ ' + json.dumps(action).lstrip('{').rstrip('}') + ' }'
        output += f'\t\t{line},\n'
    output = output.rstrip(',\n') + '\n'
    output += '\t],\n'

    output += '\t\"decorations\": \n\t[\n'
    for decoration in decorations:
        line = '{ ' + json.dumps(decoration).lstrip('{').rstrip('}') + '  }'
        output += f'\t\t{line},\n'
    output = output.rstrip(',\n') + '\n'
    output += '\t]\n}'

    if info:
        if os.path.exists(path):
            if input(f'{path} already exists. Do you want to overwrite it? Yes / [No] ') == 'Yes':
                print(output, file=open(path, 'w', encoding='utf-8-sig'))
                print(f'Exported to {path}. ')
            else:
                print('Canceled. ')
                return
        else:
            print(output, file=open(path, 'w', encoding='utf-8-sig'))
    else:
        print(output, file=open(path, 'w', encoding='utf-8-sig'))

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


