from pytube import YouTube
from main import link_to_video, name_for_video

# link = input("Please specify the link: ")
# video_name = input("Please name the video: ")

def download_youtube_video(link_to_video, name_for_video):
	YouTube(link_to_video).streams.get_highest_resolution().download(filename=f"{name_for_video}.mp4")

