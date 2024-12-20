# YouTube 视频下载器

这是一个使用 Python 编写的简单的 YouTube 视频下载器，利用 `yt-dlp` 库来下载视频。该脚本会自动选择最清晰的视频格式（根据文件大小和分辨率）并下载。

## 功能

- 输入 YouTube 视频 URL
- 自动选择文件大小最大且分辨率最高的视频格式进行下载
- 显示下载进度

## 安装依赖

1. 确保你已经安装了 [Python](https://www.python.org/downloads/)，建议使用 Python 3.6 及以上版本。
2. 安装依赖库，运行以下命令：

   ```bash
   pip install -r requirements.txt
