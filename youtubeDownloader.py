import os
import yt_dlp as youtube_dl
import sys

# 选择下载路径
def select_download_path():
    download_path = input("请输入下载路径 (默认是桌面): ")
    if not download_path:
        download_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    if not os.path.exists(download_path):
        print(f"路径不存在: {download_path}")
        sys.exit(1)
    return download_path


# 显示下载进度
def show_progress(d):
    if d['status'] == 'downloading':
        downloaded = d.get('downloaded_bytes', 0)
        total = d.get('total_bytes', 1)
        percentage = downloaded / total * 100
        print(f"下载进度: {percentage:.2f}%")


# 获取视频信息并展示
def load_video_info(url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'noplaylist': True,
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)

            title = info_dict.get('title', '视频')
            formats = info_dict.get('formats', [])
            subtitles = info_dict.get('subtitles', {})

            # 如果没有合适的格式，退出
            if not formats:
                print("没有找到可下载的视频格式。")
                sys.exit(1)

            return title, formats, subtitles

    except Exception as e:
        print(f"加载视频信息出错: {e}")
        sys.exit(1)

# 筛选并选择filesize最大的视频格式
def select_best_format(formats):
    # 筛选出同时包含filesize和height的格式
    valid_formats = [fmt for fmt in formats if 'filesize' in fmt and 'height' in fmt]

    # 如果没有合适的格式，退出
    if not valid_formats:
        print("没有找到合适的视频格式。")
        sys.exit(1)

    # 根据filesize排序，选择最大的视频格式
    best_format = max(valid_formats, key=lambda x: x['filesize'])
    return best_format
# 下载视频
def download_video(formats, selected_quality_index, url):
    selected_format = select_best_format(formats)

    if 'height' in selected_format and 'filesize' in selected_format:
        quality_text = f"{selected_format['height']}p - {selected_format['filesize'] / 1024 / 1024:.2f} MB"
    elif 'filesize' in selected_format:  # 可能是音频
        quality_text = f"音频 - {selected_format['filesize'] / 1024 / 1024:.2f} MB"
    else:
        print("选择的格式不包含有效的质量信息")
        return

    print(f"正在下载 {quality_text} 格式...")

    # 使用 youtube-dl 进行下载操作，确保选中合适的格式。
    # ydl_opts = {'format': selected_format['format_id'], 'progress_hooks': [show_progress]}
    ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # 下载最佳视频和音频并合并
            'postprocessors': [{  # 使用后处理器将音频和视频合并成 MP4 格式
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',  # 强制转换为 mp4 格式
            }],
            'progress_hooks': [self.show_progress],  # 显示进度
            'quiet': False,  # 显示更多信息
        }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


# 主函数
def main():
    print("欢迎使用 YouTube 下载器")

    # 获取并验证视频URL
    url = ''
    while not url.startswith('https://www.youtube.com/watch'):
        url = input("请输入有效的 YouTube 视频 URL: ")
        if not url.startswith('https://www.youtube.com/watch'):
            print("输入无效，请输入有效的 YouTube 视频 URL。")

    # 使用 youtube_dl 获取视频信息
    title, formats, subtitles = load_video_info(url)

    # 选择最清晰的视频格式 (即formats列表中的第一个)
    selected_quality_index = len(formats) - 1  # 默认选择最清晰的画质

    # 下载视频
    download_video(formats, selected_quality_index, url)


if __name__ == "__main__":
    main()
