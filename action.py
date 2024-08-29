from .enums import *

class ACTION:

    @classmethod
    def load(cls, floor: int | None = None, eventType: str | EventTypes | None = None, **kwargs):
        """
        将字典型转化为Action型

        :param floor: 必须的参数floor，若未传入则应当在kwargs中声明
        :param eventType: 必须的参数eventType，若未传入则应当在kwargs中声明
        :param kwargs: 事件的其他参数，若未传入则按该事件的默认参数处理

        :return: 对应事件类型的Action类
        """
        if floor is None:
            floor = kwargs.get('floor')
        if eventType is None:
            eventType = kwargs.get('eventType')
        
        if floor is None:
            raise ValueError('param "floor" must be provided as an argument or in kwargs')
        if eventType is None:
            raise ValueError('param "eventType" must be provided as an argument or in kwargs')
        
        kwargs['floor'] = floor
        kwargs['eventType'] = eventType

        eventType = value_to_subenum(eventTypes, kwargs['eventType'])
        match eventType:
            case eventTypes.Gameplay.SetSpeed:
                return cls.SetSpeed(**kwargs)
            case eventTypes.Gameplay.Twirl:
                return cls.Twirl(**kwargs)
            case eventTypes.Gameplay.Checkpoint:
                return cls.Checkpoint(**kwargs)
            case eventTypes.Gameplay.SetHitsound:
                return cls.SetHitsound(**kwargs)
            case eventTypes.Gameplay.PlaySound:
                return cls.PlaySound(**kwargs)
            case eventTypes.Gameplay.SetPlanetRotation:
                return cls.SetPlanetRotation(**kwargs)
            case eventTypes.Gameplay.Pause:
                return cls.Pause(**kwargs)
            case eventTypes.Gameplay.AutoPlayTiles:
                return cls.AutoPlayTiles(**kwargs)
            case eventTypes.Gameplay.ScalePlanets:
                return cls.ScalePlanets(**kwargs)
            case eventTypes.TrackEvents.ColorTrack:
                return cls.ColorTrack(**kwargs)
            case eventTypes.TrackEvents.AnimateTrack:
                return cls.AnimateTrack(**kwargs)
            case eventTypes.TrackEvents.RecolorTrack:
                return cls.RecolorTrack(**kwargs)
            case eventTypes.TrackEvents.MoveTrack:
                return cls.MoveTrack(**kwargs)
            case eventTypes.TrackEvents.PositionTrack:
                return cls.PositionTrack(**kwargs)
            case eventTypes.DecorationEvents.MoveDecorations:
                return cls.MoveDecorations(**kwargs)
            case eventTypes.DecorationEvents.SetText:
                return cls.SetText(**kwargs)
            case eventTypes.DecorationEvents.EmitParticle:
                return cls.EmitParticle(**kwargs)
            case eventTypes.DecorationEvents.SetParticle:
                return cls.SetParticle(**kwargs)
            case eventTypes.DecorationEvents.SetObject:
                return cls.SetObject(**kwargs)
            case eventTypes.DecorationEvents.SetDefaultText:
                return cls.SetDefaultText(**kwargs)
            case eventTypes.VisualEffects.CustomBackground:
                return cls.CustomBackground(**kwargs)
            case eventTypes.VisualEffects.Flash:
                return cls.Flash(**kwargs)
            case eventTypes.VisualEffects.MoveCamera:
                return cls.MoveCamera(**kwargs)
            case eventTypes.VisualEffects.SetFilter:
                return cls.SetFilter(**kwargs)
            case eventTypes.VisualEffects.SetFilterAdvanced:
                return cls.SetFilterAdvanced(**kwargs)
            case eventTypes.VisualEffects.HallOfMirrors:
                return cls.HallOfMirrors(**kwargs)
            case eventTypes.VisualEffects.ShakeScreen:
                return cls.ShakeScreen(**kwargs)
            case eventTypes.VisualEffects.Bloom:
                return cls.Bloom(**kwargs)
            case eventTypes.VisualEffects.ScreenTile:
                return cls.ScreenTile(**kwargs)
            case eventTypes.VisualEffects.ScreenScroll:
                return cls.ScreenScroll(**kwargs)
            case eventTypes.VisualEffects.SetFrameRate:
                return cls.SetFrameRate(**kwargs)
            case eventTypes.Modifiers.RepeatEvents:
                return cls.RepeatEvents(**kwargs)
            case eventTypes.Modifiers.SetConditionalEvents:
                return cls.SetConditionalEvents(**kwargs)
            case eventTypes.Conveniences.EditorComment:
                return cls.EditorComment(**kwargs)
            case eventTypes.Conveniences.Bookmark:
                return cls.Bookmark(**kwargs)
            case eventTypes.DLC.Hold:
                return cls.Hold(**kwargs)
            case eventTypes.DLC.SetHoldSound:
                return cls.SetHoldSound(**kwargs)
            case eventTypes.DLC.MultiPlanet:
                return cls.MultiPlanet(**kwargs)
            case eventTypes.DLC.FreeRoam:
                return cls.FreeRoam(**kwargs)
            case eventTypes.DLC.FreeRoamTwirl:
                return cls.FreeRoamTwirl(**kwargs)
            case eventTypes.DLC.FreeRoamRemove:
                return cls.FreeRoamRemove(**kwargs)
            case eventTypes.DLC.Hide:
                return cls.Hide(**kwargs)
            case eventTypes.DLC.ScaleMargin:
                return cls.ScaleMargin(**kwargs)
            case eventTypes.DLC.ScaleRadius:
                return cls.ScaleRadius(**kwargs)
            case _:
                raise ValueError(f'The eventType {eventType.name} is not an Action')

    @get_value
    class SetSpeed:
        """设置速度"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.Gameplay.SetSpeed
            """事件类型"""
            self.speedType: SpeedType = value_to_enum(SpeedType, kwargs.get('speedType', SpeedType.Bpm))
            """速度类型"""
            self.beatsPerMinute : float | int = kwargs.get('beatsPerMinute', 100)
            """BPM"""
            self.bpmMultiplier : float | int = kwargs.get('bpmMultiplier', 1)
            """倍频"""
            self.angleOffset : float | int = kwargs.get('angleOffset', 0)
            """角度偏移"""

    @get_value
    class Twirl:
        """旋转"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.Gameplay.Twirl
            """事件类型"""

    @get_value
    class Checkpoint:
        """检查点"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.Gameplay.Checkpoint
            """事件类型"""
            self.tileOffset : int = kwargs.get('tileOffset', 0)
            """重置方块偏移"""

    @get_value
    class SetHitsound:
        """设置打拍音"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.Gameplay.SetHitsound
            """事件类型"""
            self.gameSound : GameSound = value_to_enum(GameSound, kwargs.get('gameSound', GameSound.Hitsound))
            """打拍音设置目标"""
            self.hitsound : HITSOUND = value_to_enum(HITSOUND, kwargs.get('hitsound', HITSOUND.Kick))
            """打拍声"""
            self.hitsoundVolume : int = kwargs.get('hitsoundVolume', 100)
            """打拍声音量"""

    @get_value
    class PlaySound:
        """设置音效"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.Gameplay.PlaySound
            """事件类型"""
            self.hitsound : HITSOUND = value_to_enum(HITSOUND, kwargs.get('hitsound', HITSOUND.Kick))
            """打拍声"""
            self.hitsoundVolume : int = kwargs.get('hitsoundVolume', 100)
            """打拍声音量"""
            self.angleOffset : float | int = kwargs.get('angleOffset', 0)
            """角度偏移"""
            self.eventTag : str = kwargs.get('eventTag', '')
            """事件标签"""

    @get_value
    class SetPlanetRotation:
        """设置星球轨迹"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.Gameplay.SetPlanetRotation
            """事件类型"""
            self.ease : EASE = value_to_enum(EASE, kwargs.get('ease', EASE.Linear))
            """缓速"""
            self.easeParts : int = kwargs.get('waseParts', 1)
            """缓速部分"""
            self.easePartBehavior : EASE_PART_BEHAVIOR = value_to_enum(EASE_PART_BEHAVIOR, kwargs.get('easePartBehavior', EASE_PART_BEHAVIOR.Mirror))
            """缓速部分行为"""

    @get_value
    class Pause:
        """暂停节拍"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.Gameplay.Pause
            """事件类型"""
            self.duration : float | int = kwargs.get('duration', 1)
            """暂停时长（拍）"""
            self.coundownTicks : int = kwargs.get('countdownTicks', 0)
            """计数滴答"""
            self.angleCorrectionDir : int = kwargs.get('angleCorrectionDir', -1)
            """角度校正（-1, 0, 1）"""

    @get_value
    class AutoPlayTiles:
        """自动播放格子"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.Gameplay.AutoPlayTiles
            """事件类型"""
            self.enabled : bool = boolean(kwargs.get('enabled', True))
            """设置为"""
            self.showStatusText : bool = boolean(kwargs.get('showStatusText', True))
            """显示“自动方块”文本"""
            self.safetyTiles : bool = boolean(kwargs.get('safetyTiles', False))
            """保险方块 [关卡编辑器中不可直接编辑]"""

    @get_value
    class ScalePlanets:
        """缩放行星"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.Gameplay.ScalePlanets
            """事件类型"""
            self.duration : float | int = kwargs.get('duration')
            """时长"""
            self.targetPlanet : Planet = value_to_enum(Planet, kwargs.get('targetPlanet', Planet.All))
            """目标星球"""
            self.scale : float | int = kwargs.get('scale', 100)
            """星球大小"""
            self.angleOffset : float | int = kwargs.get('angleOffset', 0)
            """角度偏移"""
            self.ease : EASE = value_to_enum(EASE, kwargs.get('ease', EASE.Linear))
            """缓速"""
            self.eventTag : str = kwargs.get('eventTag', '')
            """事件标签"""

    @get_value
    class ColorTrack:
        """设置轨道颜色"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.TrackEvents.ColorTrack
            """事件类型"""
            self.trackColorType : TRACK_COLOR_TYPE = value_to_enum(TRACK_COLOR_TYPE, kwargs.get('trackColorType', TRACK_COLOR_TYPE.Single))
            """轨道颜色类型"""
            self.trackColor : Color = Color(kwargs.get('trackColor', 'debb7b'))
            """轨道主色调"""
            self.secondaryTrackColor : Color = Color(kwargs.get('secondaryTrackColor' , 'ffffff'))
            """轨道副色调"""
            self.trackColorAnimDuration : float | int = kwargs.get('trackColorAnimDuration', 2)
            """色彩动画间隔"""
            self.trackColorPulse : TRACK_COLOR_PULSE = value_to_enum(TRACK_COLOR_PULSE, kwargs.get('trackColorPulse', TRACK_COLOR_PULSE.NONE))
            """颜色脉冲类型"""
            self.trackPulseLength : int = kwargs.get('trackPulseLength', 10)
            """颜色脉冲长度"""
            self.trackStyle : TRACK_STYLE = value_to_enum(TRACK_STYLE, kwargs.get('trackStyle', TRACK_STYLE.Standard))
            """轨道风格"""
            self.trackTexture : str = kwargs.get('trackTexture', '')
            """轨道贴图（相对文件路径）"""
            self.trackTextureScale : float | int = kwargs.get('trackTextureScale', 1)
            """轨道贴图大小"""
            self.trackGlowIntensity : float | int = kwargs.get('trackGlowIntensity', 100)
            """轨道辉度"""
            if 'floorIconOutlines' in kwargs:
                self.floorIconOutlines : bool = boolean(kwargs.get('floorIconOUtlines', False))
                """方块图标描边 [可隐藏]"""
            self.justThisTile : bool = boolean(kwargs.get('justThisTile', False))
            """仅改变此方块"""

    @get_value
    class AnimateTrack:
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.TrackEvents.AnimateTrack
            """事件类型"""
            if 'trackAnimation' in kwargs:
                self.trackAnimation : TRACK_ANIMATION = value_to_enum(TRACK_ANIMATION, kwargs.get('trackAnimation', TRACK_ANIMATION.NONE))
                """轨道出现动画 [可隐藏]"""
            self.beatsAhead : float | int = kwargs.get('beatsAhead', 3)
            """轨道出现动画提前节拍数"""
            if 'trackDisapperAnimation' in kwargs:
                self.trackDisappearAnimation : TRACK_DISAPPEAR_ANIMATION = value_to_enum(TRACK_DISAPPEAR_ANIMATION, kwargs.get('trackDisappearAnimation', TRACK_DISAPPEAR_ANIMATION.NONE))
                """轨道消失动画 [可隐藏]"""
            self.beatsBehind : float | int = kwargs.get('beatsBehind', 4)
            """轨道消失动画延后节拍数"""

    @get_value
    class RecolorTrack:
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.TrackEvents.RecolorTrack
            """事件类型"""
            self.startTile : Data_Pair.TilePosition = Data_Pair.TilePosition.from_int_str(kwargs.get('startTile', (0, 'Start')))
            """效果起始方块"""
            self.endTile : Data_Pair.TilePosition = Data_Pair.TilePosition.from_int_str(kwargs.get('endTile', (0, 'End')))
            """效果结束方块"""
            self.gapLength : int = kwargs.get('gapLength', 0)
            """间隙长度"""
            self.duration : float | int = kwargs.get('duration', 0)
            """时长"""
            self.trackColorType : TRACK_COLOR_TYPE = value_to_enum(TRACK_COLOR_TYPE, kwargs.get('trackColorType', TRACK_COLOR_TYPE.Single))
            """轨道颜色类型"""
            self.trackColor : Color = Color(kwargs.get('trackColor', 'debb7b'))
            """轨道主色调"""
            self.secondaryTrackColor : Color = Color(kwargs.get('secondaryTrackColor' , 'ffffff'))
            """轨道副色调"""
            self.trackColorAnimDuration : float | int = kwargs.get('trackColorAnimDuration', 2)
            """色彩动画间隔"""
            self.trackColorPulse : TRACK_COLOR_PULSE = value_to_enum(TRACK_COLOR_PULSE, kwargs.get('trackColorPulse', TRACK_COLOR_PULSE.NONE))
            """颜色脉冲类型"""
            self.trackPulseLength : int = kwargs.get('trackPulseLength', 10)
            """颜色脉冲长度"""
            self.trackStyle : TRACK_STYLE = value_to_enum(TRACK_STYLE, kwargs.get('trackStyle', TRACK_STYLE.Standard))
            """轨道风格"""
            self.trackGlowIntensity : float | int = kwargs.get('trackGlowIntensity', 100)
            """轨道辉度"""
            self.angleOffset : float | int = kwargs.get('angleOffset', 0)
            """角度偏移"""
            self.ease : EASE = value_to_enum(EASE, kwargs.get('ease', EASE.Linear))
            """缓速"""
            self.eventTag : str = kwargs.get('eventTag', '')

    @get_value
    class MoveTrack:
        """移动轨道"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.TrackEvents.MoveTrack
            """事件类型"""
            self.startTile : Data_Pair.TilePosition = Data_Pair.TilePosition.from_int_str(kwargs.get('startTile', (0, 'ThisTile')))
            """效果起始方块"""
            self.endTile : Data_Pair.TilePosition = Data_Pair.TilePosition.from_int_str(kwargs.get('endTile', (0, 'ThisTile')))
            """效果结束方块"""
            self.gapLength : int = kwargs.get('gapLength', 0)
            """间隙长度"""
            self.duration : float | int = kwargs.get('duration', 1)
            """时长"""
            if 'positionOffset' in kwargs:
                self.positionOffset : Data_Pair.XY_NonePair = Data_Pair.XY_NonePair.from_tuple(kwargs.get('positionOffset', (None, None)))
                """位置偏移"""
            if 'rotationOffset' in kwargs:
                self.rotationOffset : float | int = kwargs.get('rotationOffset', 0)
                """旋转偏移"""
            if 'scale' in kwargs:
                self.scale : Data_Pair.XY_NonePair = Data_Pair.XY_NonePair.from_tuple(kwargs.get('scale', (None, None)))
                """缩放"""
            if 'opacity' in kwargs:
                self.opacity : float | int = kwargs.get('opacity', 100)
                """透明度"""
            self.angleOffset : float | int = kwargs.get('angleOffset', 0)
            """角度偏移"""
            self.ease : EASE = value_to_enum(EASE, kwargs.get('ease', EASE.Linear))
            """缓速"""
            self.maxVfxOnly : bool = boolean(kwargs.get('maxVfxOnly', False))
            """仅在视觉效果全开时启用 [关卡编辑器中不可直接编辑]"""
            self.eventTag : str = kwargs.get('eventTag', '')
            """事件标签"""

    @get_value
    class PositionTrack:
        """位置轨道"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.TrackEvents.PositionTrack
            """事件类型"""
            if 'positionOffset' in kwargs:
                self.positionOffset : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('positionOffset', (0, 0)))
                """位置偏移"""
            self.relativeTo : Data_Pair.TilePosition = Data_Pair.TilePosition.from_int_str(kwargs.get('relativeTo', [0, 'ThisTile']))
            """相对于"""
            if 'rotation' in kwargs:
                self.rotation : float | int = kwargs.get('rotation', 0)
                """旋转"""
            if 'scale' in kwargs:
                self.scale : float | int = kwargs.get('scale', 100)
                """大小"""
            if 'opacity' in kwargs:
                self.opacity : float | int = kwargs.get('opacity', 100)
                """透明度"""
            self.justThisTile : bool = boolean(kwargs.get('justThisTile', False))
            """仅改变此方块"""
            self.editorOnly : bool = boolean(kwargs.get('editorOnly', False))
            """仅限编辑器"""
            if 'stickToFloors' in kwargs:
                self.stickToFloors : bool = boolean(kwargs.get('stickToFloors', True))
                """黏性方块"""
        
    @get_value
    class MoveDecorations:
        """移动装饰"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.DecorationEvents.MoveDecorations
            """事件类型"""
            self.duration : float | int = kwargs.get('duration', 1)
            """时长"""
            self.tag : str = kwargs.get('tag', 'sampleTag')
            """目标装饰物标签"""
            if 'visible' in kwargs:
                self.visible : bool = boolean(kwargs.get('visible', True))
                """可见"""
            if 'relativeTo' in kwargs:
                self.relativeTo : DecorationRelative = value_to_enum(DecorationRelative, kwargs.get('relativeTo', DecorationRelative.Global))
                """相对于"""
            if 'decorationImage' in kwargs:
                self.decorationImage : str = kwargs.get('decorationImage', '')
                """图片（相对文件路径）"""
            if 'positionOffset' in kwargs:
                self.positionOffset : Data_Pair.XY_NonePair = Data_Pair.XY_NonePair.from_tuple(kwargs.get('positionOffset', (None, None)))
                """位置偏移"""
            if 'pivotOffset' in kwargs:
                self.pivotOffset : Data_Pair.XY_NonePair = Data_Pair.XY_NonePair.from_tuple(kwargs.get('pivotOffset', (None, None)))
                """轴心偏移"""
            if 'rotationOffset' in kwargs:
                self.rotationOffset : float | int = kwargs.get('rotationOffset', 0)
                """旋转偏移"""
            if 'scale' in kwargs:
                self.scale : Data_Pair.XY_NonePair = Data_Pair.XY_NonePair.from_tuple(kwargs.get('scale', (None, None)))
                """大小"""
            if 'color' in kwargs:
                self.color : str = kwargs.get('color', 'ffffff')
                """颜色"""
            if 'opacity' in kwargs:
                self.opacity : float | int = kwargs.get('opacity', 100)
                """透明度"""
            if 'depth' in kwargs:
                self.depth : int = kwargs.get('depth', -1)
                """深度"""
            if 'parallax' in kwargs:
                self.parallax : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('parallax', [0, 0]))
                """平行"""
            if 'parallaxOffset' in kwargs:
                self.parallaxOffset : Data_Pair.XY_NonePair = Data_Pair.XY_NonePair.from_tuple(kwargs.get('parallaxOffset', [None, None]))
                """视差偏移"""
            self.angleOffset : float | int = kwargs.get('angleOffset', 0)
            """角度偏移"""
            self.ease : EASE = value_to_enum(EASE, kwargs.get('ease', EASE.Linear))
            """缓速"""
            self.eventTag : str = kwargs.get('eventTag', '')
            """事件标签"""
            if 'maskingType' in kwargs:
                self.maskingType : MaskType = value_to_enum(MaskType, kwargs.get('maskingType', MaskType.NONE))
                """遮罩类型"""
            if 'useMaskingDepth' in kwargs:
                self.useMaskingDepth : bool = boolean(kwargs.get('useMaskingDepth', False))
                """使用遮罩深度"""
            if 'maskingFrontDepth' in kwargs:
                self.maskingFrontDepth : int = kwargs.get('maskingFrontDepth', -1)
                """遮罩起始深度"""
            if 'maskingBackDepth' in kwargs:
                self.maskingBackDepth : int = kwargs.get('maskingBackDepth', False)
                """遮罩结束深度"""

    @get_value
    class SetText:
        """设置文本"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.DecorationEvents.SetText
            """事件类型"""
            self.decText : str = kwargs.get('decText', '文本')
            """文本"""
            self.tag : str = kwargs.get('tag', '')
            """标签"""
            self.angleOffset : float | int = kwargs.get('angleOffset', 0)
            """角度偏移"""
            self.eventTag : str = kwargs.get('eventTag', '')
            """事件标签"""

    @get_value
    class EmitParticle:
        """发射粒子"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.DecorationEvents.EmitParticle
            """事件类型"""
            self.tag : str = kwargs.get('tag', 'sampleTag')
            """标签"""
            self.count : int = kwargs.get('count', 10)
            """数量"""
            self.eventTag : str = kwargs.get('eventTag', '')
            """事件标签"""
            self.angleOffset : float | int = kwargs.get('angleOffset', 0)
            """角度偏移"""

    @get_value
    class SetParticle:
        """设置粒子"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.DecorationEvents.SetParticle
            """事件类型"""
            self.duration : float | int = kwargs.get('duration', 1)
            """时长"""
            self.tag : str = kwargs.get('tag', 'sampleTag')
            """标签"""
            if 'targetMode' in kwargs:
                self.targetMode : ParticleMode = value_to_enum(ParticleMode, kwargs.get('targetMode', ParticleMode.Start))
                """模式"""
            self.eventTag : str = kwargs.get('eventTag', '')
            """事件标签"""
            if 'particleLifetime' in kwargs:
                self.particleLifetime : Data_Pair.Increasing_Range_Pair = Data_Pair.Increasing_Range_Pair.from_tuple(kwargs.get('particleLifetime', [10, 10]))
                """粒子持续时间"""
            if 'emissionRate' in kwargs:
                self.emissionRate : int = kwargs.get('emissionRate', 10)
                """发送频率"""
            if 'simulationSpeed' in kwargs:
                self.simulationSpeed : float | int = kwargs.get('simulationSpeed', 100)
                """模拟速度"""
            self.angleOffset : float | int = kwargs.get('angleOffset', 0)
            if 'lockRotation' in kwargs:
                self.lockRotation : bool = boolean('lockRotation', False)
                """锁定转角"""
            if 'lockScale' in kwargs:
                self.lockScale : bool = boolean('lockScale', False)
                """锁定大小"""
            self.ease : EASE = value_to_enum(EASE, kwargs.get('ease', EASE.Linear))


            if 'color' in kwargs:
                self.color : ParticleColor = ParticleColor(**kwargs.get('color', {"color1": "ffffff", "mode": "Color"}))
                """颜色"""
            if 'maxParticles' in kwargs:
                self.maxParticles : int = kwargs.get('maxParticles', 1000)
                """最大粒子数"""
            if 'particleSize' in kwargs:
                self.particleSize : Data_Pair.Increasing_Range_Pair = Data_Pair.Increasing_Range_Pair.from_tuple(kwargs.get('particleSize', (100, 100)))
                """粒子大小"""
            if 'shapeType' in kwargs:
                self.shapeType : ParticleShapeType = value_to_enum(ParticleShapeType, kwargs.get('shapeType'))
                """粒子发射形状"""
                if self.shapeType == ParticleShapeType.Circle:
                    if 'shapeRadius' in kwargs:
                        self.shapeRadius : float | int = kwargs.get('shapeRadius', 1)
                        """半径"""
                    if 'arc' in kwargs:
                        self.arc : float | int = kwargs.get('arc', 360)
                        """弧"""
                    if 'arcMode' in kwargs:
                        self.arcMode : ParticleArcMode = value_to_enum(ParticleArcMode, kwargs.get('arcMode', ParticleArcMode.Random))
                        """弧模式"""
            else:
                if 'shapeRadius' in kwargs:
                    self.shapeRadius : float | int = kwargs.get('shapeRadius', 1)
                    """半径"""
                if 'arc' in kwargs:
                    self.arc : float | int = kwargs.get('arc', 360)
                    """弧"""
                if 'arcMode' in kwargs:
                    self.arcMode : ParticleArcMode = value_to_enum(ParticleArcMode, kwargs.get('arcMode', ParticleArcMode.Random))
                    """弧模式"""
            
            if 'velocityLimitOverLifetime' in kwargs:
                self.velocityLimitOverLifetime : Data_Pair.Range_Pair = Data_Pair.Range_Pair.from_tuple(kwargs.get('velocityLimitOverLifetime', (0, 0)))
                """生命周期限速"""
            if 'colorOverLifetime' in kwargs:
                self.colorOverLifetime : ParticleColor = ParticleColor(**kwargs['colorOverLifetime'])
                """随时间变色"""
            if 'sizeOverLifetime' in kwargs:
                self.sizeOverLifetime : Data_Pair.Range_Pair = Data_Pair.Range_Pair.from_tuple(kwargs.get('sizeOverLifetime', (100, 100)))
                """随时间缩放"""
            if 'velocity' in kwargs:
                self.velocity : Data_Pair.Increasing_XY_Pair = Data_Pair.Increasing_Range_Pair.from_tuple(kwargs.get('velocity', ((0, 0), (0, 0))))
                """随时间变速"""
            if 'rotationOverTime' in kwargs:
                self.rotationOverTime : Data_Pair.Increasing_Range_Pair = Data_Pair.Increasing_Range_Pair.from_tuple(kwargs.get('rotationOverTime', (0, 0)))
                """随时间旋转"""

    @get_value
    class SetObject:
        """设置对象"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.DecorationEvents.SetObject
            """事件类型"""
            self.duration : int = kwargs.get('duration', 1)
            """时长"""
            self.tag : str = kwargs.get('tag', 'sampleTag')
            """标签"""
            if 'planetColor' in kwargs:
                self.planetColor : Color = Color(kwargs.get('planetColor', 'ff0000'))
                """星球颜色"""
            if 'planetTailColor' in kwargs:
                self.planetTailColor : Color = Color(kwargs.get('planetTailColor', 'ff0000'))
                """星球轨迹颜色"""
            if 'trackAngle' in kwargs:
                self.trackAngle : float | int = kwargs.get('trackAngle', 180)
                """轨道角度"""
            if 'trackColorType' in kwargs:
                self.trackColorType : TRACK_COLOR_TYPE = value_to_enum(TRACK_COLOR_TYPE, kwargs.get('trackColorType', TRACK_COLOR_TYPE.Single))
                """轨道颜色类型"""
            if 'trackColor' in kwargs:
                self.trackColor : Color = Color(kwargs.get('trackColor', 'debb7b'))
                """轨道主色调"""
            if 'secondaryTrackColor' in kwargs:
                self.secondaryTrackColor : Color = Color(kwargs.get('secondaryTrackColor', 'ffffff'))
                """轨道副色调"""
            if 'trackColorAnimDuration' in kwargs:
                self.trackColorAnimDuration : float | int = kwargs.get('trackColorAnimDuration', 2)
                """色彩动画间隔"""
            if 'trackOpacity' in kwargs:
                self.trackOpacity : float | int = kwargs.get('trackOpacity', 100)
                """透明度"""
            if 'trackStyle' in kwargs:
                self.trackStyle : TRACK_STYLE = value_to_enum(TRACK_STYLE, kwargs.get('trackStyle', TRACK_STYLE.Standard))
                """轨道风格"""
            if 'trackIcon' in kwargs:
                self.trackIcon : TrackIcon = value_to_enum(TrackIcon, kwargs.get('trackIcon', TrackIcon.NONE))
                """轨道图标"""
            if 'trackIconAngle' in kwargs:
                self.trackIconAngle : float | int = kwargs.get('trackIconAngle', 0)
                """轨道图标角度"""
            if 'trackIconFlipped' in kwargs:
                self.trackIconFlipped : bool = boolean(kwargs.get('trackIconFlipped', False))
                """轨道图标翻转"""
            if 'trackRedSwirl' in kwargs:
                self.trackRedSwirl : bool = boolean(kwargs.get('trackRedSwirl', False))
                """红色漩涡"""
            if 'trackGraySetSpeedIcon' in kwargs:
                self.trackGraySetSpeedIcon : bool = boolean(kwargs.get('trackGraySetSpeedIcon', False))
                """灰色设置速度图标"""
            if 'trackGlowEnabled' in kwargs:
                self.trackGlowEnabled : bool = boolean(kwargs.get('trackGlowEnabled', False))
                """允许轨道发光"""
            if 'trackGlowColor' in kwargs:
                self.trackGlowColor : Color = Color(kwargs.get('trackGlowColor', 'ffffff'))
                """轨道发光颜色"""
            if 'trackIconOutlines' in kwargs:
                self.trackIconOutlines : bool = boolean(kwargs.get('trackIconOutlines', False))
                """方块图标描边"""
            self.angleOffset : float | int = kwargs.get('angleOffset', 0)
            """角度偏移"""
            self.ease : EASE = value_to_enum(EASE, kwargs.get('ease', EASE.Linear))
            """缓速"""
            self.eventTag : str = kwargs.get('eventTag', '')
            """事件标签"""

    @get_value
    class SetDefaultText:
        """设置默认文本"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.DecorationEvents.SetDefaultText
            """事件类型"""
            self.duration : float | int = kwargs.get('duration', 1)
            """时长"""
            self.angleOffset : float | int = kwargs.get('angleOffset', 0)
            """角度偏移"""
            self.ease : EASE = value_to_enum(EASE, kwargs.get('ease', EASE.Linear))
            """缓速"""
            if 'defaultTextColor' in kwargs:
                self.defaultTextColor : Color = Color(kwargs.get('defaultTextColor', 'ffffff'))
                """默认文本颜色"""
            if 'defaultTextShadowColor' in kwargs:
                self.defaultTextShadowColor : Color = Color(kwargs.get('defaultTextShadowColor', '00000050'))
                """默认文本阴影颜色"""
            if 'levelTitlePosition' in kwargs:
                self.levelTitlePosition : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('levelTitlePosition', (0, 0)))
                """关卡标题位置"""
            if 'levelTitleText' in kwargs:
                self.levelTitleText : str = kwargs.get('levelTitleText', '')
                """关卡标题文本"""
            if 'congratsText' in kwargs:
                self.congratsText : str = kwargs.get('congratsText', '恭喜！')
                """“庆贺！”文本"""
            if 'perfectText' in kwargs:
                self.perfectText : str = kwargs.get('perfectText', '完美无瑕！')
                """“完美无瑕！”文本"""
            self.eventTag : str = kwargs.get('eventTag', '')
            """事件标签"""

    @get_value
    class CustomBackground:
        """设置背景"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.VisualEffects.CustomBackground
            """事件类型"""
            self.color : str = kwargs.get('color', '000000')
            """颜色"""
            self.bgImage : str = kwargs.get('bgImage', '')
            """背景图片（相对文件路径）"""
            self.imageColor : Color = Color(kwargs.get('imageColor', 'ffffff'))
            """图片颜色"""
            self.parallax : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('parallax', (100, 100)))
            """平行"""
            self.bgDisplayMode : BG_DISPLAY_MODE = value_to_enum(BG_DISPLAY_MODE, kwargs.get('bgDisplayMode', BG_DISPLAY_MODE.FitToScreen))
            """背景图片显示模式"""
            self.imageSmoothing : bool = boolean(kwargs.get('imageSmoothing', True))
            """图片平滑"""
            self.lockRot : bool = boolean(kwargs.get('lockRot', False))
            """旋转锁定"""
            self.loopBG : bool = boolean(kwargs.get('loopBG', False))
            """循环背景"""
            self.scalingRatio : int = kwargs.get('scalingRatio', 100)
            """缩放比例"""
            self.angleOffset : float | int = kwargs.get('angleOffset', 0)
            """角度偏移"""
            self.eventTag : str = kwargs.get('eventTag', '')
            """事件标签"""

    @get_value
    class Flash:
        """闪光"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.VisualEffects.Flash
            """事件类型"""
            self.duration : float | int = kwargs.get('duration', 1)
            """时长"""
            self.plane : Plane = value_to_enum(Plane, kwargs.get('plane', Plane.Background))
            """平面"""
            self.startColor : Color = Color(kwargs.get('startColor', 'ffffff'))
            """起始颜色"""
            self.startOpacity : float | int = kwargs.get('startOpacity', 100)
            """起始透明度"""
            self.endColor : Color = Color(kwargs.get('endColor', 'ffffff'))
            """结束颜色"""
            self.endOpacity : float | int = kwargs.get('endOpacity', 0)
            """结束透明度"""
            self.angleOffset : float | int = kwargs.get('angleOffset', 0)
            """角度偏移"""
            self.ease : EASE = value_to_enum(EASE, kwargs.get('ease', EASE.Linear))
            """缓速"""
            self.eventTag : str = kwargs.get('eventTag', '')
            """事件标签"""

    @get_value
    class MoveCamera:
        """移动摄像头"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.VisualEffects.MoveCamera
            """事件类型"""
            self.duration : float | int = kwargs.get('duration', 1)
            """时长"""
            if 'relativeTo' in kwargs:
                self.relativeTo : CAMERA_RELATIVE = value_to_enum(CAMERA_RELATIVE, kwargs.get('relativeTo', CAMERA_RELATIVE.Player))
                """相对于"""
            if 'position' in kwargs:
                self.position : Data_Pair.XY_NonePair = Data_Pair.XY_NonePair.from_tuple(kwargs.get('position', (None, None)))
                """位置"""
            if 'rotation' in kwargs:
                self.rotation : float | int = kwargs.get('rotation', 0)
                """角度"""
            if 'zoom' in kwargs:
                self.zoom : float | int = kwargs.get('zoom', 100)
                """缩放"""
            self.angleOffset : float | int = kwargs.get('angleOffset', 0)
            """角度偏移"""
            self.ease : EASE = value_to_enum(EASE, kwargs.get('ease', EASE.Linear))
            """缓速"""
            self.dontDisable : bool = boolean(kwargs.get('dontDisable', False))
            """不禁用 [关卡编辑器中不可直接编辑]"""
            self.minVfxOnly : bool = boolean(kwargs.get('minVfxOnly', False))
            """仅限低视效 [关卡编辑器中不可直接编辑]"""
            self.eventTag : str = kwargs.get('eventTag', '')
            """事件标签"""
        
    @get_value
    class SetFilter:
        """预设滤镜"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.VisualEffects.SetFilter
            """事件类型"""
            self.filter : Filter = value_to_enum(Filter, kwargs.get('filter', Filter.Grayscale))
            """滤镜"""
            self.enabled : bool = boolean(kwargs.get('enabled', True))
            """启用"""
            self.intensity : float | int = kwargs.get('intensity', 100)
            """强度"""
            self.duration : float | int = kwargs.get('duration', 0)
            """时长"""
            self.ease : EASE = value_to_enum(EASE, kwargs.get('ease', EASE.Linear))
            """缓速"""
            self.disableOthers : bool = boolean(kwargs.get('disableOthers', False))
            """禁用其它"""
            self.angleOffset : float | int = kwargs.get('angleOffset', 0)
            """角度偏移"""
            self.eventTag : str = kwargs.get('eventTag', '')
            """事件标签"""

    @get_value
    class SetFilterAdvanced:
        """预设高级滤镜"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.VisualEffects.SetFilterAdvanced
            """事件类型"""
            self.filter : AdvancedFilterName = value_to_enum(AdvancedFilterName, kwargs.get('filter', AdvancedFilterName.AAA_SuperComputer))
            """滤镜"""
            self.enabled : bool = boolean(kwargs.get('enabled', True))
            """启用"""
            self.disabledOthers : bool = boolean(kwargs.get('disabledOthers', False))
            """禁用其它"""
            self.duration : float | int = kwargs.get('duration', 0)
            """时长"""
            self.ease : EASE = value_to_enum(EASE, kwargs.get('ease', EASE.Linear))
            """缓速"""
            self.targetType : AdvancedFilterTartgetType = value_to_enum(AdvancedFilterTartgetType, kwargs.get('targetType', AdvancedFilterTartgetType.Camera))
            """目标类型 [关卡编辑器中不可直接编辑]"""
            self.plane : Plane = value_to_enum(Plane, kwargs.get('plane', Plane.Foreground))
            """平面"""
            self.targetTag : str = kwargs.get('targetTag', '')
            """目标标签 [仅当targetType设定为Decoration时，关卡编辑器中可以直接编辑]"""
            self.filterProperties : str = kwargs.get('filterProperties', '')
            """滤镜属性"""
            self.angleOffset : float | int = kwargs.get('angleOffset', 0)
            """角度偏移"""
            self.eventTag : str = kwargs.get('eventTag', '')
            """事件标签"""

    @get_value
    class HallOfMirrors:
        """镜厅"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.VisualEffects.HallOfMirrors
            """事件类型"""
            self.enabled : bool = boolean(kwargs.get('enabled', True))
            """启用"""
            self.angleOffset : float | int = kwargs.get('angleOffset', 0)
            """角度偏移"""
            self.eventTag : str = kwargs.get('eventTag', '')
            """事件标签"""

    @get_value
    class ShakeScreen:
        """振屏"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.VisualEffects.ShakeScreen
            """事件类型"""
            self.duration : float | int = kwargs.get('duration', 1)
            """时长"""
            self.strength : float | int = kwargs.get('strength', 100)
            """力度"""
            self.intensity : float | int = kwargs.get('intensity', 100)
            """速度"""
            self.ease : EASE = value_to_enum(EASE, kwargs.get('ease', EASE.Linear))
            """缓速"""
            self.fadeOut : bool = boolean(kwargs.get('fadeOut', True))
            """淡出"""
            self.angleOffset : float | int = kwargs.get('angleOffset', 0)
            """角度偏移"""
            self.eventTag : str = kwargs.get('eventTag', '')
            """事件标签"""

    @get_value
    class Bloom:
        """绽放"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.VisualEffects.Bloom
            """事件类型"""
            self.enabled : bool = boolean(kwargs.get('enabled', True))
            """启用"""
            self.threshold : float | int = kwargs.get('threshold', 50)
            """阈值"""
            self.intensity : float | int = kwargs.get('intensity', 100)
            """强度"""
            self.color : str = kwargs.get('color', 'ffffff')
            """颜色"""
            self.duration : float | int = kwargs.get('duration', 0)
            """时长"""
            self.ease : EASE = value_to_enum(EASE, kwargs.get('ease', EASE.Linear))
            """缓速"""
            self.angleOffset : float | int = kwargs.get('angleOffset', 0)
            """角度偏移"""
            self.eventTag : str = kwargs.get('eventTag', '')
            """事件标签"""

    @get_value
    class ScreenTile:
        """平铺"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.VisualEffects.ScreenTile
            """事件类型"""
            self.duration : float | int = kwargs.get('duration', 0)
            """时长"""
            self.tile : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('tile', (1, 1)))
            """平铺"""
            self.angleOffset : float | int = kwargs.get('angleOffset', 0)
            """角度偏移"""
            self.ease : EASE = value_to_enum(EASE, kwargs.get('ease', EASE.Linear))
            """缓速"""
            self.eventTag : str = kwargs.get('eventTag', '')
            """事件标签"""

    @get_value
    class ScreenScroll:
        """卷屏"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.VisualEffects.ScreenScroll
            """事件类型"""
            self.scroll : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('scroll', (0, 0)))
            """卷屏速度"""
            self.angleOffset : float | int = kwargs.get('angleOffset', 0)
            """角度偏移"""
            self.eventTag : str = kwargs.get('eventTag', '')
            """事件标签"""

    @get_value
    class SetFrameRate:
        """设置帧率"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.VisualEffects.SetFrameRate
            """事件类型"""
            self.enabled : bool = boolean(kwargs.get('enabled', True))
            """启用"""
            self.frameRate : float | int = kwargs.get('frameRate', 5)
            """帧率"""
            self.angleOffset : float | int = kwargs.get('angleOffset', 0)
            """角度偏移"""

    @get_value
    class RepeatEvents:
        """重复事件"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.Modifiers.RepeatEvents
            """事件类型"""
            self.repeatType : RepeatType = value_to_enum(RepeatType, kwargs.get('repeatType', RepeatType.Beat))
            """重复类型"""
            self.repetitions : int = kwargs.get('repetitions', 1)
            """重复次数"""
            self.floorCount : int = kwargs.get('floorCount', 1)
            """重复方块数"""
            self.interval : float | int = kwargs.get('interval', 1)
            """间隔时长"""
            self.executeOnCurrentFloor : bool = boolean(kwargs.get('executeOnCurrentFloor', False))
            """在当前方块执行"""
            self.tag : str = kwargs.get('tag', '')
            """目标标签"""

    @get_value
    class SetConditionalEvents:
        """设置条件事件"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.Modifiers.SetConditionalEvents
            """事件类型"""
            self.perfectTag : str = kwargs.get('perfectTag', '无')
            """“完美”标签"""
            self.hitTag : str = kwargs.get('hitTag', '无')
            """“打击”标签 [关卡编辑器中不可直接编辑]"""
            self.earlyperfectTag : str = kwargs.get('earlyperfectTag', '无')
            """“稍快”标签"""
            self.lateperfectTag : str = kwargs.get('lateperfectTag', '无')
            """“稍慢”标签"""
            self.barelyTag : str = kwargs.get('perfectTag', '无')
            """“勉强”标签 [关卡编辑器中不可直接编辑]"""
            self.veryEarlyTag : str = kwargs.get('veryEarlyTag', '无')
            """“太快”标签"""
            self.veryLateTag : str = kwargs.get('veryLateTag', '无')
            """“太慢”标签"""
            self.missTag : str = kwargs.get('missTag', '无')
            """“miss”标签 [关卡编辑器中不可直接编辑]"""
            self.tooEarlyTag : str = kwargs.get('tooEarlyTag', '无')
            """“特別快”标签"""
            self.tooLateTag : str = kwargs.get('tooLateTag', '无')
            """“特別慢”标签"""
            self.lossTag : str = kwargs.get('lossTag', '无')
            """“丢牌”标签"""
            self.onCheckpointTag : str = kwargs.get('onCheckpointTag', '无')
            """“重启时”标签"""

    @get_value
    class EditorComment:
        """编辑器附注"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.Conveniences.EditorComment
            """事件类型"""
            self.comment : str = kwargs.get('comment', "你可以在这里留下自己的评论！\n\n支持多行文本和<color=#00FF00>彩色</color>文本。")
            """评论"""

    @get_value
    class Bookmark:
        """书签"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.Conveniences.Bookmark
            """事件类型"""

    @get_value
    class Hold:
        """长按"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.DLC.Hold
            """事件类型"""
            self.duration : int = kwargs.get('duration', 0)
            """额外长按循环"""
            self.distanceMultiplier : int = kwargs.get('distanceMultiplier', 100)
            """旅行距离（%）"""
            self.landingAnimation : bool = boolean(kwargs.get('landingAnimation', False))
            """收尾动画"""

    @get_value
    class SetHoldSound: 
        """设置长按音效"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.DLC.SetHoldSound
            """事件类型"""
            self.holdStartSound : HoldSound = value_to_enum(HoldSound, kwargs.get('holdStartSound', HoldSound.Fuse), HoldSound.SingSing)
            """长按开始音效"""
            self.holdLoopSound : HoldSound = value_to_enum(HoldSound, kwargs.get('holdLoopSound', HoldSound.Fuse), HoldSound.SingSing)
            """长按循环音效"""
            self.holdEndSound : HoldSound = value_to_enum(HoldSound, kwargs.get('holdEndSound', HoldSound.Fuse), HoldSound.SingSing)
            """长按结束音效"""
            self.holdMidSound : HoldSound = value_to_enum(HoldSound, kwargs.get('holdMidSound', HoldSound.Fuse))
            """长按中段音效"""
            self.holdMidSoundType : HoldMidSoundType = value_to_enum(HoldMidSoundType, kwargs.get('holdMidSoundType', HoldMidSoundType.Once))
            """长按中段音效类型"""
            self.holdMidSoundDelay : float | int = kwargs.get('holdMidSoundDelay', 0.5)
            """长按中段音效延迟"""
            self.holdMidSoundTimingRelativeTo : HoldMidSoundTimingRelative = value_to_enum(HoldMidSoundTimingRelative, kwargs.get('holdMidSoundTimingRelativeTo', HoldMidSoundTimingRelative.End))
            """长按中段音效延迟关联到"""
            self.holdSoundVolume : int = kwargs.get('holdSoundVolume', 100)
            """长按音效音量"""
        
    @get_value
    class MultiPlanet:
        """多行星"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.DLC.MultiPlanet
            """事件类型"""
            self.planets : MultiPlanets = value_to_enum(MultiPlanets, kwargs.get('planets', MultiPlanets.TwoPlanets))
            """行星数"""

    @get_value
    class FreeRoam:
        """自由移动段落"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.DLC.FreeRoam
            """事件类型"""
            self.duration : int = kwargs.get('duration', 16)
            """时长"""
            self.size : Data_Pair.XY_natural_Pair = Data_Pair.XY_natural_Pair.from_tuple(kwargs.get('size', (4, 4)))
            """自由区域大小"""
            self.positionOffset : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('positionOffset', (0, 0)))
            """位置偏移"""
            self.outTime : int = kwargs.get('outTime', 4)
            """退出过渡时长"""
            self.outEase : EASE = value_to_enum(EASE, kwargs.get('ease', EASE.InOutSine))
            """缓速"""
            self.hitsoundOnBeats : HITSOUND = value_to_enum(HITSOUND, kwargs.get('hitsoundOnBeats', HITSOUND.NONE))
            """强拍击拍音效"""
            self.hitsoundOffBeats : HITSOUND = value_to_enum(HITSOUND, kwargs.get('hitsoundOffBeats', HITSOUND.NONE))
            """弱拍击拍音效"""
            self.countdownTicks : int = kwargs.get('countdownTicks', 4)
            """计数滴答"""
            self.angleCorrectionDir : int = kwargs.get('angleCorrectionDir', -1)
            """角度校准（-1, 0, 1）"""

    @get_value
    class FreeRoamTwirl:
        """自由旋转"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.DLC.FreeRoamTwirl
            """事件类型"""
            self.position : Data_Pair.XY_natural_Pair = Data_Pair.XY_natural_Pair.from_tuple(kwargs.get('position', (1, 0)))
            """位置偏移"""

    @get_value
    class FreeRoamRemove:
        """自由移除"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.DLC.FreeRoamRemove
            """事件类型"""
            self.position : Data_Pair.XY_natural_Pair = Data_Pair.XY_natural_Pair.from_tuple(kwargs.get('position', (1, 0)))
            """位置偏移"""
            self.size : Data_Pair.XY_natural_Pair = Data_Pair.XY_natural_Pair.from_tuple(kwargs.get('size', (1, 1)))
            """要移除的区域大小"""

    @get_value
    class Hide:
        """隐藏判定/地板图标"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.DLC.Hide
            """事件类型"""
            self.hideJudgment : bool = boolean(kwargs.get('hideJudgement', False))
            """隐藏判定文本"""
            self.hideTileIcon : bool = boolean(kwargs.get('hideTileIcon', False))
            """隐藏方块图标"""

    @get_value
    class ScaleMargin:
        """定时窗口大小"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.DLC.ScaleMargin
            """事件类型"""
            self.scale : float | int = kwargs.get('scale', 100)
            """大小"""

    @get_value
    class ScaleRadius:
        """星球半径大小"""
        def __init__(self, floor:int | None = None, **kwargs) -> None:
            if floor is None:
                floor = kwargs.get('floor')
            if floor is None:
                raise KeyError('"floor" must be provied as argument or in kwargs')
            self.floor : int = floor
            """事件所在砖块"""
            self.eventType = eventTypes.DLC.ScaleRadius
            """事件类型"""
            self.scale : float | int = kwargs.get('scale', 100)
            """大小"""

Action = ACTION.SetSpeed | ACTION.Twirl | ACTION.Checkpoint | ACTION.SetHitsound | ACTION.PlaySound | ACTION.SetPlanetRotation | ACTION.Pause | ACTION.AutoPlayTiles | ACTION.ScalePlanets | ACTION.ColorTrack | ACTION.AnimateTrack | ACTION.RecolorTrack | ACTION.MoveTrack | ACTION.PositionTrack | ACTION.MoveDecorations | ACTION.SetText | ACTION.EmitParticle | ACTION.SetParticle | ACTION.SetObject | ACTION.SetDefaultText | ACTION.CustomBackground | ACTION.Flash | ACTION.MoveCamera | ACTION.SetFilter | ACTION.SetFilterAdvanced | ACTION.HallOfMirrors | ACTION.ShakeScreen | ACTION.Bloom | ACTION.ScreenTile | ACTION.ScreenScroll | ACTION.SetFrameRate | ACTION.RepeatEvents | ACTION.SetConditionalEvents | ACTION.EditorComment | ACTION.Bookmark | ACTION.Hold | ACTION.SetHoldSound | ACTION.MultiPlanet | ACTION.FreeRoam | ACTION.FreeRoamTwirl | ACTION.FreeRoamRemove | ACTION.Hide | ACTION.ScaleMargin | ACTION.ScaleRadius