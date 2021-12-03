import tkinter as tk
from pytube import YouTube
import threading

root = tk.Tk()
root.geometry("300x300")
root.title("Youtube Downloader")
root.configure(bg="#14b6e2")
root.iconbitmap("C:/Users/netwo/Desktop/youtube_downloader/youtube_icon.ico")
link_to_video = ""
name_for_video = ""

# changing message works, but only when the updated message is longer
# make the gui widgets pretty
# handle errors of download button with no entries in command line
# ask how to make filename optional in the program
# make about page

def download_youtube_video(link_to_video, name_for_video):
	link_to_video = youtube_download_input.get()
	name_for_video = video_name_input.get()
	top= tk.Toplevel(root)
	top.geometry("350x100")
	top.title("Youtube Downloader")
	tk.Label(top, text= "Downloading...", font=('Mistral 18 bold')).place(relx=.5, rely=.1,anchor= tk.CENTER)
	YouTube(link_to_video).streams.get_highest_resolution().download(filename=f"{name_for_video}.mp4", output_path="videos")
	tk.Label(top, text= "Download complete!", font=('Mistral 18 bold')).place(relx=.5, rely=.1,anchor= tk.CENTER)
	close_downloaded_popup = tk.Button(top, width = 16, height=3, text= "Back", bg="#e23e1e", command = lambda: top.destroy())
	close_downloaded_popup.place(relx=.5, rely=.7,anchor= tk.CENTER)

def thread_download_button(link_to_video, name_for_video):
	threading.Thread(target=download_youtube_video, args=(link_to_video, name_for_video)).start()


tk.Label(root, text="YouTube Video Link", bg="#14b6e2").place(relx=.5, rely=.1,anchor= tk.CENTER)
tk.Label(root, text="Video Name", bg="#14b6e2").place(relx=.5, rely=.3,anchor= tk.CENTER)

youtube_download_input = tk.Entry(root)
video_name_input = tk.Entry(root)

youtube_download_input.place(width=270, relx=.5, rely=.2,anchor= tk.CENTER)
video_name_input.place(width=270, relx=.5, rely=.4,anchor= tk.CENTER)

download_button = tk.Button(width = 16, height=5, text= "Download", bg="#1fc72a", command = lambda: thread_download_button(link_to_video, name_for_video))
download_button.place(relx=.5, rely=.6,anchor= tk.CENTER)

exit_button = tk.Button(width = 16, height=3, text= "Exit", bg="#e23e1e", command = lambda: root.destroy())
exit_button.place(relx=.5, rely=.9,anchor= tk.CENTER)

root.mainloop()
