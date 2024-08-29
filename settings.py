from enums import *


class SETTINGS:

    def __init__(self, **kwargs) -> None:
        self.version : int = kwargs.get('version', 15)
        """关卡编辑器的版本号，当前游戏最新版本版本号为15（v2.8.1 Alpha/r123 (a6926c3, 2024/08/28 9:45 AM)）"""
        self.artist : str = kwargs.get('artist', '')
        """关卡音乐的作者"""
        self.specialArtistType : SPECIAL_ARTIST_TYPE = value_to_enum(SPECIAL_ARTIST_TYPE, kwargs.get('specialArtistType', SPECIAL_ARTIST_TYPE.NONE))
        """关卡音乐作者的特殊授权"""
        self.artistPermission : str = kwargs.get('artistPermission', '')
        """关卡音乐的艺术家授权（相对文件路径）"""
        self.song : str = kwargs.get('song', '')
        """关卡音乐名"""
        self.author : str = kwargs.get('author', '')
        """关卡作者"""
        self.separateCountdownTime : bool = boolean(kwargs.get('separateCountdownTime', True))
        """[关卡编辑器中不可直接编辑]"""
        self.previewImage : str = kwargs.get('previewImage', '')
        """传送门图片（相对文件路径）"""
        self.previewIcon : str = kwargs.get('previewIcon', '')
        """关卡图标（相对文件路径）"""
        self.previewIconColor : Color = Color(kwargs.get('previewIconColor', '003f52'))
        """关卡图标颜色"""
        self.previewSongStart : int = kwargs.get('previewSongStart', 0)
        """歌曲预览开始时间（秒）（自然数）"""
        self.previewSongDuration : int = kwargs.get('previewSongDuration', 10)
        """歌曲预览时长（秒）（自然数）"""
        self.seizureWarning: bool = boolean(kwargs.get('seizureWarning', False))
        """光敏感性癫痫警告"""
        self.levelDesc : str = kwargs.get('levelDesc', '')
        """关卡描述"""
        self.levelTags : str = kwargs.get('levelTags', '')
        """关卡标签"""
        self.artistLinks : str = kwargs.get('artistLinks', '')
        """艺术家链接"""
        self.speedTrialAim : float | int = kwargs.get('speedTrialAim', 0)
        """飚速模式倍速目标"""
        self.difficulty : int = kwargs.get('difficulty', 1)
        """难度（1 ~ 10）"""
        self.requiredMods : List[str] = kwargs.get('requiredMods', [])
        """所需模组列表 [关卡编辑器中不可直接编辑]"""
        self.songFilename : str = kwargs.get('songFilename', '')
        """关卡音乐文件名（相对文件路径）"""
        self.bpm : float | int = kwargs.get('bpm', 100)
        """关卡初始BPM（正实数）"""
        self.volume : int = kwargs.get('volume', 100)
        """关卡音乐音量（%）"""
        self.offset : int = kwargs.get('offset', 0)
        """关卡初始时间偏移（ms）"""
        self.pitch : int = kwargs.get('pitch', 100)
        """关卡音乐音高/速度（%）"""
        self.hitsound : HITSOUND = value_to_enum(HITSOUND, kwargs.get('hitsound', HITSOUND.Kick))
        """关卡初始打拍声"""
        self.hitsoundVolume : int = kwargs.get('hitsoundVolume', 100)
        """关卡初始打拍声音量（0 ~ 100）"""
        self.countdownTicks : int = kwargs.get('countdownTicks', 4)
        """关卡开始时的滴答计数（2 ~ 12）"""
        self.trackColorType : TRACK_COLOR_TYPE = value_to_enum(TRACK_COLOR_TYPE, kwargs.get('trackColorType', TRACK_COLOR_TYPE.Single))
        """初始轨道颜色类型"""
        self.trackColor : Color = Color(kwargs.get('trackColor', 'debb7b'))
        """初始轨道颜色"""
        self.secondaryTrackColor : Color = Color(kwargs.get('secondaryTrackColor', 'ffffff'))
        """轨道二级颜色/轨道副色调"""
        self.trackColorAnimDuration : float | int = kwargs.get('trackColorAnimDuration', 2)
        """轨道颜色动画周期/色彩动画间隔（1.401298E-45 ~ 1000）"""
        self.trackColorPulse : TRACK_COLOR_PULSE = value_to_enum(TRACK_COLOR_PULSE, kwargs.get('trackColorPulse', TRACK_COLOR_PULSE.NONE))
        """轨道颜色脉冲类型"""
        self.trackPulseLength : int = kwargs.get('trackPulseLength', 10)
        """轨道颜色脉冲长度（2-1000）"""
        self.trackStyle : TRACK_STYLE = value_to_enum(TRACK_STYLE, kwargs.get('trackStyle', TRACK_STYLE.Standard))
        """初始轨道风格"""
        self.trackTexture : str = kwargs.get('trackTexture', '')
        """轨道贴图（相对文件路径）"""
        self.trackTextureScale : float | int = kwargs.get('trackTextureScale', 1)
        """轨道贴图缩放比例（1.401298E-45 ~ 1000）"""
        self.trackGlowIntensity : float | int = kwargs.get('trackGlowIntensity', 100)
        """轨道辉度（0 ~ 100）"""
        self.trackAnimation : TRACK_ANIMATION = value_to_enum(TRACK_ANIMATION, kwargs.get('trackAnimation', TRACK_ANIMATION.NONE))
        """轨道出现动画"""
        self.beatsAhead : float | int = kwargs.get('beatsAhead', 3)
        """轨道出现动画提前节拍数"""
        self.trackDisappearAnimation : TRACK_DISAPPEAR_ANIMATION = value_to_enum(TRACK_DISAPPEAR_ANIMATION, kwargs.get('trackDisappearAnimation', TRACK_DISAPPEAR_ANIMATION.NONE))
        """轨道消失动画"""
        self.beatsBehind : float | int = kwargs.get('beatsBehind', 4)
        """轨道消失动画延后节拍数"""
        self.backgroundColor : Color = Color(kwargs.get('backgroundColor', '000000'))
        """初始背景颜色"""
        self.showDefaultBGIfNoImage : bool = boolean(kwargs.get('showDefaultBGIfNoImage', True))
        """当没有背景图片时，显示默认背景 [关卡编辑器中不可直接编辑]"""
        self.showDefaultBGTile : bool = boolean(kwargs.get('showDefaultBGTile', True))
        """显示教程背景图案"""
        self.defaultBGTileColor : Color = Color(kwargs.get('defaultBGTileColor', '101121ff'))
        """教程背景图案颜色"""
        self.defaultBGShapeType : DEFAULT_BG_SHAPE_TYPE = value_to_enum(DEFAULT_BG_SHAPE_TYPE, kwargs.get('defaultBGShapeType', DEFAULT_BG_SHAPE_TYPE.Default))
        """教程背景图形"""
        self.defaultBGShapeColor : Color = Color(kwargs.get('defaultBGShapeColor', 'ffffff'))
        """教程背景图形填色"""
        self.bgImage : str = kwargs.get('bgImage', '')
        """背景图片（相对文件路径）"""
        self.bgImageColor : Color = Color(kwargs.get('bgImageColor', 'ffffff'))
        """背景图片颜色"""
        self.parallax : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('parallax', (100, 100)))
        """背景图片平行"""
        self.bgDisplayMode : BG_DISPLAY_MODE = value_to_enum(BG_DISPLAY_MODE, kwargs.get('bgDisplayMode', BG_DISPLAY_MODE.FitToScreen))
        """背景图片显示模式"""
        self.imageSmoothing : bool = boolean(kwargs.get('imageSmoothing', True))
        """背景图片图像平滑"""
        self.lockRot : bool = boolean(kwargs.get('lockRot', False))
        """背景图片旋转锁定"""
        self.loopBG : bool = boolean(kwargs.get('loopBG', False))
        """背景图片循环背景"""
        self.scalingRatio : int = kwargs.get('scalingRatio', 100)
        """背景图片缩放比例（1-1000）"""
        self.relativeTo : CAMERA_RELATIVE = value_to_enum(CAMERA_RELATIVE, kwargs.get('relativeTo', ), CAMERA_RELATIVE.LastPosition)
        """初始摄像头相对于"""
        self.position : Data_Pair.XY_Pair = Data_Pair.XY_Pair.from_tuple(kwargs.get('position', (0, 0)))
        """初始摄像头位置"""
        self.rotation : float | int = kwargs.get('rotation', 0)
        """初始摄像头角度"""
        self.zoom : float | int = kwargs.get('zoom', 100)
        """初始摄像头缩放"""
        self.pulseOnFloor : bool = boolean(kwargs.get('pulseOnFloor', True))
        """触发方块时摄像头脉动"""
        self.bgVideo : str = kwargs.get('bgVideo', '')
        """背景视频（相对文件路径）"""
        self.loopVideo : bool = boolean(kwargs.get('loopVideo', False))
        """背景视频循环"""
        self.vidOffset : int = kwargs.get('vidOffset', 0)
        """背景视频偏移"""
        self.floorIconOutlines : bool = boolean(kwargs.get('floorIconOutlines', False))
        """方块图标描边"""
        self.stickToFloors : bool = boolean(kwargs.get('stickToFloors', True))
        """黏性方块"""
        self.planetEase : EASE = value_to_enum(EASE, kwargs.get('planetEase', EASE.Linear))
        """初始星球缓速"""
        self.planetEaseParts: int = kwargs.get('planetEaseParts', 1)
        """初始星球缓速分段（正整数）"""
        self.planetEasePartBehavior : EASE_PART_BEHAVIOR = value_to_enum(EASE_PART_BEHAVIOR, kwargs.get('planetEasePartBehavior', EASE_PART_BEHAVIOR.Mirror))
        """初始星球缓速分段行为"""
        self.defaultTextColor : Color = Color(kwargs.get('defaultTextColor', 'ffffff'))
        """默认文本颜色"""
        self.defaultTextShadowColor : Color = Color(kwargs.get('defaultTextShadowColor', '00000050'))
        """默认文本阴影颜色"""
        self.congratsText : str = kwargs.get('congratsText', '')
        """通关恭喜文本"""
        self.perfectText : str = kwargs.get('perfectText', '')
        """完美无瑕文本"""
        self.legacyFlash : bool = boolean(kwargs.get('legacyFlash', False))
        """旧版闪光 [关卡编辑器中不可直接编辑]"""
        self.legacyCamRelativeTo : bool = boolean(kwargs.get('legacyCamRelativeTo', False))
        """旧版摄像头相对于 [关卡编辑器中不可直接编辑]"""
        self.legacySpriteTiles : bool = boolean(kwargs.get('legacySpriteTiles', False))
        """旧版精灵方块 [关卡编辑器中不可直接编辑]"""
        self.legacyTween : bool = boolean(kwargs.get('legacyTween', True))
        """旧版Tween [关卡编辑器中不可直接编辑]"""
        self.disableV15Features : bool = boolean(kwargs.get('disableV15Features', False))
        """禁用新版编辑器功能"""
    
    @property
    def value(self) -> dict:
        d = {}
        for key, value in self.__dict__.items():
            if isinstance(value, Enum | Data_Pair | Color):
                d[key] = value.value
            else:
                d[key] = value
        return d
            
