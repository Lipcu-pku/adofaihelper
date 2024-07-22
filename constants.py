from enum import Enum


true = True
false = False
null = None
settings={
		"version": 14 ,
		"artist": "", 
		"specialArtistType": "None", 
		"artistPermission": "", 
		"song": "", 
		"author": "", 
		"separateCountdownTime": true, 
		"previewImage": "", 
		"previewIcon": "", 
		"previewIconColor": "003f52", 
		"previewSongStart": 0, 
		"previewSongDuration": 10, 
		"seizureWarning": false, 
		"levelDesc": "", 
		"levelTags": "", 
		"artistLinks": "", 
		"speedTrialAim": 0, 
		"difficulty": 1, 
		"requiredMods": [],
		"songFilename": "", 
		"bpm": 100, 
		"volume": 100, 
		"offset": 0, 
		"pitch": 100, 
		"hitsound": "Kick", 
		"hitsoundVolume": 100, 
		"countdownTicks": 4,
		"trackColorType": "Single", 
		"trackColor": "debb7b", 
		"secondaryTrackColor": "ffffff", 
		"trackColorAnimDuration": 2, 
		"trackColorPulse": "None", 
		"trackPulseLength": 10, 
		"trackStyle": "Standard", 
		"trackTexture": "", 
		"trackTextureScale": 1, 
		"trackGlowIntensity": 100, 
		"trackAnimation": "None", 
		"beatsAhead": 3, 
		"trackDisappearAnimation": "None", 
		"beatsBehind": 4,
		"backgroundColor": "000000", 
		"showDefaultBGIfNoImage": true, 
		"showDefaultBGTile": true, 
		"defaultBGTileColor": "101121", 
		"defaultBGShapeType": "Default", 
		"defaultBGShapeColor": "ffffff", 
		"bgImage": "", 
		"bgImageColor": "ffffff", 
		"parallax": [100, 100], 
		"bgDisplayMode": "FitToScreen", 
		"imageSmoothing": true, 
		"lockRot": false, 
		"loopBG": false, 
		"scalingRatio": 100,
		"relativeTo": "Player", 
		"position": [0, 0], 
		"rotation": 0, 
		"zoom": 100, 
		"pulseOnFloor": true,
		"bgVideo": "", 
		"loopVideo": false, 
		"vidOffset": 0, 
		"floorIconOutlines": false, 
		"stickToFloors": true, 
		"planetEase": "Linear", 
		"planetEaseParts": 1, 
		"planetEasePartBehavior": "Mirror", 
		"defaultTextColor": "ffffff", 
		"defaultTextShadowColor": "00000050", 
		"congratsText": "", 
		"perfectText": "",
		"legacyFlash": false ,
		"legacyCamRelativeTo": false ,
		"legacySpriteTiles": false ,
		"legacyTween": true 
	}


for x in settings:
    print(f'{x} = \'{x}\'')

class ADOFAIAttr(Enum):
    pathData = 'pathData'
    angleData = 'angleData'
    settings = 'settings'
    actions = 'actions'
    decorations = 'decorations'

class SettingsAttr(Enum):
    version = 'version'
    artist = 'artist'
    specialArtistType = 'specialArtistType'
    artistPermission = 'artistPermission'
    song = 'song'
    author = 'author'
    separateCountdownTime = 'separateCountdownTime'
    previewImage = 'previewImage'
    previewIcon = 'previewIcon'
    previewIconColor = 'previewIconColor'
    previewSongStart = 'previewSongStart'
    previewSongDuration = 'previewSongDuration'
    seizureWarning = 'seizureWarning'
    levelDesc = 'levelDesc'
    levelTags = 'levelTags'
    artistLinks = 'artistLinks'
    speedTrialAim = 'speedTrialAim'
    difficulty = 'difficulty'
    requiredMods = 'requiredMods'
    songFilename = 'songFilename'
    bpm = 'bpm'
    volume = 'volume'
    offset = 'offset'
    pitch = 'pitch'
    hitsound = 'hitsound'
    hitsoundVolume = 'hitsoundVolume'
    countdownTicks = 'countdownTicks'
    trackColorType = 'trackColorType'
    trackColor = 'trackColor'
    secondaryTrackColor = 'secondaryTrackColor'
    trackColorAnimDuration = 'trackColorAnimDuration'
    trackColorPulse = 'trackColorPulse'
    trackPulseLength = 'trackPulseLength'
    trackStyle = 'trackStyle'
    trackTexture = 'trackTexture'
    trackTextureScale = 'trackTextureScale'
    trackGlowIntensity = 'trackGlowIntensity'
    trackAnimation = 'trackAnimation'
    beatsAhead = 'beatsAhead'
    trackDisappearAnimation = 'trackDisappearAnimation'
    beatsBehind = 'beatsBehind'
    backgroundColor = 'backgroundColor'
    showDefaultBGIfNoImage = 'showDefaultBGIfNoImage'
    showDefaultBGTile = 'showDefaultBGTile'
    defaultBGTileColor = 'defaultBGTileColor'
    defaultBGShapeType = 'defaultBGShapeType'
    defaultBGShapeColor = 'defaultBGShapeColor'
    bgImage = 'bgImage'
    bgImageColor = 'bgImageColor'
    parallax = 'parallax'
    bgDisplayMode = 'bgDisplayMode'
    imageSmoothing = 'imageSmoothing'
    lockRot = 'lockRot'
    loopBG = 'loopBG'
    scalingRatio = 'scalingRatio'
    relativeTo = 'relativeTo'
    position = 'position'
    rotation = 'rotation'
    zoom = 'zoom'
    pulseOnFloor = 'pulseOnFloor'
    bgVideo = 'bgVideo'
    loopVideo = 'loopVideo'
    vidOffset = 'vidOffset'
    floorIconOutlines = 'floorIconOutlines'
    stickToFloors = 'stickToFloors'
    planetEase = 'planetEase'
    planetEaseParts = 'planetEaseParts'
    planetEasePartBehavior = 'planetEasePartBehavior'
    defaultTextColor = 'defaultTextColor'
    defaultTextShadowColor = 'defaultTextShadowColor'
    congratsText = 'congratsText'
    perfectText = 'perfectText'
    legacyFlash = 'legacyFlash'
    legacyCamRelativeTo = 'legacyCamRelativeTo'
    legacySpriteTiles = 'legacySpriteTiles'
    legacyTween = 'legacyTween'

class eventTypes(Enum):    
    SetSpeed = 'SetSpeed'
    Twirl = 'Twirl'
    Checkpoint = 'Checkpoint'
    SetHitsound = 'SetHitsound'
    PlaySound = 'PlaySound'
    SetPlanetRotation = 'SetPlanetRotation'
    Pause = 'Pause'
    AutoPlayTiles = 'AutoPlayTiles'
    ScalePlanets = 'ScalePlanets'
    ColorTrack = 'ColorTrack'
    AnimateTrack = 'AnimateTrack'
    RecolorTrack = 'RecolorTrack'
    MoveTrack = 'MoveTrack'
    PositionTrack = 'PositionTrack'
    MoveDecorations = 'MoveDecorations'
    SetText = 'SetText'
    SetObject = 'SetObject'
    SetDefaultText = 'SetDefaultText'
    CustomBackground = 'CustomBackground'
    Flash = 'Flash'
    MoveCamera = 'MoveCamera'
    SetFilter = 'SetFilter'
    HallOfMirrors = 'HallOfMirrors'
    ShakeScreen = 'ShakeScreen'
    Bloom = 'Bloom'
    ScreenTile = 'ScreenTile'
    ScreenScroll = 'ScreenScroll'
    SetFrameRate = 'SetFrameRate'
    RepeatEvents = 'RepeatEvents'
    SetConditionalEvents = 'SetConditionalEvents'
    EditorComment = 'EditorComment'
    Bookmark = 'Bookmark'
    Hold = 'Hold'
    SetHoldSound = 'SetHoldSound'
    MultiPlanet = 'MultiPlanet'
    FreeRoam = 'FreeRoam'
    FreeRoamTwirl = 'FreeRoamTwirl'
    FreeRoamRemove = 'FreeRoamRemove'
    Hide = 'Hide'
    ScaleMargin = 'ScaleMargin'
    ScaleRadius = 'ScaleRadius'
    AddDecoration = 'AddDecoration'
    AddText = 'AddText'
    AddObject = 'AddObject'
