from enum import Enum, auto
from typing import List, Tuple, Literal
import re

class Value(float):
    """A value of int or float"""
    def __new__(cls, value):
        if isinstance(value, int):
            return value
        elif isinstance(value, float):
            if value.is_integer():
                return int(value)
            return value
        raise TypeError(f"{type(value)} can't be converted to int or float")
    
    def __repr__(self):
        if isinstance(self, int):
            return f'{int(super().__repr__())}'
        return super().__repr__()

NoneType = type(None)

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
    if value == 'Enabled':
        return True
    elif value == 'Disabled':
        return False
    raise ValueError(f'{value} is not a valid boolean value. ')

def value_to_enum(enum_class, value, *invalid_values):
    if isinstance(value, enum_class):
        return value
    try:
        enum_value = enum_class(value)
        if enum_value not in invalid_values:
            return enum_value
        else:
            raise ValueError(f'Invalid value for {enum_class} ("{value}")')
    except:
        raise ValueError(f'Invalid value for {enum_class} ("{value}")')

def value_to_subenum(class_name, value):
    if isinstance(value, Enum):
        return value
    try: 
        enum_value = class_name.get_enum_value(value)
        return enum_value
    except:
        raise ValueError(f'Invalid value for class {class_name} ("{value}")')

def get_value(cls):
    """类装饰器"""
    
    @property
    def value(self):
        """将类转为字典"""
        d = {}
        for key, value in self.__dict__.items():
            if isinstance(value, Enum | DataPair | Color | ParticleColor):
                d[key] = value.value
            else:
                d[key] = value
        return d
    
    def __repr__(self) -> str:
        """使类以字典形式打印"""
        return f'{self.__class__.__name__}({self.value})'

    def hasparam(cls, attr: str) -> bool:
        """检查该类是否存在某参数"""
        return hasattr(cls, attr)

    cls.value = value
    cls.__repr__ = __repr__
    cls.hasattr = hasparam
    return cls


class Color(str):
    """颜色型字符串，仅接受6位或8位的十六进制数"""
    def __init__(self, value):
        if isinstance(value, Color):
            self._value = value._value
        elif isinstance(value, str):
            if not re.fullmatch(r'^[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$', value):
                raise ValueError('Invalid Color value: must be a 6 or 8 character hexadecimal string')
            self. _value = value.lower()
        else:
            raise TypeError('Value must be a string or Color')
    
    @property
    def value(self) -> str:
        return self._value

    def __repr__(self):
        return f'Color({self._value})'

class ADOFAIBool(int, Enum):
    true = True
    false = False

class ADOFAINone(Enum):
    null = None

ADOFAIAttr = Literal[
    'pathData',
    'angleData',
    'settings',
    'actions',
    'decorations',
]

SettingsAttr = Literal[
    'version', 
    'artist',
    'specialArtistType',
    'artistPermission',
    'song',
    'author',
    'separateCountdownTime',
    'previewImage',
    'previewIcon',
    'previewIconColor',
    'previewSongStart',
    'previewSongDuration',
    'seizureWarning',
    'levelDesc',
    'levelTags',
    'artistLinks',
    'speedTrialAim',
    'difficulty',
    'requiredMods',
    'songFilename',
    'bpm',
    'volume',
    'offset',
    'pitch',
    'hitsound',
    'hitsoundVolume',
    'countdownTicks',
    'trackColorType',
    'trackColor',
    'secondaryTrackColor',
    'trackColorAnimDuration',
    'trackColorPulse',
    'trackPulseLength',
    'trackStyle',
    'trackTexture',
    'trackTextureScale',
    'trackGlowIntensity',
    'trackAnimation',
    'beatsAhead',
    'trackDisappearAnimation',
    'beatsBehind',
    'backgroundColor',
    'showDefaultBGIfNoImage',
    'showDefaultBGTile',
    'defaultBGTileColor',
    'defaultBGShapeType',
    'defaultBGShapeColor',
    'bgImage',
    'bgImageColor',
    'parallax',
    'bgDisplayMode',
    'imageSmoothing',
    'lockRot',
    'loopBG',
    'scalingRatio',
    'relativeTo',
    'position',
    'rotation',
    'zoom',
    'pulseOnFloor',
    'bgVideo',
    'loopVideo',
    'vidOffset',
    'floorIconOutlines',
    'stickToFloors',
    'planetEase',
    'planetEaseParts',
    'planetEasePartBehavior',
    'defaultTextColor',
    'defaultTextShadowColor',
    'congratsText',
    'perfectText',
    'legacyFlash',
    'legacyCamRelativeTo',
    'legacySpriteTiles',
    'legacyTween',
    'disableV15Features'
]

class SPECIAL_ARTIST_TYPE(str, Enum):
    """特殊授权"""

    NONE = 'None'
    """无"""
    ARTIST = 'AuthorIsArtist'
    """我是艺术家本人"""
    PUBLIC = 'PublicLicense'
    """公共版权"""

class HITSOUND(str, Enum):
    """打拍音"""

    Hat = 'Hat' 
    """高帽钹"""
    Kick = 'Kick' 
    """底鼓"""
    Shaker = 'Shaker' 
    """沙槌"""
    Sizzle = 'Sizzle'
    """镲片"""
    Chuck = 'Chuck'
    """低音底鼓"""
    ShakerLoud = 'ShakerLoud'
    """沙槌（响）"""
    NONE = 'None'
    """无"""
    Hammer = 'Hammer'
    """音锤"""
    KickChroma = 'KickChroma'
    """底鼓-铬"""
    SnareAcoustic2 = 'SnareAcoustic2'
    """军鼓原声2"""
    Sidestick = 'Sidestick'
    """鼓边"""
    Stick = 'Stick'
    """鼓棒"""
    ReverbClack = 'ReverbClack'
    """混响噼啪"""
    Squareshot = 'Squareshot'
    """正角快照"""
    PowerDown = 'PowerDown'
    """减速音效"""
    PowerUp = 'PowerUp'
    """加速音效"""
    KickHouse = 'KickHouse'
    """底鼓-浩室"""
    KickRupture = 'KickRupture'
    """底鼓-裂解"""
    HatHouse = 'HatHouse'
    """镲片-浩室"""
    SnareHouse = 'SnareHouse'
    """军鼓-浩室"""
    SnareVapor = 'SnareVapor'
    """军鼓-蒸汽"""
    ClapHit = 'ClapHit'
    """拍掌"""
    ClapHitEcho = 'ClapHitEcho'
    """回音拍掌"""
    ReverbClap = 'ReverbClap'
    """混响拍掌"""
    FireTile = 'FireTile'
    """火方块"""
    IceTile = 'IceTile'
    """冰方块"""
    VehiclePositive = 'VehiclePositive'
    """更多星球"""
    VehicleNegative = 'VehicleNegative'
    """更少星球"""

class TRACK_COLOR_TYPE(str, Enum):
    """轨道颜色类型"""
    
    Single = 'Single'
    """单独"""
    Stripes = 'Stripes'
    """条纹"""
    Glow = 'Glow'
    """发光"""
    Blink = 'Blink'
    """闪烁"""
    Switch = 'Switch'
    """切换"""
    Rainbow = 'Rainbow'
    """彩虹"""
    Volume = 'Volume'
    """音量"""
    
class TRACK_COLOR_PULSE(str, Enum):
    """颜色脉冲类型"""

    NONE = 'None'
    """无"""
    Forward = 'Forward'
    """前进"""
    Backward = 'Backward'
    """后退"""

class TRACK_STYLE(str, Enum):
    """轨道风格"""

    Standard = 'Standard'
    """标准"""
    Neon = 'Neon'
    """霓虹"""
    NeonLight = 'NeonLight'
    """霓虹灯"""
    Basic = 'Basic'
    """基础"""
    Gems = 'Gems'
    """宝石"""
    Minimal = 'Minimal'
    """极简"""

class TRACK_ANIMATION(str, Enum):
    """轨道出现动画"""

    NONE = 'None'
    """无"""
    Assemble = 'Assemble'
    """聚合"""
    Assemble_Far = 'Assemble_Far'
    """聚合：远"""
    Extend = 'Extend'
    """延伸"""
    Grow = 'Grow'
    """生长"""
    Grow_Spin = 'Grow_Spin'
    """生长+旋转"""
    Fade = 'Fade'
    """出现"""
    Drop = 'Drop'
    """下坠"""
    Rise = 'Rise'
    """升起"""

class TRACK_DISAPPEAR_ANIMATION(str, Enum):
    """轨道消失动画"""

    NONE = 'None' 
    """无"""
    Scatter = 'Scatter'
    """分散"""
    Scatter_Far = 'Scatter_Far'
    """分散：远"""
    Retract = 'Retract'
    """收缩"""
    Shrink = 'Shrink'
    """暗淡"""
    Shrink_Spin = 'Shrink_Spin'
    """暗淡+旋转"""
    Fade = 'Fade'
    """出现"""

class DEFAULT_BG_SHAPE_TYPE(str, Enum):
    """教程背景图形"""

    Default = 'Default'
    """默认"""
    SingleColor = 'SingleColor'
    """纯色"""
    Disabled = 'Disabled'
    """无"""

class BG_DISPLAY_MODE(str, Enum):
    """背景图片显示格式"""

    FitToScreen = 'FitToScreen'
    """拉伸"""
    Unscaled = 'Unscaled'
    """未缩放"""
    Tiled = 'Tiled'
    """平铺"""

class CAMERA_RELATIVE(str, Enum):
    """摄像头相对于"""

    Player = 'Player'
    """玩家"""
    Tile = 'Tile'
    """方块"""
    Global = 'Global'
    """全局"""
    LastPosition = 'LastPosition'
    """上次位置"""
    LastPositionNoRotation = 'LastPositionNoRotation'
    """上次位置（无旋转）"""

class EASE(str, Enum):
    """缓速"""

    Linear = 'Linear'
    """线性"""
    InSine = 'InSine'
    """正弦缓入"""
    OutSine = 'OutSine'
    """正弦缓出"""
    InOutSine = 'InOutSine'
    """正弦缓入缓出"""
    InQuad = 'InQuad'
    """二次缓入"""
    OutQuad = 'OutQuad'
    """二次缓出"""
    InOutQuad = 'InOutQuad'
    """二次缓入缓出"""
    InCubic = 'InCubic'
    """三次缓入"""
    OutCubic = 'OutCubic'
    """三次缓出"""
    InOutCubic = 'InOutCubic'
    """三次缓入缓出"""
    InQuart = 'InQuart'
    """四次缓入"""
    OutQuart = 'OutQuart'
    """四次缓出"""
    InOutQuart = 'InOutQuart'
    """四次缓入缓出"""
    InQuint = 'InQuint'
    """五次缓入"""
    OutQuint = 'OutQuint'
    """五次缓出"""
    InOutQuint = 'InOutQuint'
    """五次缓入缓出"""
    InExpo = 'InExpo'
    """指数缓入"""
    OutExpo = 'OutExpo'
    """指数缓出"""
    InOutExpo = 'InOutExpo'
    """指数缓入缓出"""
    InCirc = 'InCirc'
    """弧形缓入"""
    OutCirc = 'OutCirc'
    """弧形缓出"""
    InOutCirc = 'InOutCirc'
    """弧形缓入缓出"""
    InElastic = 'InElastic'
    """弹性缓入"""
    OutElastic = 'OutElastic'
    """弹性缓出"""
    InOutElastic = 'InOutElastic'
    """弹性缓入缓出"""
    InBack = 'InBack'
    """回弹缓入"""
    OutBack = 'OutBack'
    """回弹缓出"""
    InOutBack = 'InOutBack'
    """回弹缓入缓出"""
    InBounce = 'InBounce'
    """弹跳缓入"""
    OutBounce = 'OutBounce'
    """弹跳缓出"""
    InOutBounce = 'InOutBounce'
    """弹跳缓入缓出"""
    Flash = 'Flash'
    """闪现"""
    InFlash = 'InFlash'
    """闪现缓入"""
    OutFlash = 'OutFlash'
    """闪现缓出"""
    InOutFlash = 'InOutFlash'
    """闪现缓入缓出"""

class EASE_PART_BEHAVIOR(str, Enum):
    """缓速部分行为"""

    Mirror = 'Mirror'
    """镜像"""
    Repeat = 'Repeat'
    """重复"""

class eventTypes: 
    class Gameplay(str, Enum):
        """玩法类"""

        SetSpeed = 'SetSpeed'
        """设置速度"""
        Twirl = 'Twirl'
        """旋转"""
        Checkpoint = 'Checkpoint'
        """检查点"""
        SetHitsound = 'SetHitsound'
        """设置打拍音"""
        PlaySound = 'PlaySound'
        """播放音效"""
        SetPlanetRotation = 'SetPlanetRotation'
        """设置星球轨道"""
        Pause = 'Pause'
        """暂停"""
        AutoPlayTiles = 'AutoPlayTiles'
        """自动播放格子"""
        ScalePlanets = 'ScalePlanets'
        """缩放行星"""
    
    class TrackEvents(str, Enum):
        """轨道类"""

        ColorTrack = 'ColorTrack'
        """设置轨道颜色"""
        AnimateTrack = 'AnimateTrack'
        """设置轨道动画"""
        RecolorTrack = 'RecolorTrack'
        """重新设置轨道颜色"""
        MoveTrack = 'MoveTrack'
        """移动轨道"""
        PositionTrack = 'PositionTrack'
        """位置轨道"""
    
    class DecorationEvents(str, Enum):
        """装饰类"""

        MoveDecorations = 'MoveDecorations'
        """移动装饰"""
        SetText = 'SetText'
        """设置文本"""
        EmitParticle = 'EmitParticle'
        """发射粒子"""
        SetParticle = 'SetParticle'
        """设置粒子"""
        SetObject = 'SetObject'
        """设置对象"""
        SetDefaultText = 'SetDefaultText'
        """设置默认文本"""
    
    class VisualEffects(str, Enum):
        """视效类"""

        CustomBackground = 'CustomBackground'
        """设置背景"""
        Flash = 'Flash'
        """闪光"""
        MoveCamera = 'MoveCamera'
        """移动摄像头"""
        SetFilter = 'SetFilter'
        """预设滤镜"""
        SetFilterAdvanced = 'SetFilterAdvanced'
        """预设高级滤镜"""
        HallOfMirrors = 'HallOfMirrors'
        """镜厅"""
        ShakeScreen = 'ShakeScreen'
        """振屏"""
        Bloom = 'Bloom'
        """绽放"""
        ScreenTile = 'ScreenTile'
        """平铺"""
        ScreenScroll = 'ScreenScroll'
        """卷屏"""
        SetFrameRate = 'SetFrameRate'
        """设置帧率"""
    
    class Modifiers(str, Enum):
        """调整类"""

        RepeatEvents = 'RepeatEvents'
        """重复事件"""
        SetConditionalEvents = 'SetConditionalEvents'
        """设置条件事件"""
        SetInputEvent = 'SetInputEvent'
        """设置输入事件"""
    
    class Conveniences(str, Enum):
        """易用性类"""

        EditorComment = 'EditorComment'
        """编辑器附注"""
        Bookmark = 'Bookmark'
        """书签"""
    
    class DLC(str, Enum):
        """DLC类"""

        Hold = 'Hold'
        """长按"""
        SetHoldSound = 'SetHoldSound'
        """设置长按音效"""
        MultiPlanet = 'MultiPlanet'
        """多星球"""
        FreeRoam = 'FreeRoam'
        """自由移动段落"""
        FreeRoamTwirl = 'FreeRoamTwirl'
        """自由旋转"""
        FreeRoamRemove = 'FreeRoamRemove'
        """自由移除"""
        Hide = 'Hide'
        """隐藏判定/地图图标"""
        ScaleMargin = 'ScaleMargin'
        """定时窗口大小"""
        ScaleRadius = 'ScaleRadius'
        """星球半径大小"""
    
    class AddDecorations(str, Enum):
        """添加装饰类"""
        
        AddDecoration = 'AddDecoration'
        """添加装饰"""
        AddText = 'AddText'
        """条件文字"""
        AddObject = 'AddObject'
        """添加对象"""
        AddParticle = 'AddParticle'
        """添加粒子"""

    _value_to_enum = {
        e.value : e
        for name, obj in vars().items()
        if isinstance(obj, type) and issubclass(obj, Enum)
        for e in obj
    }

    def __new__(cls, value: str):
        if value in cls._value_to_enum:
            return cls._value_to_enum[value]
        raise ValueError(f"'{value}' is not a valid eventType")


EventTypes = eventTypes.Gameplay | eventTypes.TrackEvents | eventTypes.DecorationEvents | eventTypes.VisualEffects | eventTypes.Modifiers | eventTypes.Conveniences | eventTypes.DLC | eventTypes.AddDecorations

class SpeedType(str, Enum):
    """设置速度类型"""

    Bpm = 'Bpm'
    """BPM"""
    Multiplier = 'Multiplier'
    """倍频器"""

class GameSound(str, Enum):
    """打拍音设置目标"""

    Hitsound = 'Hitsound'
    """普通击拍音效"""
    Midspin = 'Midspin'
    """中旋击拍音效"""

class Planet(str, Enum):
    """行星"""

    FirePlanet = 'FirePlanet'
    """火之行星"""
    IcePlanet = 'IcePlanet'
    """冰之行星"""
    GreenPlanet = 'GreenPlanet'
    """风之行星"""
    All = 'All'
    """所有行星"""

class TileRelative(str, Enum):
    """轨道相对于"""

    ThisTile = 'ThisTile'
    """本方块"""
    Start = 'Start'
    """起点方块"""
    End = 'End'
    """终点方块"""

class Data_Pair:
    """数据对类型"""

    class TilePosition:
        def __init__(self, tile_position: int, tile_relativeto: TileRelative):
            if not isinstance(tile_position, int):
                raise TypeError('The first value in TilePosition must be an integer')
            if not isinstance(tile_relativeto, TileRelative):
                raise TypeError('The second value in TilePosition must be an instance of TileRelative')
            self._tile_position = tile_position
            self._tile_relativeto = tile_relativeto
        
        @property
        def tile_position(self) ->int:
            return self._tile_position
        
        @tile_position.setter
        def tile_position(self, value: int):
            if not isinstance(value, int):
                raise TypeError('The first value in TilePosition must be an integer')
            self._tile_position = value

        @property
        def tile_relativeto(self) -> TileRelative:
            return self._tile_relativeto
        
        @tile_relativeto.setter
        def tile_relativeto(self, value: TileRelative):
            if not isinstance(value, TileRelative):
                raise TypeError('The second value in TilePosition must be an instance of TileRelative')
            self._tile_relativeto = value
        
        @classmethod
        def from_int_str(cls, int_str_tuple: tuple | list):
            tile_position, tile_relativeto = int_str_tuple[0], int_str_tuple[1]
            if not isinstance(tile_position, int):
                raise TypeError('The first value in TilePosition must be an integer')
            if not isinstance(tile_relativeto, str):
                raise TypeError('The second value in TilePosition must be a string value of TileRelative')
            try:
                enum_value = TileRelative(tile_relativeto)
            except ValueError:
                raise ValueError(f'"{tile_relativeto}" is not a valid value for TileRelative')
            return cls(tile_position, enum_value)
        
        def __repr__(self) -> str:
            return f'TilePosition(tile_position={self.tile_position}, tile_relativeto={self.tile_relativeto})'

        @property
        def value(self):
            return (self.tile_position, self.tile_relativeto.value)

    class XY_NonePair:
        """允许None存在的(x, y)值对"""
        def __init__(self, x: float | int | None = None, y: float | int | None = None) -> None:
            if not (isinstance(x, float | int | NoneType) and isinstance(y, float | int | NoneType)):
                raise TypeError('Both values in XYPair must be either float or int or NoneType')
            self._x = x
            self._y = y
        
        @property
        def x(self):
            return self._x
        
        @x.setter
        def x(self, value: float | int | None):
            if not isinstance(value, float | int | NoneType):
                raise TypeError('x must be float or int or NoneType')
            self._x = value

        @property
        def y(self):
            return self._y
        
        @y.setter
        def y(self, value: float | int | None):
            if not isinstance(value, float | int | NoneType):
                raise TypeError('y must be float or int or NoneType')
            self._y = value
        
        def __repr__(self):
            return f'XY_NonePair(x={self._x}, y={self._y})'

        def _tuple(self):
            return (self._x, self._y)

        @property
        def value(self):
            return (self._x, self._y)

        @classmethod
        def from_tuple(cls, data_tuple : tuple | list):
            x, y = data_tuple[0], data_tuple[1]
            if not (isinstance(x, float | int | NoneType) and isinstance(y, float | int | NoneType)):
                raise TypeError('Both values in XY_NonePair must be either float or int or NoneType')
            return cls(x, y)

    class XY_Pair:
        """不允许None存在的(x, y)值对"""
        def __init__(self, x: float | int = 0, y: float | int = 0) -> None:
            if not (isinstance(x, float | int) and isinstance(y, float | int)):
                raise TypeError('Both values in XYPair must be float or int')
            self._x = x
            self._y = y
        
        @property
        def x(self):
            return self._x
        
        @x.setter
        def x(self, value: float | int):
            if not isinstance(value, float | int):
                raise TypeError('x must be float or int')
            self._x = value

        @property
        def y(self):
            return self._y
        
        @y.setter
        def y(self, value: float | int):
            if not isinstance(value, float | int):
                raise TypeError('y must be float or int')
            self._y = value
        
        def __repr__(self):
            return f'XY_Pair(x={self._x}, y={self._y})'

        def _tuple(self):
            return (self._x, self._y)

        @property
        def value(self):
            return (self._x, self._y)

        @classmethod
        def from_tuple(cls, data_tuple : tuple | list):
            x, y = data_tuple[0], data_tuple[1]
            if not (isinstance(x, float | int) and isinstance(y, float | int)):
                raise TypeError('Both values in XY_Pair must be float or int')
            return cls(x, y)

    class XY_natural_Pair:
        """不允许None存在的(x, y)自然数值对"""
        def __init__(self, x: int = 0, y: int = 0, zero_allowed : bool = True) -> None:
            if not (isinstance(x, int) and isinstance(y, int)):
                raise TypeError('Both values in XYPair must be int')
            if not ((x >= 0) and (y >= 0)):
                raise ValueError('Both values should be natural')
            if not zero_allowed:
                if (x == 0) or (y == 0):
                    raise ValueError('Both values should be positive')
            self._x = x
            self._y = y
        
        @property
        def x(self):
            return self._x
        
        @x.setter
        def x(self, value: int):
            if not isinstance(value, int):
                raise TypeError('x must be float or int')
            if value < 0:
                raise ValueError('x should be natural')
            self._x = value

        @property
        def y(self):
            return self._y
        
        @y.setter
        def y(self, value: int):
            if not isinstance(value, int):
                raise TypeError('y must be float or int')
            if value < 0:
                raise ValueError('y should be natural')
            self._y = value
        
        def __repr__(self):
            return f'XY_Pair(x={self._x}, y={self._y})'

        def _tuple(self):
            return (self._x, self._y)

        @property
        def value(self):
            return (self._x, self._y)

        @classmethod
        def from_tuple(cls, data_tuple : tuple | list, zero_allowed : bool = True):
            x, y = data_tuple[0], data_tuple[1]
            if not (isinstance(x, int) and isinstance(y, int)):
                raise TypeError('Both values in XY_Pair must be int')
            if not ((x >= 0) and (y >= 0)):
                raise ValueError('Both values should be natural')
            if not zero_allowed:
                if (x == 0) or (y == 0):
                    raise ValueError('Both values should be positive')
            return cls(x, y)

    class Range_Pair:
        """不允许None存在的(value1, value2)值对"""
        def __init__(self, value1: float | int = 0, value2: float | int = 0) -> None:
            if not (isinstance(value1, float | int) and isinstance(value2, float | int)):
                raise TypeError('Both values in Range_Pair must be float or int')
            self._1 = value1
            self._2 = value2
        
        @property
        def value1(self):
            return self._1
        
        @value1.setter
        def value1(self, value: float | int):
            if not isinstance(value, float | int):
                raise TypeError('value1 must be float or int')
            self._1 = value

        @property
        def value2(self):
            return self._2
        
        @value2.setter
        def value2(self, value: float | int):
            if not isinstance(value, float | int):
                raise TypeError('value2 must be float or int')
            self._2 = value
        
        def __repr__(self):
            return f'Range_Pair(value1={self._1}, value2={self._2})'

        def _tuple(self):
            return (self._1, self._2)

        @property
        def value(self):
            return (self._1, self._2)

        @classmethod
        def from_tuple(cls, data_tuple : tuple | list):
            x, y = data_tuple[0], data_tuple[1]
            if not (isinstance(x, float | int) and isinstance(y, float | int)):
                raise TypeError('Both values in Range_Pair must be float or int')
            return cls(x, y)

    class Increasing_Range_Pair:
        """不允许None存在的(value1, value2)递增值对"""
        def __init__(self, value1: float | int = 0, value2: float | int = 0) -> None:
            if not (isinstance(value1, float | int) and isinstance(value2, float | int)):
                raise TypeError('Both values in XYPair must be float or int')
            if value1 > value2:
                raise ValueError('value1 must be equal or greater than value2')
            self._1 = value1
            self._2 = value2
        
        @property
        def value1(self):
            return self._1
        
        @value1.setter
        def value1(self, value: float | int):
            if not isinstance(value, float | int):
                raise TypeError('value1 must be float or int')
            self._1 = value

        @property
        def value2(self):
            return self._2
        
        @value2.setter
        def value2(self, value: float | int):
            if not isinstance(value, float | int):
                raise TypeError('value2 must be float or int')
            self._2 = value
        
        def __repr__(self):
            return f'Range_Pair(value1={self._1}, value2={self._2})'

        def _tuple(self):
            return (self._1, self._2)

        @property
        def value(self):
            if self._1 > self._2:
                raise ValueError('value1 must be equal or smaller than value2')
            return (self._1, self._2)

        @classmethod
        def from_tuple(cls, data_tuple : tuple | list):
            x, y = data_tuple[0], data_tuple[1]
            if not (isinstance(x, float | int) and isinstance(y, float | int)):
                raise TypeError('Both values in Range_Pair must be float or int')
            if x > y:
                raise ValueError('value1 must be equal or smaller than value2')
            return cls(x, y)

    class Increasing_XY_Pair:
        """不允许None存在的((x1, y1), (x2, y2))的增长值对"""
        def __init__(self, x1: float | int, y1: float | int, x2: float | int, y2: float | int) -> None:
            if not (isinstance(x1, float | int) and isinstance(y1, float | int) and isinstance(x2, float | int) and isinstance(y2, float | int)):
                raise TypeError('numbers in Increasing_XY_Pair must be float or int')
            self._x1 = x1
            self._y1 = y1
            self._x2 = x2
            self._y2 = y2
        
        @property
        def x1(self):
            return self._x1
        
        @x1.setter
        def x1(self, value: float | int):
            if not isinstance(value, float | int):
                raise TypeError('x1 must be float or int')
            self._x1 = value
        
        @property
        def y1(self):
            return self._y1
        
        @y1.setter
        def y1(self, value: float | int):
            if not isinstance(value, float | int):
                raise TypeError('y1 must be float or int')
            self._y1 = value
        
        @property
        def x2(self):
            return self._x2
        
        @x2.setter
        def x2(self, value: float | int):
            if not isinstance(value, float | int):
                raise TypeError('x2 must be float or int')
            self._x2 = value
        
        @property
        def y2(self):
            return self._y2
        
        @y2.setter
        def y2(self, value: float | int):
            if not isinstance(value, float | int):
                raise TypeError('y2 must be float or int')
            self._y2 = value
        
        @property
        def value(self):
            return ((self._x1, self._y1), (self._x2, self._y2))

        def __repr__(self):
            return f'Increasing_XY_Pair(x1={self._x1}, y1={self._y1}, x2={self._x2}, y2={self._y2})'

        @classmethod
        def from_tuple(cls, data_tuple: Tuple[Tuple | List] | List[Tuple | List]):
            x1, y1, x2, y2 = data_tuple[0][0], data_tuple[0][1], data_tuple[1][0], data_tuple[1][1]
            if not (isinstance(x1, float | int) and isinstance(y1, float | int) and isinstance(x2, float | int) and isinstance(y2, float | int)):
                raise TypeError('numbers in Increasing_XY_Pair must be float or int')
            return cls(x1, y1, x2, y2)

DataPair = Data_Pair.XY_Pair | Data_Pair.XY_NonePair | Data_Pair.XY_natural_Pair | Data_Pair.TilePosition | Data_Pair.Range_Pair | Data_Pair.Increasing_Range_Pair | Data_Pair.Increasing_XY_Pair

class DecorationRelative(str, Enum):
    """装饰物相对于"""

    Tile = 'Tile'
    """方块"""
    Global = 'Global'
    """全局"""
    RedPlanet = 'RedPlanet'
    """火之行星"""
    BluePlanet = 'BluePlanet'
    """冰之行星"""
    GreenPlanet = 'GreenPlanet'
    """风之行星"""
    Camera = 'Camera'
    """镜头"""
    CameraAspect = 'CameraAspect'
    """镜头（屏幕比例）"""
    LastPosition = 'LastPosition'
    """上次位置"""

class MaskType(str, Enum):
    """遮罩类型"""

    NONE = 'None'
    """无"""
    Mask = 'Mask'
    """遮盖其他装饰"""
    VisibleInsideMask = 'VisibleInsideMask'
    """显示叠层"""
    VisibleOutsideMask = 'VisibleOutsideMask'
    """隐藏叠层"""

class ParticleMode(str, Enum):
    """粒子模式"""

    Start = 'Start'
    """开始"""
    Stop = 'Stop'
    """停止"""
    Clear = 'Clear'
    """停止并清空"""

class ParticleColor:
    """粒子颜色"""

    def __init__(self, **kwargs):
        self.color1 = Color(kwargs['color1'])
        self.mode = ParticleColor.ParticleColorMode(kwargs['mode'])
        match self.mode:
            case ParticleColor.ParticleColorMode.TwoColors:
                self.color2 = Color(kwargs['color2'])
            case ParticleColor.ParticleColorMode.Gradient | ParticleColor.ParticleColorMode.RandomColor:
                self.gradient1 = ParticleColor.ParticleGradient(**kwargs['gradient1'])
            case ParticleColor.ParticleColorMode.TwoGradients:
                self.gradient1 = ParticleColor.ParticleGradient(**kwargs['gradient1'])
                self.gradient2 = ParticleColor.ParticleGradient(**kwargs['gradient2'])
    
    class ParticleColorMode(str, Enum):
        """粒子颜色模式"""

        Color = 'Color'
        """颜色"""
        Gradient = 'Gridient'
        """渐变"""
        TwoColors = 'TwoColors'
        """随机中间颜色"""
        TwoGradients = 'TwoGradients'
        """随机中间渐变"""
        RandomColor = 'RandomColor'
        """随机渐变"""
    
    class ParticleGradient:
        def __init__(self, **kwargs) -> None:
            self.mode = ParticleColor.ParticleGradient.GradientMode(kwargs['mode'])
            self.alphaKeys = [ParticleColor.ParticleGradient.AlphaKey(key) for key in kwargs['alphaKeys']]
            self.colorKeys = [ParticleColor.ParticleGradient.ColorKey(key) for key in kwargs['colorKeys']]
        
        class GradientMode(str, Enum):
            """渐变类型"""

            Blend = 'Blend'
            """混合"""
            Fixed = 'Fixed'
            """固定"""
            PerceptualBlend = 'PerceptualBlend'
            """感知混合"""


        class AlphaKey:
            def __init__(self, **kwargs) -> None:
                self.time : float | int = kwargs['time']
                self.alpha : float | int = kwargs['alpha']
            
            @property
            def value(self):
                return {"time": self.time, "alpha": self.alpha}
        
        class ColorKey:
            def __init__(self, **kwargs) -> None:
                self.time : float | int = kwargs['time']
                self.color : Color = Color(kwargs['color'])
            
            @property
            def value(self):
                return {"time": self.time, "color": self.color.value}
        
        def add_alphaKey(self, time: float | int, alpha: float | int):
            self.alphaKeys.append(ParticleColor.ParticleGradient.AlphaKey(time=time, alpha=alpha))
        
        def add_colorKey(self, time: float | int, color: Color | str):
            self.colorKeys.append(ParticleColor.ParticleGradient.ColorKey(time=time, color=color))
        
        @property
        def value(self):
            return {
                "mode": self.mode.value,
                "alphaKeys": [alphakey.value for alphakey in self.alphaKeys],
                "colorKeys": [colorkey.value for colorkey in self.colorKeys]
            }
        
    @property
    def value(self):
        match self.mode:
            case ParticleColor.ParticleColorMode.Color:
                return {
                    "color1": self.color1.value,
                    "mode": self.mode.value
                }
            case ParticleColor.ParticleColorMode.TwoColors:
                return {
                    "color1": self.color1.value,
                    "color2": self.color2.value,
                    "mode": self.mode.value
                }
            case ParticleColor.ParticleColorMode.Gradient | ParticleColor.ParticleColorMode.RandomColor:
                return {
                    "color1": self.color1.value,
                    "gradient1": self.gradient1.value,
                    "mode": self.mode.value
                }
            case ParticleColor.ParticleColorMode.TwoGradients:
                return {
                    "color1": self.color1.value,
                    "gradient1": self.gradient1.value,
                    "gradient2": self.gradient2.value,
                    "mode": self.mode.value
                }
            case _:
                raise ValueError('Invalid mode for ParticleColor')

class ParticleShapeType(str, Enum):
    """粒子形状"""
    
    Circle = 'Circle'
    """圆形"""
    Rectangle = 'Rectangle'
    """矩形"""

class ParticleArcMode(str, Enum):
    """粒子弧模式"""

    Random = 'Random'
    """随机"""
    Loop = 'Loop'
    """循环"""
    PingPong = 'PingPong'
    """Ping Pong"""
    BurstSpread = 'BurstSpread'
    """炸裂传播"""

class TrackIcon(str, Enum):
    """轨道图标"""

    NONE = 'None'
    """无"""
    Snail = 'Snail'
    """蜗牛"""
    DoubleSnail = 'DoubleSnail'
    """双蜗牛"""
    Rabbit = 'Rabbit'
    """兔子"""
    DoubleRabbit = 'DoubleRabbit'
    """双兔子"""
    Swirl = 'Swirl'
    """漩涡"""
    Checkpoint = 'Checkpoint'
    """检查点"""
    HoldArrowShort = 'HoldArrowShort'
    """短长按箭头"""
    HoldArrowLong = 'HoldArrowLong'
    """长长按箭头"""
    HoldReleaseShort = 'HoldReleaseShort'
    """短长按释放"""
    HoldReleaseLong = 'HoldReleaseLong'
    """长长按释放"""
    MultiPlanetTwo = 'MultiPlanetTwo'
    """双星"""
    MultiPlanetThreeMore = 'MultiPlanetThreeMore'
    """三星"""
    Portal = 'Portal'
    """传送门"""

class Plane(str, Enum):
    """闪光平面"""

    Foreground = 'Foreground'
    """前景"""
    Background = 'Background'
    """背景"""

class Filter(str, Enum):
    """滤镜"""

    Grayscale = 'Grayscale'
    """灰阶"""
    Sepia = 'Sepia'
    """复古"""
    Invert = 'Invert'
    """反色"""
    VHS = 'VHS'
    """录像带"""
    EightiesTV = 'EightiesTV'
    """80年代电视"""
    FiftiesTV = 'FiftiesTV'
    """50年代电视"""
    Arcade = 'Arcade'
    """街机"""
    LED = 'LED'
    """LED"""
    Rain = 'Rain'
    """雨水"""
    Blizzard = 'Blizzard'
    """暴雪"""
    PixelSnow = 'PixelSnow'
    """像素雪"""
    Compression = 'Compression'
    """压缩"""
    Glitch = 'Glitch'
    """故障"""
    Pixelate = 'Pixelate'
    """像素"""
    Waves = 'Waves'
    """示波"""
    Static = 'Static'
    """静电"""
    Grain = 'Grain'
    """胶片噪点"""
    MotionBlur = 'MotionBlur'
    """运动模糊"""
    Fisheye = 'Fisheye'
    """鱼眼"""
    Aberration = 'Aberration'
    """像差"""
    Drawing = 'Drawing'
    """涂鸦"""
    Neon = 'Neon'
    """霓虹"""
    Handheld = 'Handheld'
    """8比特掌机"""
    NightVision = 'NightVision'
    """夜视"""
    Funk = 'Funk'
    """放克"""
    Tunnel = 'Tunnel'
    """隧道"""
    Weird3D = 'Weird3D'
    """怪异3D"""
    Blur = 'Blur'
    """模糊"""
    BlurFocus = 'BlurFocus'
    """模糊聚焦"""
    GaussianBlur = 'GaussianBlur'
    """高斯模糊"""
    HexagonBlack = 'HexagonBlack'
    """六边形黑圈"""
    Posterize = 'Posterize'
    """色调分离"""
    Sharpen = 'Sharpen'
    """锐化"""
    Contrast = 'Contrast'
    """对比度"""
    EdgeBlackLine = 'EdgeBlackLine'
    """边缘描黑"""
    OilPaint = 'OilPaint'
    """油画"""
    SuperDot = 'SuperDot'
    """点阵"""
    WaterDrop = 'WaterDrop'
    """水滴"""
    LightWater = 'LightWater'
    """涟漪"""
    Petals = 'Petals'
    """落花"""
    PetalsInstant = 'PetalsInstant'
    """落花（直接）"""

class AdvancedFilterName(str, Enum):
    """高级滤镜"""

    AAA_SuperComputer = 'CameraFilterPack_AAA_SuperComputer'
    AAA_SuperHexagon = 'CameraFilterPack_AAA_SuperHexagon'
    AAA_WaterDrop = 'CameraFilterPack_AAA_WaterDrop'
    Alien_Vision = 'CameraFilterPack_Alien_Vision'
    Atmosphere_Rain = 'CameraFilterPack_Atmosphere_Rain'
    Atmosphere_Rain_Pro = 'CameraFilterPack_Atmosphere_Rain_Pro'
    Atmosphere_Snow_8bits = 'CameraFilterPack_Atmosphere_Snow_8bits'
    Blizzard = 'CameraFilterPack_Blizzard'
    Blur_Bloom = 'CameraFilterPack_Blur_Bloom'
    Blur_BlurHole = 'CameraFilterPack_Blur_BlurHole'
    Blur_Blurry = 'CameraFilterPack_Blur_Blurry'
    Blur_Dithering2x2 = 'CameraFilterPack_Blur_Dithering2x2'
    Blur_DitherOffset = 'CameraFilterPack_Blur_DitherOffset'
    Blur_Focus = 'CameraFilterPack_Blur_Focus'
    Blur_GaussianBlur = 'CameraFilterPack_Blur_GaussianBlur'
    Blur_Movie = 'CameraFilterPack_Blur_Movie'
    Blur_Noise = 'CameraFilterPack_Blur_Noise'
    Blur_Radial = 'CameraFilterPack_Blur_Radial'
    Blur_Radial_Fast = 'CameraFilterPack_Blur_Radial_Fast'
    Blur_Regular = 'CameraFilterPack_Blur_Regular'
    Blur_Steam = 'CameraFilterPack_Blur_Steam'
    Blur_Tilt_Shift = 'CameraFilterPack_Blur_Tilt_Shift'
    Blur_Tilt_Shift_Hole = 'CameraFilterPack_Blur_Tilt_Shift_Hole'
    Blur_Tilt_Shift_V = 'CameraFilterPack_Blur_Tilt_Shift_V'
    Colors_Adjust_ColorRGB = 'CameraFilterPack_Colors_Adjust_ColorRGB'
    Colors_Adjust_FullColors = 'CameraFilterPack_Colors_Adjust_FullColors'
    Colors_BleachBypass = 'CameraFilterPack_Colors_BleachBypass'
    Colors_Brightness = 'CameraFilterPack_Colors_Brightness'
    Colors_DarkColor = 'CameraFilterPack_Colors_DarkColor'
    Colors_HSV = 'CameraFilterPack_Colors_HSV'
    Colors_HUE_Rotate = 'CameraFilterPack_Colors_HUE_Rotate'
    Colors_NewPosterize = 'CameraFilterPack_Colors_NewPosterize'
    Colors_RgbClamp = 'CameraFilterPack_Colors_RgbClamp'
    Colors_Threshold = 'CameraFilterPack_Colors_Threshold'
    Color_BrightContrastSaturation = 'CameraFilterPack_Color_BrightContrastSaturation'
    Color_Chromatic_Aberration = 'CameraFilterPack_Color_Chromatic_Aberration'
    Color_Contrast = 'CameraFilterPack_Color_Contrast'
    Color_GrayScale = 'CameraFilterPack_Color_GrayScale'
    Color_Invert = 'CameraFilterPack_Color_Invert'
    Color_Noise = 'CameraFilterPack_Color_Noise'
    Color_RGB = 'CameraFilterPack_Color_RGB'
    Color_Sepia = 'CameraFilterPack_Color_Sepia'
    Color_Switching = 'CameraFilterPack_Color_Switching'
    Color_YUV = 'CameraFilterPack_Color_YUV'
    Distortion_Aspiration = 'CameraFilterPack_Distortion_Aspiration'
    Distortion_BigFace = 'CameraFilterPack_Distortion_BigFace'
    Distortion_BlackHole = 'CameraFilterPack_Distortion_BlackHole'
    Distortion_Dissipation = 'CameraFilterPack_Distortion_Dissipation'
    Distortion_Dream = 'CameraFilterPack_Distortion_Dream'
    Distortion_Dream2 = 'CameraFilterPack_Distortion_Dream2'
    Distortion_FishEye = 'CameraFilterPack_Distortion_FishEye'
    Distortion_Flag = 'CameraFilterPack_Distortion_Flag'
    Distortion_Flush = 'CameraFilterPack_Distortion_Flush'
    Distortion_Half_Sphere = 'CameraFilterPack_Distortion_Half_Sphere'
    Distortion_Heat = 'CameraFilterPack_Distortion_Heat'
    Distortion_Lens = 'CameraFilterPack_Distortion_Lens'
    Distortion_Noise = 'CameraFilterPack_Distortion_Noise'
    Distortion_ShockWave = 'CameraFilterPack_Distortion_ShockWave'
    Distortion_Twist = 'CameraFilterPack_Distortion_Twist'
    Distortion_Twist_Square = 'CameraFilterPack_Distortion_Twist_Square'
    Distortion_Water_Drop = 'CameraFilterPack_Distortion_Water_Drop'
    Distortion_Wave_Horizontal = 'CameraFilterPack_Distortion_Wave_Horizontal'
    Drawing_BluePrint = 'CameraFilterPack_Drawing_BluePrint'
    Drawing_CellShading = 'CameraFilterPack_Drawing_CellShading'
    Drawing_CellShading2 = 'CameraFilterPack_Drawing_CellShading2'
    Drawing_Comics = 'CameraFilterPack_Drawing_Comics'
    Drawing_Crosshatch = 'CameraFilterPack_Drawing_Crosshatch'
    Drawing_Curve = 'CameraFilterPack_Drawing_Curve'
    Drawing_EnhancedComics = 'CameraFilterPack_Drawing_EnhancedComics'
    Drawing_Halftone = 'CameraFilterPack_Drawing_Halftone'
    Drawing_Laplacian = 'CameraFilterPack_Drawing_Laplacian'
    Drawing_Lines = 'CameraFilterPack_Drawing_Lines'
    Drawing_Manga = 'CameraFilterPack_Drawing_Manga'
    Drawing_Manga2 = 'CameraFilterPack_Drawing_Manga2'
    Drawing_Manga3 = 'CameraFilterPack_Drawing_Manga3'
    Drawing_Manga4 = 'CameraFilterPack_Drawing_Manga4'
    Drawing_Manga5 = 'CameraFilterPack_Drawing_Manga5'
    Drawing_Manga_Color = 'CameraFilterPack_Drawing_Manga_Color'
    Drawing_Manga_Flash = 'CameraFilterPack_Drawing_Manga_Flash'
    Drawing_Manga_FlashWhite = 'CameraFilterPack_Drawing_Manga_FlashWhite'
    Drawing_Manga_Flash_Color = 'CameraFilterPack_Drawing_Manga_Flash_Color'
    Drawing_NewCellShading = 'CameraFilterPack_Drawing_NewCellShading'
    Drawing_Paper = 'CameraFilterPack_Drawing_Paper'
    Drawing_Paper2 = 'CameraFilterPack_Drawing_Paper2'
    Drawing_Paper3 = 'CameraFilterPack_Drawing_Paper3'
    Drawing_Toon = 'CameraFilterPack_Drawing_Toon'
    Edge_BlackLine = 'CameraFilterPack_Edge_BlackLine'
    Edge_Edge_filter = 'CameraFilterPack_Edge_Edge_filter'
    Edge_Golden = 'CameraFilterPack_Edge_Golden'
    Edge_Neon = 'CameraFilterPack_Edge_Neon'
    Edge_Sigmoid = 'CameraFilterPack_Edge_Sigmoid'
    Edge_Sobel = 'CameraFilterPack_Edge_Sobel'
    EXTRA_Rotation = 'CameraFilterPack_EXTRA_Rotation'
    EyesVision_1 = 'CameraFilterPack_EyesVision_1'
    EyesVision_2 = 'CameraFilterPack_EyesVision_2'
    Film_ColorPerfection = 'CameraFilterPack_Film_ColorPerfection'
    Film_Grain = 'CameraFilterPack_Film_Grain'
    FlipScreen = 'CameraFilterPack_FlipScreen'
    Fly_Vision = 'CameraFilterPack_Fly_Vision'
    FX_8bits = 'CameraFilterPack_FX_8bits'
    FX_8bits_gb = 'CameraFilterPack_FX_8bits_gb'
    FX_Ascii = 'CameraFilterPack_FX_Ascii'
    FX_DarkMatter = 'CameraFilterPack_FX_DarkMatter'
    FX_DigitalMatrix = 'CameraFilterPack_FX_DigitalMatrix'
    FX_DigitalMatrixDistortion = 'CameraFilterPack_FX_DigitalMatrixDistortion'
    FX_Dot_Circle = 'CameraFilterPack_FX_Dot_Circle'
    FX_Drunk = 'CameraFilterPack_FX_Drunk'
    FX_Drunk2 = 'CameraFilterPack_FX_Drunk2'
    FX_EarthQuake = 'CameraFilterPack_FX_EarthQuake'
    FX_Funk = 'CameraFilterPack_FX_Funk'
    FX_Glitch1 = 'CameraFilterPack_FX_Glitch1'
    FX_Glitch2 = 'CameraFilterPack_FX_Glitch2'
    FX_Glitch3 = 'CameraFilterPack_FX_Glitch3'
    FX_Grid = 'CameraFilterPack_FX_Grid'
    FX_Hexagon = 'CameraFilterPack_FX_Hexagon'
    FX_Hexagon_Black = 'CameraFilterPack_FX_Hexagon_Black'
    FX_Hypno = 'CameraFilterPack_FX_Hypno'
    FX_InverChromiLum = 'CameraFilterPack_FX_InverChromiLum'
    FX_Mirror = 'CameraFilterPack_FX_Mirror'
    FX_Plasma = 'CameraFilterPack_FX_Plasma'
    FX_Psycho = 'CameraFilterPack_FX_Psycho'
    FX_Scan = 'CameraFilterPack_FX_Scan'
    FX_Screens = 'CameraFilterPack_FX_Screens'
    FX_Spot = 'CameraFilterPack_FX_Spot'
    FX_superDot = 'CameraFilterPack_FX_superDot'
    FX_ZebraColor = 'CameraFilterPack_FX_ZebraColor'
    Glitch_Mozaic = 'CameraFilterPack_Glitch_Mozaic'
    Glow_Glow = 'CameraFilterPack_Glow_Glow'
    Glow_Glow_Color = 'CameraFilterPack_Glow_Glow_Color'
    Gradients_Ansi = 'CameraFilterPack_Gradients_Ansi'
    Gradients_Desert = 'CameraFilterPack_Gradients_Desert'
    Gradients_ElectricGradient = 'CameraFilterPack_Gradients_ElectricGradient'
    Gradients_FireGradient = 'CameraFilterPack_Gradients_FireGradient'
    Gradients_Hue = 'CameraFilterPack_Gradients_Hue'
    Gradients_NeonGradient = 'CameraFilterPack_Gradients_NeonGradient'
    Gradients_Rainbow = 'CameraFilterPack_Gradients_Rainbow'
    Gradients_Stripe = 'CameraFilterPack_Gradients_Stripe'
    Gradients_Tech = 'CameraFilterPack_Gradients_Tech'
    Gradients_Therma = 'CameraFilterPack_Gradients_Therma'
    Light_Rainbow = 'CameraFilterPack_Light_Rainbow'
    Light_Rainbow2 = 'CameraFilterPack_Light_Rainbow2'
    Light_Water = 'CameraFilterPack_Light_Water'
    Light_Water2 = 'CameraFilterPack_Light_Water2'
    NightVisionFX = 'CameraFilterPack_NightVisionFX'
    NightVision_4 = 'CameraFilterPack_NightVision_4'
    Noise_TV = 'CameraFilterPack_Noise_TV'
    Noise_TV_2 = 'CameraFilterPack_Noise_TV_2'
    Noise_TV_3 = 'CameraFilterPack_Noise_TV_3'
    Oculus_NightVision1 = 'CameraFilterPack_Oculus_NightVision1'
    Oculus_NightVision2 = 'CameraFilterPack_Oculus_NightVision2'
    Oculus_NightVision3 = 'CameraFilterPack_Oculus_NightVision3'
    Oculus_NightVision5 = 'CameraFilterPack_Oculus_NightVision5'
    Oculus_ThermaVision = 'CameraFilterPack_Oculus_ThermaVision'
    OldFilm_Cutting1 = 'CameraFilterPack_OldFilm_Cutting1'
    OldFilm_Cutting2 = 'CameraFilterPack_OldFilm_Cutting2'
    Pixelisation_Dot = 'CameraFilterPack_Pixelisation_Dot'
    Pixelisation_OilPaint = 'CameraFilterPack_Pixelisation_OilPaint'
    Pixelisation_OilPaintHQ = 'CameraFilterPack_Pixelisation_OilPaintHQ'
    Pixel_Pixelisation = 'CameraFilterPack_Pixel_Pixelisation'
    Real_VHS = 'CameraFilterPack_Real_VHS'
    Retro_Loading = 'CameraFilterPack_Retro_Loading'
    Sharpen_Sharpen = 'CameraFilterPack_Sharpen_Sharpen'
    Special_Bubble = 'CameraFilterPack_Special_Bubble'
    TV_50 = 'CameraFilterPack_TV_50'
    TV_80 = 'CameraFilterPack_TV_80'
    TV_ARCADE = 'CameraFilterPack_TV_ARCADE'
    TV_ARCADE_2 = 'CameraFilterPack_TV_ARCADE_2'
    TV_ARCADE_3 = 'CameraFilterPack_TV_ARCADE_3'
    TV_ARCADE_Fast = 'CameraFilterPack_TV_ARCADE_Fast'
    TV_Artefact = 'CameraFilterPack_TV_Artefact'
    TV_BrokenGlass = 'CameraFilterPack_TV_BrokenGlass'
    TV_BrokenGlass2 = 'CameraFilterPack_TV_BrokenGlass2'
    TV_Chromatical = 'CameraFilterPack_TV_Chromatical'
    TV_Chromatical2 = 'CameraFilterPack_TV_Chromatical2'
    TV_CompressionFX = 'CameraFilterPack_TV_CompressionFX'
    TV_Distorted = 'CameraFilterPack_TV_Distorted'
    TV_Horror = 'CameraFilterPack_TV_Horror'
    TV_LED = 'CameraFilterPack_TV_LED'
    TV_Noise = 'CameraFilterPack_TV_Noise'
    TV_Old = 'CameraFilterPack_TV_Old'
    TV_Old_Movie = 'CameraFilterPack_TV_Old_Movie'
    TV_Old_Movie_2 = 'CameraFilterPack_TV_Old_Movie_2'
    TV_PlanetMars = 'CameraFilterPack_TV_PlanetMars'
    TV_Posterize = 'CameraFilterPack_TV_Posterize'
    TV_Rgb = 'CameraFilterPack_TV_Rgb'
    TV_Tiles = 'CameraFilterPack_TV_Tiles'
    TV_Vcr = 'CameraFilterPack_TV_Vcr'
    TV_VHS = 'CameraFilterPack_TV_VHS'
    TV_VHS_Rewind = 'CameraFilterPack_TV_VHS_Rewind'
    TV_Video3D = 'CameraFilterPack_TV_Video3D'
    TV_Videoflip = 'CameraFilterPack_TV_Videoflip'
    TV_Vintage = 'CameraFilterPack_TV_Vintage'
    TV_WideScreenCircle = 'CameraFilterPack_TV_WideScreenCircle'
    TV_WideScreenHorizontal = 'CameraFilterPack_TV_WideScreenHorizontal'
    TV_WideScreenHV = 'CameraFilterPack_TV_WideScreenHV'
    TV_WideScreenVertical = 'CameraFilterPack_TV_WideScreenVertical'
    VHS_Tracking = 'CameraFilterPack_VHS_Tracking'
    Vision_Aura = 'CameraFilterPack_Vision_Aura'
    Vision_AuraDistortion = 'CameraFilterPack_Vision_AuraDistortion'
    Vision_Crystal = 'CameraFilterPack_Vision_Crystal'
    Vision_Drost = 'CameraFilterPack_Vision_Drost'
    Vision_Plasma = 'CameraFilterPack_Vision_Plasma'
    Vision_Psycho = 'CameraFilterPack_Vision_Psycho'
    Vision_Rainbow = 'CameraFilterPack_Vision_Rainbow'
    Vision_Tunnel = 'CameraFilterPack_Vision_Tunnel'
    Vision_Warp = 'CameraFilterPack_Vision_Warp'
    Vision_Warp2 = 'CameraFilterPack_Vision_Warp2'

class AdvancedFilterTartgetType(str, Enum):
    """高级滤镜目标类型"""
    
    Camera = 'Camera'
    """摄像头"""
    Decoration = 'Decoration'
    """装饰物"""

class RepeatType(str, Enum):
    """重复事件类型"""

    Beat = 'Beat'
    """节拍"""
    Floor = 'Floor'
    """方块"""

class HoldSound(str, Enum):
    """长按音效"""

    Fuse = 'Fuse'
    """引信"""
    SingSing = 'SingSing'
    """歌咏"""
    NONE = 'None'
    """无"""

class HoldMidSoundType(str, Enum):
    """长按中段音效类型"""

    Once = 'Once'
    """一次"""
    Repeat = 'Repeat'
    """重复"""

class HoldMidSoundTimingRelative(str, Enum):
    """长按中段音效延迟关联到"""

    Start = 'Start'
    """起点方块"""
    End = 'End'
    """终点方块"""

class MultiPlanets(str, Enum):
    """多行星"""

    TwoPlanets = 'TwoPlanets'
    """双星"""
    ThreePlanets = 'ThreePlanets'
    """三星"""

class BlendMode(str, Enum):
    """混合模式"""

    NONE = 'None'
    """无"""
    Screen = 'Screen'
    """滤色模式"""
    LinearDodge = 'LinearDodge'
    """线性减淡"""
    Overlay = 'Overlay'
    """叠加模式"""
    SoftLight = 'SoftLight'
    """柔光模式"""
    Difference = 'Difference'
    """差值模式"""
    Multiply = 'Multiply'
    """正片叠底"""

class Hitbox(str, Enum):
    """判定框"""

    NONE = 'None'
    """禁用"""
    Kill = 'Kill'
    """失败玩家"""
    Event = 'Event'
    """运行事件"""

class HitboxTarget(str, Enum):
    """判定框检查目标"""

    Planet = 'Planet'
    """行星"""
    Decoration = 'Decoration'
    """装饰"""

class HitboxTriggerType(str, Enum):
    """判定框触发类型"""

    Once = 'Once'
    """单次"""
    PerTouch = 'PerTouch'
    """每次接触"""
    Repeat = 'Repeat'
    """重复"""

class HitboxType(str, Enum):
    """判定框形状"""

    Box = 'Box'
    """盒形"""
    Circle = 'Circle'
    """环形"""
    Capsule = 'Capsule'
    """胶囊形"""

class Font(str, Enum):
    """字体"""

    Default = 'Default'
    """默认"""
    Arial = 'Arial'
    """Arial"""
    ComicSansMS = 'ComicSansMS'
    """Comic Sans MS"""
    CourierNew = 'CourierNew'
    """Courier New"""
    Georgia = 'Georgia'
    """Georgia"""
    Impact = 'Impact'
    """Impact"""
    TimesNewRoman = 'TimesNewRoman'
    """Times New Roman"""

class ObjectType(str, Enum):
    """对象类型"""

    Floor = 'Floor'
    """地板"""
    Planet = 'Planet'
    """星球"""

class PlanetColorType(str, Enum):
    """星球颜色类型"""

    DefaultRed = 'DefaultRed'
    """默认红色"""
    DefaultBlue = 'DefaultBlue'
    """默认蓝色"""
    Gold = 'Gold'
    """金色"""
    Overseer = 'Overseer'
    """监督者"""
    Custom = 'Custom'
    """自定义"""

class TrackType(str, Enum):
    """轨道样式"""

    Normal = 'Normal'
    """标准"""
    Midspin = 'Midspin'
    """中旋"""

class ParticleSimulationSpace(str, Enum):
    """粒子模拟空间"""

    Local = 'Local'
    """本地"""
    World = 'World'
    """全局"""

class InputEventTarget(str, Enum):
    Any = 'Any'
    """任意"""
    Any1 = 'Any1'
    """键盘左侧"""
    Any2 = 'Any2'
    """键盘右侧"""
    Up = 'Up'
    """上键（↑）"""
    Down = 'Down'
    """下键（↓）"""
    Left = 'Left'
    """左键（←）"""
    Right = 'Right'
    """右键（→）"""

class InputEventState(str, Enum):
    Down = 'Down'
    """按键按下时"""
    Up = 'Up'
    """按键松开时"""
