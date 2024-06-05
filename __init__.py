import json, os, re, sys
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Prohibit calls to the following funcs
sys.modules["builtins"].__dict__['clearFormat'] = None
sys.modules["builtins"].__dict__['boolean'] = None

__all__ = [
    'ADOFAI_read', 'pathData_to_angleData', 'AskForPath', 'adofai', 'ADOFAI_print'
    'SETTINGS', 'ACTION', 'DECORATION', 'ADOFAI'
]

def AskForPath() -> str:
    """
    Select .adofai file

    ---
    returns:
        .adofai file path
    """
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    icon_path = os.path.join(cur_dir, 'icon.ico')
    root = Tk()
    root.iconbitmap(icon_path)
    root.withdraw()
    return askopenfilename(filetypes=[("ADOFAI files", "*.adofai"), ("ADOFAI files", "*.ADOFAI")])

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
    return level_dir, level_name, extension

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
    fname, extension = os.path.splitext(FILE_PATH)
    if extension not in ['.adofai', '.ADOFAI']:
        print(f'\033[91m[ERROR] The file at \033[93m\033[4m{FILE_PATH}\033[0m\033[91m is not an .adofai file. \033[0m')
        return
    try:
        contents = open(FILE_PATH, 'r', encoding='utf-8-sig').read()
        correction = {
            ", }": "}",
            ",  }": "}",
            "]\n\t\"decorations\"": "],\n\t\"decorations\"",
            "],\n}": "]\n}",
            ",,": ",",
            "}\n\t\t{": "},\n\t\t{",
            "},\n\t]": "}\n\t]",
            "\n\\n": "\\n"
        }
        for c in correction:
            contents = contents.replace(c, correction[c])
        content_dict = json.loads(contents)
        return content_dict
    except FileNotFoundError:
        print(f'\033[91m[ERROR] The file at \033[93m\033[4m{FILE_PATH}\033[0m\033[91m do not exist. \033[0m')
    except PermissionError:
        print(f'\033[91m[ERROR] No permission to view the file at \033[93m\033[4m{FILE_PATH}\033[0m\033[91m. \033[0m')
    except SyntaxError:
        print(f'\033[91m[ERROR] Syntax Error Exists in \033[93m\033[4m{FILE_PATH}\033[0m\033[91m. \033[0m')
    except json.decoder.JSONDecodeError as e:
        print(f'\033[91m[ERROR] JSONDecodeError Exists in \033[93m\033[4m{FILE_PATH}\033[0m\033[91m. \033[0m')
        e=str(e)
        ErrorName, ErrorPlace = e.split(': ')
        pos = [int(i.group()) for i in re.finditer(r'\d+',ErrorPlace)]
        line, column, char = tuple(pos)
        lines = contents.split('\n')
        Error_line = lines[line-1]
        fore, error, behind = Error_line[:column-1], Error_line[column-1], Error_line[column:]
        print(f'\033[2m> line {line} | \033[0m{fore}\033[0m\033[91m{error}\033[90m{behind}\033[0m')

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
        self.version = settings['version']
        self.artist = clearFormat(settings['artist'])
        self.specialArtistType = settings.get('specialArtistType', "None")
        self.artistPermission = settings.get('artistPermission', "")
        self.artistLinks = settings.get('artistLinks', "")

        self.song = clearFormat(settings['song'])
        self.songFilename = settings['songFilename']
        self.author = clearFormat(settings['author'])

        self.previewImage = settings.get('previewImage', "")
        self.previewIcon = settings.get('previewIcon', "")
        self.previewIconColor = settings.get('previewIconColor', "")
        self.previewSongStart = settings.get('previewSongStart', "")
        self.previewSongDuration = settings.get('previewSongDuration', "")

        self.seizureWarning = boolean(settings.get('seizureWarning', False))

        self.levelDesc = settings.get('levelDesc', "")
        self.levelTags = settings.get('levelTags', "")
        
        self.speedTrialAim = settings.get('speedTrialAim', 1.0)
        self.difficulty = settings.get('difficulty', "")
        self.requiredMods = settings.get('requiredMods', [])

        self.bpm = settings['bpm']
        self.volume = settings['volume']
        self.offset = settings['offset']
        self.pitch = settings['pitch']
        self.hitsound = settings['hitsound']
        self.hitsoundVolume = settings['hitsoundVolume']
        self.countdownTicks = settings.get('countdownTicks', 4)
        self.separateCountdownTime = boolean(settings['separateCountdownTime'])

        self.trackColorType = settings['trackColorType']
        self.trackColor = settings['trackColor']
        self.secondaryTrackColor = settings['secondaryTrackColor']
        self.trackColorAnimDuration = settings.get('trackColorAnimDuration', 2)
        self.trackColorPulse = settings.get('trackColorPulse', "None")
        self.trackPulseLength = settings.get('trackPulseLength', 10)
        self.trackStyle = settings['trackStyle']
        self.trackTexture = settings.get('trackTexture', '')
        self.trackTextureScale = settings.get('trackTextureScale', 1)
        self.trackGlowIntensity = settings.get('trackGlowIntensity', 100)
        self.trackAnimation = settings['trackAnimation']
        self.beatsAhead = settings.get('beatsAhead', 4)
        self.trackDisappearAnimation = settings['trackDisappearAnimation']      
        self.beatsBehind = settings.get('beatsBehind', 4)

        self.backgroundColor = settings['backgroundColor']
        self.showDefaultBGIfNoImage = boolean(settings.get('showDefaultBGIfNoImage', True))
        self.showDefaultBGTile = settings.get('showDefaultBGTile', False)
        self.defaultBGTileColor = settings.get('defaultBGTileColor', '101121')
        self.defaultBGShapeType = settings.get('defaultBGShapeType', 'Disabled')
        self.defaultBGShapeColor = settings.get('defaultBGShapeColor', 'ffffff')
        self.bgImage = settings['bgImage']
        self.bgImageColor = settings['bgImageColor']
        self.parallax = settings.get('parallax', 100)
        self.bgDisplayMode = settings.get('bgDisplayMode', 'FitToScreen')
        self.imageSmoothing = settings.get('imageSmoothing', True)
        self.lockRot = boolean(settings.get('lockRot', False))
        self.loopBG = boolean(settings.get('loopBG', False))
        self.scalingRatio = settings.get('scalingRatio', settings.get('unscaledSize', 100))
        self.relativeTo = settings.get('relativeTo', "Player")
        self.position = settings.get('position', [0, 0])
        self.rotation = settings.get('rotation', 0)
        self.zoom = settings.get('zoom', 100)

        self.bgVideo = settings.get('bgVideo', '')
        self.loopVideo = boolean(settings.get('loopVideo', False))
        self.vidOffset = settings.get('vidOffset', 0)
        
        self.pulseOnFloor = settings.get('pulseOnFloor', True)
        self.floorIconOutlines = boolean(settings.get('floorIconOutlines', False))
        self.stickToFloors = boolean(settings.get('stickToFloors', True))

        self.planetEase = settings.get('planetEase', 'Linear')
        self.planetEaseParts = settings.get('planetEaseParts', 1)
        self.planetEasePartBehavior = settings.get('planetEasePartBehavior', 'Mirror')

        self.defaultTextColor = settings.get('defaultTextColor', 'ffffff')
        self.defaultTextShadowColor = settings.get('defaultTextShadowColor', '00000050')
        self.congratsText = settings.get('congratsText', '')
        self.perfectText = settings.get('perfectText', '')

        self.legacyFlash = boolean(settings.get('legacyFlash', False))
        self.legacyCamRelativeTo = boolean(settings.get('legacyCamRelativeTo', False))
        self.legacySpriteTiles = boolean(settings.get('legacySpriteTiles', False))

class ACTION:
    def __init__(self, action: dict):
        self.floor = action['floor']
        self.eventType = action['eventType']
    
        # SetSpeed
        if self.eventType == 'SetSpeed':
            self.speedType = action.get('speedType', 'Bpm')
            self.beatsPerMinute = action['beatsPerMinute'] if self.speedType == 'Bpm' else None
            self.bpmMultiplier = action.get('bpmMultiplier', 1) if self.speedType == 'Multiplier' else None
            self.angleOffset = action.get('angleOffset', 0)

        # Twirl
        elif self.eventType == 'Twirl':
            pass
        
        # Checkpoint
        elif self.eventType == 'Checkpoint':
            self.tileOffset = action.get('tileOffset', 0)

        # SetHitsound
        elif self.eventType == 'SetHitSound':
            self.gameSound = action.get('gameSound', 'hitsound')
            self.hitsound = action['hitsound']
            self.hitsoundVolume = action['hitsoundVolume']
        
        # PlaySound
        elif self.eventType == 'PlaySound':
            self.hitsound = action['hitsound']
            self.hitsoundVolume = action['hitsoundVolume']
            self.angleOffset = action.get('angleOffset', 0)
            self.eventTag = action['eventTag']
        
        # SetPlanetRotation
        elif self.eventType == 'SetPlanetRotation':
            self.ease = action['ease']
            self.easeParts = action['easeParts']
            self.easePartsBehavior = action.get('easePartsBehavior', 'Mirror')
        
        # Pause
        elif self.eventType == 'Pause':
            self.duration = action['duration']
            self.countdownTicks = action['countdownTicks']
            self.angleCorrectionDir = action['angleCorrectionDir']

        # AutoPlayTiles
        elif self.eventType == 'AutoPlayTiles':
            self.enabled = boolean(action['enabled'])
            self.showStatusText = action['showStatusText']
            self.safetyTiles = action['safetyTiles']

        # ScalePlanets
        elif self.eventType == 'ScalePlanets':
            self.duration = action['duration']
            self.targetPlanet = action['targetPlanet']
            self.scale = action['scale']
            self.angleOffset = action['angleOffset']
            self.ease = action['ease']
            self.eventTag = action['eventTag']

        # ColorTrack
        elif self.eventType == 'ColorTrack':
            self.trackColorType = action['trackColorType']
            self.trackColor = action['trackColor']
            self.secondaryTrackColor = action['secondaryTrackColor']
            self.trackColorAnimDuration = action['trackColorAnimDuration']
            self.trackColorPulse = action['trackColorPulse']
            self.trackPulseLength = action['trackPulseLength']
            self.trackStyle = action['trackStyle']
            self.trackTexture = action['trackTexture']
            self.trackTextureScale = action['trackTextureScale']
            self.trackGlowIntensity = action['trackGlowIntensity']
            if 'floorIconOutlines' in action:
                self.floorIconOutlines = action['floorIconOutlines']

        # AnimateTrack
        elif self.eventType == 'AnimateTrack':
            if 'trackAnimation' in action:
                self.trackAnimation = action['trackAnimation']
                self.beatsAhead = action['beatsAhead']
            if 'trackDisappearAnimation' in action:
                self.trackDisappearAnimation = action['trackDisappearAnimation']
                self.beatsBehind = action['beatsBehind']

        # RecolorTrack
        elif self.eventType == 'RecolorTrack':
            self.startTile = action['startTile']
            self.endTile = action['endTile']
            self.gapLength = action.get('gapLength', 0)
            self.duration = action.get('duration', 0)
            self.trackColorType = action['trackColorType']
            self.trackColor = action['trackColor']
            self.secondaryTrackColor = action['secondaryTrackColor']
            self.trackColorAnimDuration = action['trackColorAnimDuration']
            self.trackColorPulse = action['trackColorPulse']
            self.trackPulseLength = action['trackPulseLength']
            self.trackStyle = action['trackStyle']
            self.trackGlowIntensity = action.get('trackGlowIntensity', 100)
            self.angleOffset = action['angleOffset']
            self.ease = action.get('ease', 'Linear')
            self.eventTag = action['eventTag']

        # MoveTrack
        elif self.eventType == 'MoveTrack':
            self.startTile = action['startTile']
            self.endTile = action['endTile']
            self.gapLength = action.get('gapLength', 0)
            self.duration = action['duration']
            self.positionOffset = action['positionOffset']
            if 'rotationOffset' in action:
                self.rotationOffset = action['rotationOffset']
            if 'scale' in action:
                self.scale = action['scale']
            if 'opacity' in action:
                self.scale = action['opacity']
            self.angleOffset = action['angleOffset']
            self.ease = action['ease']
            if 'maxVfxOnly' in action:
                self.maxVfxOnly = action['maxVfxOnly']
            self.eventTag = action['eventTag']

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
        self.pathData = contents['pathData'] if 'pathData' in contents else None
        self.angleData = pathData_to_angleData(contents['pathData']) if 'pathData' in contents else contents['angleData']
        # settings of the level
        self.settings = contents['settings']
        self.setting = SETTINGS(contents['settings'])
        # events in this level
        self.actions = contents['actions']
        # decorations in this level
        self.decorations = contents.get('decorations', [])

def ADOFAI_print(level: ADOFAI, path: str, info: bool = False) -> None:
    """
    print level in `.adofai` form

    ---
    Parameters:
        `level`: `<ADOFAI>`, level to print
        `path`: path to print
    """
    angleData = level.angleData
    settings = level.settings
    actions = level.actions
    decorations = level.decorations
    output = f'''{{\n\t\"angleData\": {angleData},\n'''

    output += '\t\"settings\": \n\t{\n'
    for setting in settings:
        output += f'\t\t\"{setting}\": {json.dumps(settings[setting])}, \n'
    output = output.rstrip(', \n') + '\n'
    output += '\t},\n'
    
    output += '\t\"actions\": \n\t{\n'
    for action in actions:
        output += f'\t\t{json.dumps(action)}, \n'
    output = output.rstrip(', \n') + '\n'
    output += '\t},\n'

    output += '\t\"decorations\": \n\t{\n'
    for decoration in decorations:
        output += f'\t\t{json.dumps(decoration)}, \n'
    output = output.rstrip(', \n') + '\n'
    output += '\t}\n}'

    print(output, file=open(path, 'w', encoding='utf-8-sig'))
    if info:
        print(f'Exported to {path}. ')

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