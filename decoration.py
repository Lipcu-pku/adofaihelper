from .enums import *

class DECORATION:
    
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

    @get_value
    class AddDecoration:
        """添加装饰"""
        def __init__(self, **kwargs) -> None:
            if 'floor' in kwargs:
                self.floor = int(kwargs['floor'])
                """事件所在砖块"""
            self.eventType = eventTypes.AddDecorations.AddDecoration
            """事件类型"""
            self.decorationImage = str(kwargs.get('decorationImage', ''))
            """装饰图片（相对文件路径）"""
            self.position = Data_Pair.XY_Pair.from_tuple(kwargs.get('position', (0, 0)))
            """位置"""
            self.relativeTo = DecorationRelative(kwargs.get('relativeTo', DecorationRelative.Global))
            """相对于"""
            if 'stickToFloor' in kwargs:
                self.stickToFloor = boolean(kwargs.get('stickToFloor', False))
                """依附地板"""
            self.pivotOffset = Data_Pair.XY_Pair.from_tuple(kwargs.get('pivotOffset', (0, 0)))
            """轴心偏移"""
            self.rotation = int(kwargs.get('rotation', 0))
            """旋转"""
            if 'lockRotation' in kwargs:
                self.lockRotation = boolean(kwargs.get('lockRotation', False))
                """锁定转角"""
            self.scale = Data_Pair.XY_Pair.from_tuple(kwargs.get('scale', (100, 100)))
            """缩放"""
            if 'lockScale' in kwargs:
                self.lockScale= boolean(kwargs.get('lockScale', False))
                """锁定缩放"""
            self.tile = Data_Pair.XY_natural_Pair.from_tuple(kwargs.get('tile', (1, 1)), False)
            """平铺装饰"""
            self.color = Color(kwargs.get('color', 'ffffff'))
            """颜色"""
            self.opacity = int(kwargs.get('opacity', 100))
            """透明度"""
            self.depth = int(kwargs.get('depth', -1))
            """深度"""
            if 'syncFloorDepth' in kwargs:
                self.syncFloorDepth = boolean(kwargs.get('syncFloorDepth', False))
                """同步地板深度"""
            self.parallax = Data_Pair.XY_Pair.from_tuple(kwargs.get('parallax', (0, 0)))
            """平行"""
            if 'parallaxOffset' in kwargs:
                self.parallaxOffset = Data_Pair.XY_Pair.from_tuple(kwargs.get('parallaxOffset', (0, 0)))
                """视差偏移"""
            self.tag = str(kwargs.get('tag', ''))
            """标签"""
            self.imageSmoothing = boolean(kwargs.get('imageSmoothing', True))
            """图像平滑"""
            self.blendMode = BlendMode(kwargs.get('blendMode', BlendMode.NONE))
            """混合模式"""
            self.maskingType = MaskType(kwargs.get('maskingType', MaskType.NONE))
            """遮罩类型"""
            self.maskingTarget = str(kwargs.get('maskingTarget', ''))
            """遮罩对象 [编辑器中不可直接编辑]"""
            self.useMaskingDepth = boolean(kwargs.get('useMaskingDepth', False))
            """使用遮罩深度"""
            self.maskingFrontDepth = int(kwargs.get('maskingFronDepth', -1))
            """遮罩起始深度"""
            self.maskingBackDepth = int(kwargs.get('maskingBackDepth', -1))
            """遮罩结束深度"""
            self.hitbox = Hitbox(kwargs.get('hitbox', Hitbox.NONE))
            """判定框"""
            self.hitboxDetectTarget = HitboxTarget(kwargs.get('hitboxDetectTarget', HitboxTarget.Planet))
            """判定框检查目标"""
            self.hitboxDecoTag = str(kwargs.get('hitboxDecoTag', ''))
            """待检测装饰物标签"""
            self.hitboxTriggerType = HitboxTriggerType(kwargs.get('hitboxTriggerType', HitboxTriggerType.Once))
            """判定框触发类型"""
            self.RepeatInterval = int(kwargs.get('RepeatInterval', 1000))
            """判定框触发重复间隔"""
            self.hitboxEventTag = str(kwargs.get('hitboxEventTag', ''))
            """事件运行标签"""
            self.failHitboxType = HitboxType(kwargs.get('failHitboxType', HitboxType.Box))
            """判定框形状"""
            self.failHitboxScale = Data_Pair.XY_Pair.from_tuple(kwargs.get('failHitboxScale', (100, 100)))
            """判定框大小"""
            self.failHitboxOffset = Data_Pair.XY_Pair.from_tuple(kwargs.get('failHitboxOffset', (0, 0)))
            """判定框偏移"""
            self.failHitboxRotation = int(kwargs.get('failHitboxRotation', 0))
            """判定框旋转"""
            self.components = str(kwargs.get('components', ''))
            """组成 [关卡编辑器中不可直接编辑]"""

    @get_value
    class AddText:
        """添加文本"""
        def __init__(self, **kwargs) -> None:
            if 'floor' in kwargs:
                self.floor = int(kwargs['floor'])
                """事件所在砖块"""
            self.eventType = eventTypes.AddDecorations.AddText
            """事件类型"""
            self.decText = str(kwargs.get('decText', '文本'))
            """文本"""
            self.font = Font(kwargs.get('font', Font.Default))
            """字体"""
            self.position = Data_Pair.XY_Pair.from_tuple(kwargs.get('position', (0, 0)))
            """位置"""
            self.relativeTo = DecorationRelative(kwargs.get('relativeTo', DecorationRelative.Global))
            """相对于"""
            self.pivotOffset = Data_Pair.XY_Pair.from_tuple(kwargs.get('pivotOffset', (0, 0)))
            """轴心偏移"""
            self.rotation = int(kwargs.get('rotation', 0))
            """旋转"""
            self.lockRotation = boolean(kwargs.get('lockRotation', False))
            """锁定转角"""
            self.scale = Data_Pair.XY_Pair.from_tuple(kwargs.get('scale', (100, 100)))
            """大小"""
            self.lockScale = boolean(kwargs.get('lockScale', False))
            """锁定大小"""
            self.color = Color(kwargs.get('color', 'ffffff'))
            """颜色"""
            self.opacity = int(kwargs.get('opacity', 100))
            """透明度"""
            self.depth = int(kwargs.get('depth', -1))
            """深度"""
            self.parallax = Data_Pair.XY_Pair.from_tuple(kwargs.get('parallax', (0, 0)))
            """平行"""
            self.parallaxOffset = Data_Pair.XY_Pair.from_tuple(kwargs.get('parallaxOffset', (0, 0)))
            """视差偏移"""
            self.tag = str(kwargs.get('tag', ''))
            """标签"""

    @get_value
    class AddObject:
        """添加对象"""
        def __init__(self, **kwargs) -> None:
            if 'floor' in kwargs:
                self.floor = int(kwargs['floor'])
                """事件所在砖块"""
            self.eventType = eventTypes.AddDecorations.AddObject
            """事件类型"""
            self.objectType = ObjectType(kwargs.get('objectType', ObjectType.Floor))
            """对象类型"""
            
            self.planetColorType = PlanetColorType(kwargs.get('planetColorType', PlanetColorType.DefaultRed))
            """星球颜色类型"""
            self.planetColor = Color(kwargs.get('planetColor', 'ff0000'))
            """星球颜色"""
            self.planetTailColor = Color(kwargs.get('planetTailColor', 'ff0000'))
            """星球轨迹颜色"""

            self.trackType = TrackType(kwargs.get('trackType', TrackType.Normal))
            """轨道样式"""
            self.trackAngle = int(kwargs.get('trackAngle', 180))
            """轨道角度"""

            self.trackColorType = TRACK_COLOR_TYPE(kwargs.get('trackColorType', TRACK_COLOR_TYPE.Single))
            """轨道颜色类型"""
            self.trackColor = Color(kwargs.get('trackColor', 'debb7b'))
            """轨道主色调"""
            self.secondaryTrackColor = Color(kwargs.get('secondaryTrackColor' , 'ffffff'))
            """轨道副色调"""
            self.trackColorAnimDuration = int(kwargs.get('trackColorAnimDuration', 2))
            """色彩动画间隔"""
            self.trackOpacity = int(kwargs.get('trackOpacity', 100))
            """轨道透明度"""
            self.trackStyle = TRACK_STYLE(kwargs.get('trackStyle', TRACK_STYLE.Standard))
            """轨道风格"""
            self.trackIcon = TrackIcon(kwargs.get('trackIcon', TrackIcon.NONE))
            """图标"""
            self.trackIconAngle = int(kwargs.get('trackIconAngle', 0))
            """轨道图标角度"""
            self.trackIconFlipped = boolean(kwargs.get('trackIconFlipped', False))
            """轨道图标翻转"""
            self.trackRedSwirl = boolean(kwargs.get('trackRedSwirl', False))
            """红色漩涡"""
            self.trackGraySetSpeedIcon = boolean(kwargs.get('trackGraySetSpeedIcon', False))
            """灰色设置速度图标"""
            self.trackSetSpeedIconBpm = int(kwargs.get('trackSetSpeedIconBpm', 100))
            """设置速度图标BPM"""
            self.trackGlowEnabled = boolean(kwargs.get('trackGlowIntensity', False))
            """允许轨道发光"""
            self.trackGlowColor = Color(kwargs.get('trackGlowColor', 'ffffff'))
            """轨道发光颜色"""
            self.trackIconOutlines = boolean(kwargs.get('trackIconOutlines', False))
            """方块图标描边"""
            self.position = Data_Pair.XY_Pair.from_tuple(kwargs.get('position', (0, 0)))
            """位置"""
            self.relativeTo = DecorationRelative(kwargs.get('relativeTo', DecorationRelative.Global))
            """相对于"""
            self.pivotOffset = Data_Pair.XY_Pair.from_tuple(kwargs.get('pivotOffset', (0, 0)))
            """轴心偏移"""
            self.rotation = int(kwargs.get('rotation', 0))
            """旋转"""
            self.lockRotation = boolean(kwargs.get('lockRotation', False))
            """锁定转角"""
            self.scale = Data_Pair.XY_Pair.from_tuple(kwargs.get('scale', (100, 100)))
            """大小"""
            self.lockScale = boolean(kwargs.get('lockScale', False))
            """锁定大小"""
            self.depth = int(kwargs.get('depth', -1))
            """深度"""
            self.syncFloorDepth = boolean(kwargs.get('syncFloorDepth', False))
            """同步地板深度"""
            self.parallax = Data_Pair.XY_Pair.from_tuple(kwargs.get('parallax', (0, 0)))
            """平行"""
            self.parallaxOffset = Data_Pair.XY_Pair.from_tuple(kwargs.get('parallaxOffset', (0, 0)))
            """视差偏移"""
            self.tag = str(kwargs.get('tag', ''))
            """标签"""

    @get_value
    class AddParticle:
        """添加粒子"""
        def __init__(self, **kwargs) -> None:
            self.value = kwargs
            pass
            '''if 'floor' in kwargs:
                self.floor = kwargs['floor']
                """事件所在砖块"""
            self.eventType = eventTypes.AddDecorations.AddParticle
            """事件类型"""



            """ 编辑粒子 - 基本 """
            self.simulationSpace = ParticleSimulationSpace(kwargs.get('simulationSpace', ParticleSimulationSpace.Local))
            """粒子模拟空间"""
            self.maxParticles = kwargs.get('maxParticles', 1000)
            """最大粒子数"""
            self.playDuration = kwargs.get('playDuration', 5)
            """播放时长（秒）"""
            self.loop = boolean(kwargs.get('loop', True))
            """循环"""
            self.simulationSpeed = kwargs.get('simulationSpeed', 100)
            """模拟速度"""
            self.randomSeed = kwargs.get('randomSeed', 0)
            """随机种子"""


            """ 编辑粒子 - 形状 """
            self.decorationImage = kwargs.get('decorationImage', '')
            """装饰图片（相对文件路径）"""
            self.randomTextureTiling = Data_Pair.XY_Pair.from_tuple(kwargs.get('randomTextureTiling', (1, 1)))
            """随机纹理平铺"""
            self.startRotation = Data_Pair.Increasing_Range_Pair.from_tuple(kwargs.get('startRotation', (0, 0)))
            """开始旋转"""
            self.color = ParticleColor(**kwargs.get('color', {"color1": "ffffff", "mode": "Color"}))
            """颜色"""
            self.particleLifetime = Data_Pair.Increasing_Range_Pair.from_tuple(kwargs.get('particleLifetime', (10, 10)))
            """粒子持续时间"""
            self.particleSize = Data_Pair.Increasing_Range_Pair.from_tuple(kwargs.get('particleSize', (100, 100)))
            """粒子大小"""
            self.shapeType = ParticleShapeType(kwargs.get('shapeType'))
            """粒子发射形状"""
            self.shapeRadius = kwargs.get('shapeRadius', 1)
            """半径"""
            self.emissionRate = kwargs.get('emissionRate', 10)
            """发送频率"""
            


            """ 编辑粒子 - 变换 """
            self.velocityLimitOverLifetime = Data_Pair.Range_Pair.from_tuple(kwargs.get('velocityLimitOverLifetime', (0, 0)))
            """生命周期限速"""
            if 'colorOverLifetime' in kwargs:
                self.colorOverLifetime : ParticleColor = ParticleColor(kwargs.get('colorOverLifetime'))
                """随时间变色"""
            if 'sizeOverLifetime' in kwargs:
                self.sizeOverLifetime = Data_Pair.Range_Pair.from_tuple(kwargs.get('sizeOverLifetime'))
                """随时间缩放"""
            self.velocity = Data_Pair.Increasing_XY_Pair.from_tuple(kwargs.get('velocity', ((0, 0), (0, 0))))
            """随时间变速"""
            self.rotationOverTime = Data_Pair.Increasing_Range_Pair.from_tuple(kwargs.get('rotationOverTime', (0, 0)))
            """随时间旋转"""
            self.arc = kwargs.get('arc', 360)
            """弧"""
            self.arcMode = ParticleArcMode(kwargs.get('arcMode', ParticleArcMode.Random))
            """弧模式"""



            self.autoPlay = boolean(kwargs.get('autoPlay', True))
            """开始时播放"""
            self.position = Data_Pair.XY_Pair.from_tuple(kwargs.get('position', (0, 0)))
            """位置"""
            self.relativeTo = DecorationRelative(kwargs.get('relativeTo', DecorationRelative.Global))
            """相对于"""
            self.pivotOffset = Data_Pair.XY_Pair.from_tuple(kwargs.get('pivotOffset', (0, 0)))
            """轴心偏移"""
            self.rotation = int(kwargs.get('rotation', 0))
            """旋转"""
            self.scale = Data_Pair.XY_Pair.from_tuple(kwargs.get('scale', (100, 100)))
            """大小"""
            self.depth = int(kwargs.get('depth', -1))
            """深度"""
            self.parallax = Data_Pair.XY_Pair.from_tuple(kwargs.get('parallax', (0, 0)))
            """平行"""
            self.parallaxOffset = Data_Pair.XY_Pair.from_tuple(kwargs.get('parallaxOffset', (0, 0)))
            """视差偏移"""
            self.lockRotation = boolean(kwargs.get('lockRotation', False))
            """锁定转角"""
            self.lockScale = boolean(kwargs.get('lockScale', False))
            """锁定大小"""
            self.tag = kwargs.get('tag', '')
            """标签"""'''

Decoration = DECORATION.AddDecoration | DECORATION.AddText | DECORATION.AddObject | DECORATION.AddParticle
