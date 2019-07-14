## 无法运行一些老旧程序
方案：右键>属性>以兼容模式运行
## 优酷.kux转.mp4
优酷安装文件夹内有ffmpeg.exe，按照ffmpeg用法重新封装成mp4即可。

附：优酷不给力的探索过程

- 杀掉Youku Desktop重新启动优酷
- 注销后重新启动优酷
- 在火绒中恢复优酷自启动
- 打开安装包，并没有修复功能
- 重装优酷
- 在优酷安装文件夹中漫步，找到NPlayer.exe，双击打不开，将.kux视频拖在其上，打开成功

## 为.kux文件注册打开方式

- 写`KuxConverter.py`，接收命令行参数，调用`ffmpeg`转成mp4，然后用默认应用（`PotPlayer`）打开。
- 在注册表`HKEY_CLASSES_ROOT`中
    - PyKux
		- DefaultIcon
		- shell
		    - open
				- command
    - .kux
- 其中`PyKux`项仿照`Python.File`填写，`.kux`项仿照`.mp4`填写

## FFMpeg 下载 m3u8

方便快捷，一行到位！

```shell
ffmpeg -i "https://zuikzy.603ee.com/2019/05/01/irlmX9Oasv3yhzR4/playlist.m3u8" example.mp4
```

