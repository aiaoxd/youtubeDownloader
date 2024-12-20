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

## 视频教程
```bash
https://www.bilibili.com/video/BV13KkmYYEpq
```
