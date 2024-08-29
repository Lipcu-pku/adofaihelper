from enums import *

class DECORATION:

    @property
    def value(self):
        d = {}
        for key, value in self.__dict__.items():
            if isinstance(value, int | float | str | bool | NoneType):
                d[key] = value
            else:
                d[key] = value.value
        return d
    
    @classmethod
    def load(cls, eventType: str | EventTypes | None = None, **kwargs):
        """
        将字典型转化为Action型

        :param eventType: 必须的参数eventType，若未传入则应当在kwargs中声明
        :param kwargs: 事件的其他参数，若未传入则按该事件的默认参数处理

        :return: 对应事件类型的Action类
        """

        if eventType is None:
            eventType = kwargs.get('eventType')
        
        if eventType is None:
            raise ValueError('param "eventType" must be provided as an argument or in kwargs')
        
        kwargs['eventType'] = eventType
        
        eventType = value_to_subenum(eventTypes, kwargs['eventType'])
        match eventType:
            case eventTypes.AddDecorations.AddDecoration:
                return cls.AddDecoration(**kwargs)
            case eventTypes.AddDecorations.AddText:
                return cls.AddText(**kwargs)
            case eventTypes.AddDecorations.AddObject:
                return cls.AddObject(**kwargs)
            case eventTypes.AddDecorations.AddParticle:
                return cls.AddParticle(**kwargs)
            case _:
                raise ValueError(f'The eventType {eventType.name} is not a Decoration')

    class AddDecoration:
        """添加装饰"""
        def __init__(self, **kwargs) -> None:
            if 'floor' in kwargs:
                self.floor = kwargs['floor']
                """事件所在砖块"""
            self.eventType = eventTypes.AddDecorations.AddDecoration
            """事件类型"""
            self.decorationImage : str = kwargs.get('decorationImage', '')
            """装饰图片（相对文件路径）"""
            self.position : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('position', (0, 0)))
            """位置"""
            self.relativeTo : DecorationRelative = value_to_enum(DecorationRelative, kwargs.get('relativeTo', DecorationRelative.Global))
            """相对于"""
            self.stickToFloor : bool = boolean(kwargs.get('stickToFloor', False))
            """依附地板"""
            self.pivotOffset : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('pivotOffset', (0, 0)))
            """轴心偏移"""
            self.rotation : float | int = kwargs.get('rotation', 0)
            """旋转"""
            self.lockRotation : bool = boolean(kwargs.get('lockRotation', False))
            """锁定转角"""
            self.tile : Data_Pair.XY_natural_Pair = Data_Pair.XY_natural_Pair.from_tuple(kwargs.get('tile', (1, 1)), False)
            """平铺装饰"""
            self.color : str = kwargs.get('color', 'ffffff')
            """颜色"""
            self.opacity : float | int = kwargs.get('opacity', 100)
            """透明度"""
            self.depth : int = kwargs.get('depth', -1)
            """深度"""
            self.syncFloorDepth : bool = boolean(kwargs.get('syncFloorDepth', False))
            """同步地板深度"""
            self.parallax : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('parallax', (0, 0)))
            """平行"""
            self.parallaxOffset : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('parallaxOffset', (0, 0)))
            """视差偏移"""
            self.tag : str = kwargs.get('tag', '')
            """标签"""
            self.imageSmoothing : bool = boolean(kwargs.get('imageSmoothing', True))
            """图像平滑"""
            self.blendMode : BlendMode = value_to_enum(BlendMode, kwargs.get('blendMode', BlendMode.NONE))
            """混合模式"""
            self.maskingType : MaskType = value_to_enum(MaskType, kwargs.get('maskingType', MaskType.NONE))
            """遮罩类型"""
            self.maskingTarget : str = kwargs.get('maskingTarget', '')
            """遮罩对象 [编辑器中不可直接编辑]"""
            self.useMaskingDepth : bool = boolean(kwargs.get('useMaskingDepth', False))
            """使用遮罩深度"""
            self.maskingFrontDepth : int = kwargs.get('maskingFronDepth', -1)
            """遮罩起始深度"""
            self.maskingBackDepth : int = kwargs.get('maskingBackDepth', -1)
            """遮罩结束深度"""
            self.hitbox : Hitbox = value_to_enum(Hitbox, kwargs.get('hitbox', Hitbox.NONE))
            """判定框"""
            self.hitboxDetectTarget : HitboxTarget = value_to_enum(HitboxTarget, kwargs.get('hitboxDetectTarget', HitboxTarget.Planet))
            """判定框检查目标"""
            self.hitboxDecoTag : str = kwargs.get('hitboxDecoTag', '')
            """待检测装饰物标签"""
            self.hitboxTriggerType : HitboxTriggerType = value_to_enum(HitboxTriggerType, kwargs.get('hitboxTriggerType', HitboxTriggerType.Once))
            """判定框触发类型"""
            self.RepeatInterval : float | int = kwargs.get('RepeatInterval', 1000)
            """判定框触发重复间隔"""
            self.hitboxEventTag : str = kwargs.get('hitboxEventTag', '')
            """事件运行标签"""
            self.failHitboxType : HitboxType = value_to_enum(HitboxType, kwargs.get('failHitboxType', HitboxType.Box))
            """判定框形状"""
            self.failHitboxScale : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('failHitboxScale', (100, 100)))
            """判定框大小"""
            self.failHitboxOffset : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('failHitboxOffset', (0, 0)))
            """判定框偏移"""
            self.failHitboxRotation : float | int = kwargs.get('failHitboxRotation', 0)
            """判定框旋转"""
            self.components : str = kwargs.get('components', '')
            """组成 [关卡编辑器中不可直接编辑]"""

    class AddText:
        """添加文本"""
        def __init__(self, **kwargs) -> None:
            if 'floor' in kwargs:
                self.floor = kwargs['floor']
                """事件所在砖块"""
            self.eventType = eventTypes.AddDecorations.AddText
            """事件类型"""
            self.decText : str = kwargs.get('decText', '文本')
            """文本"""
            self.font : Font = value_to_enum(Font, kwargs.get('font', Font.Default))
            """字体"""
            self.position : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('position', (0, 0)))
            """位置"""
            self.relativeTo : DecorationRelative = value_to_enum(DecorationRelative, kwargs.get('relativeTo', DecorationRelative.Global))
            """相对于"""
            self.pivotOffset : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('pivotOffset', (0, 0)))
            """轴心偏移"""
            self.rotation : float | int = kwargs.get('rotation', 0)
            """旋转"""
            self.lockRotation : bool = boolean(kwargs.get('lockRotation', False))
            """锁定转角"""
            self.scale : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('scale', (100, 100)))
            """大小"""
            self.lockScale : bool = boolean(kwargs.get('lockScale', False))
            """锁定大小"""
            self.color : str = kwargs.get('color', 'ffffff')
            """颜色"""
            self.opacity : float | int = kwargs.get('opacity', 100)
            """透明度"""
            self.depth : int = kwargs.get('depth', -1)
            """深度"""
            self.parallax : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('parallax', (0, 0)))
            """平行"""
            self.parallaxOffset : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('parallaxOffset', (0, 0)))
            """视差偏移"""
            self.tag : str = kwargs.get('tag', '')
            """标签"""

    class AddObject:
        """添加对象"""
        def __init__(self, **kwargs) -> None:
            if 'floor' in kwargs:
                self.floor = kwargs['floor']
                """事件所在砖块"""
            self.eventType = eventTypes.AddDecorations.AddObject
            """事件类型"""
            self.objectType : ObjectType = value_to_enum(ObjectType, kwargs.get('objectType', ObjectType.Floor))
            """对象类型"""
            
            self.planetColorType : PlanetColorType = value_to_enum(PlanetColorType, kwargs.get('planetColorType', PlanetColorType.DefaultRed))
            """星球颜色类型"""
            self.planetColor : Color = Color(kwargs.get('planetColor', 'ff0000'))
            """星球颜色"""
            self.planetTailColor : Color = Color(kwargs.get('planetTailColor', 'ff0000'))
            """星球轨迹颜色"""

            self.trackType : TrackType = value_to_enum(TrackType, kwargs.get('trackType', TrackType.Normal))
            """轨道样式"""
            self.trackAngle : float | int = kwargs.get('trackAngle', 180)
            """轨道角度"""

            self.trackColorType : TRACK_COLOR_TYPE = value_to_enum(TRACK_COLOR_TYPE, kwargs.get('trackColorType', TRACK_COLOR_TYPE.Single))
            """轨道颜色类型"""
            self.trackColor : Color = Color(kwargs.get('trackColor', 'debb7b'))
            """轨道主色调"""
            self.secondaryTrackColor : Color = Color(kwargs.get('secondaryTrackColor' , 'ffffff'))
            """轨道副色调"""
            self.trackColorAnimDuration : float | int = kwargs.get('trackColorAnimDuration', 2)
            """色彩动画间隔"""
            self.trackOpacity : float | int = kwargs.get('trackOpacity', 100)
            """轨道透明度"""
            self.trackStyle : TRACK_STYLE = value_to_enum(TRACK_STYLE, kwargs.get('trackStyle', TRACK_STYLE.Standard))
            """轨道风格"""
            self.trackIcon : TrackIcon = value_to_enum(TrackIcon, kwargs.get('trackIcon', TrackIcon.NONE))
            """图标"""
            self.trackIconAngle : float | int = kwargs.get('trackIconAngle', 0)
            """轨道图标角度"""
            self.trackIconFlipped : bool = boolean(kwargs.get('trackIconFlipped', False))
            """轨道图标翻转"""
            self.trackRedSwirl : bool = boolean(kwargs.get('trackRedSwirl', False))
            """红色漩涡"""
            self.trackGraySetSpeedIcon : bool = boolean(kwargs.get('trackGraySetSpeedIcon', False))
            """灰色设置速度图标"""
            self.trackSetSpeedIconBpm : float | int = kwargs.get('trackSetSpeedIconBpm', 100)
            """设置速度图标BPM"""
            self.trackGlowEnabled : bool = boolean(kwargs.get('trackGlowIntensity', False))
            """允许轨道发光"""
            self.trackGlowColor : Color = Color(kwargs.get('trackGlowColor', 'ffffff'))
            """轨道发光颜色"""
            self.trackIconOutlines : bool = boolean(kwargs.get('trackIconOutlines', False))
            """方块图标描边"""
            self.position : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('position', (0, 0)))
            """位置"""
            self.relativeTo : DecorationRelative = value_to_enum(DecorationRelative, kwargs.get('relativeTo', DecorationRelative.Global))
            """相对于"""
            self.pivotOffset : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('pivotOffset', (0, 0)))
            """轴心偏移"""
            self.rotation : float | int = kwargs.get('rotation', 0)
            """旋转"""
            self.lockRotation : bool = boolean(kwargs.get('lockRotation', False))
            """锁定转角"""
            self.scale : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('scale', (100, 100)))
            """大小"""
            self.lockScale : bool = boolean(kwargs.get('lockScale', False))
            """锁定大小"""
            self.depth : int = kwargs.get('depth', -1)
            """深度"""
            self.syncFloorDepth : bool = boolean(kwargs.get('syncFloorDepth', False))
            """同步地板深度"""
            self.parallax : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('parallax', (0, 0)))
            """平行"""
            self.parallaxOffset : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('parallaxOffset', (0, 0)))
            """视差偏移"""
            self.tag : str = kwargs.get('tag', '')
            """标签"""

    class AddParticle:
        """添加粒子"""
        def __init__(self, **kwargs) -> None:
            if 'floor' in kwargs:
                self.floor = kwargs['floor']
                """事件所在砖块"""
            self.eventType = eventTypes.AddDecorations.AddParticle
            """事件类型"""



            """ 编辑粒子 - 基本 """
            self.simulationSpace : ParticleSimulationSpace = value_to_enum(ParticleSimulationSpace, kwargs.get('simulationSpace', ParticleSimulationSpace.Local))
            """粒子模拟空间"""
            self.maxParticles : int = kwargs.get('maxParticles', 1000)
            """最大粒子数"""
            self.playDuration : float | int = kwargs.get('playDuration', 5)
            """播放时长（秒）"""
            self.loop : bool = boolean(kwargs.get('loop', True))
            """循环"""
            self.simulationSpeed : float | int = kwargs.get('simulationSpeed', 100)
            """模拟速度"""
            self.randomSeed : int = kwargs.get('randomSeed', 0)
            """随机种子"""


            """ 编辑粒子 - 形状 """
            self.decorationImage : str = kwargs.get('decorationImage', '')
            """装饰图片（相对文件路径）"""
            self.randomTextureTiling : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('randomTextureTiling', (1, 1)))
            """随机纹理平铺"""
            self.startRotation : Data_Pair.Increasing_Range_Pair = Data_Pair.Increasing_Range_Pair.from_tuple(kwargs.get('startRotation', (0, 0)))
            """开始旋转"""
            self.color : ParticleColor = ParticleColor(**kwargs.get('color', {"color1": "ffffff", "mode": "Color"}))
            """颜色"""
            self.particleLifetime : Data_Pair.Increasing_Range_Pair = Data_Pair.Increasing_Range_Pair.from_tuple(kwargs.get('particleLifetime', [10, 10]))
            """粒子持续时间"""
            self.particleSize : Data_Pair.Increasing_Range_Pair = Data_Pair.Increasing_Range_Pair.from_tuple(kwargs.get('particleSize', (100, 100)))
            """粒子大小"""
            self.shapeType : ParticleShapeType = value_to_enum(ParticleShapeType, kwargs.get('shapeType'))
            """粒子发射形状"""
            self.shapeRadius : float | int = kwargs.get('shapeRadius', 1)
            """半径"""
            self.emissionRate : int = kwargs.get('emissionRate', 10)
            """发送频率"""
            


            """ 编辑粒子 - 变换 """
            self.velocityLimitOverLifetime : Data_Pair.Range_Pair = Data_Pair.Range_Pair.from_tuple(kwargs.get('velocityLimitOverLifetime', (0, 0)))
            """生命周期限速"""
            self.colorOverLifetime : ParticleColor = ParticleColor(**kwargs['colorOverLifetime'])
            """随时间变色"""
            self.sizeOverLifetime : Data_Pair.Range_Pair = Data_Pair.Range_Pair.from_tuple(kwargs.get('sizeOverLifetime', (100, 100)))
            """随时间缩放"""
            self.velocity : Data_Pair.Increasing_XY_Pair = Data_Pair.Increasing_Range_Pair.from_tuple(kwargs.get('velocity', ((0, 0), (0, 0))))
            """随时间变速"""
            self.rotationOverTime : Data_Pair.Increasing_Range_Pair = Data_Pair.Increasing_Range_Pair.from_tuple(kwargs.get('rotationOverTime', (0, 0)))
            """随时间旋转"""
            self.arc : float | int = kwargs.get('arc', 360)
            """弧"""
            self.arcMode : ParticleArcMode = value_to_enum(ParticleArcMode, kwargs.get('arcMode', ParticleArcMode.Random))
            """弧模式"""



            self.autoPlay : bool = boolean(kwargs.get('autoPlay', True))
            """开始时播放"""
            self.position : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('position', (0, 0)))
            """位置"""
            self.relativeTo : DecorationRelative = value_to_enum(kwargs.get('relativeTo', DecorationRelative.Global))
            """相对于"""
            self.pivotOffset : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('pivotOffset', (0, 0)))
            """轴心偏移"""
            self.rotation : float | int = kwargs.get('rotation', 0)
            """旋转"""
            self.scale : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('scale', (100, 100)))
            """大小"""
            self.depth : int = kwargs.get('depth', -1)
            """深度"""
            self.parallax : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('parallax', (0, 0)))
            """平行"""
            self.parallaxOffset : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('parallaxOffset', (0, 0)))
            """视差偏移"""
            self.lockRotation : bool = boolean(kwargs.get('lockRotation', False))
            """锁定转角"""
            self.lockScale : bool = boolean(kwargs.get('lockScale', False))
            """锁定大小"""
            self.tag : str = kwargs.get('tag', '')
            """标签"""

Decoration = DECORATION.AddDecoration | DECORATION.AddText | DECORATION.AddObject | DECORATION.AddParticle