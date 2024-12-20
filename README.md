# YouTube 视频下载器

这是一个使用 Python 编写的简单的 YouTube 视频下载器，利用 `yt-dlp` 库来下载视频。该脚本会自动选择最清晰的视频格式（根据文件大小和分辨率）并下载。

## 功能

- 输入 YouTube 视频 URL
- 自动选择文件大小最大且分辨率最高的视频格式进行下载
- 显示下载进度

## 激活虚拟环境(可选)
在项目根目录下运行以下命令,例如
对于 macOS 或 Linux，运行：
```bash
cd 你的下载目录/youtubeDownloader-main
```
对于 Windows，运行：
```bash
cd 你的下载目录/youtubeDownloader-main
```
创建虚拟环境
```bash
python3 -m venv venv
```
对于 macOS 或 Linux，运行：
```bash
source venv/bin/activate
```
对于 Windows，运行：
```bash
venv\Scripts\activate
```

## 安装依赖

在项目根目录下运行以下命令安装所有必需的 Python 包：

```bash
pip install -r requirements.txt
```

## 运行
```bash
python youtubeDownloader.py
```
按照提示 输入目标网址即可

## 退出
```bash
deactivate
```
## 示例输出
```bash
欢迎使用 YouTube 下载器
请输入有效的 YouTube 视频 URL: https://www.youtube.com/watch?v=example_video_id
视频标题: Example Video
可选质量:
1. 1080p - 150.25 MB
2. 720p - 90.12 MB
正在下载 1080p - 150.25 MB 格式...
下载进度: 25.50%
下载进度: 50.00%
下载进度: 75.00%
下载进度: 100.00%
下载完成！
```
## 注意事项
```bash
请确保视频链接是有效的，且该视频可以在你所在的地区观看。
视频下载过程中需要一定的网络带宽和时间，取决于视频的大小和网络速度。
本项目仅用于个人学习和研究，使用时请遵循相关法律法规，尊重版权。
```


## 视频教程
```bash
https://www.bilibili.com/video/BV13KkmYYEpq
```
