import tkinter as tk
from pytube import YouTube

root = tk.Tk()
root.geometry("300x300")
root.title("Youtube Downloader")
root.configure(bg="#14b6e2")
# youtube_icon = tk.PhotoImage(file = 'youtube.png')
# root.iconphoto(False, youtube_icon)
root.iconbitmap("C:/Users/netwo/Desktop/youtube_downloader/youtube_icon.ico")

def download_youtube_video(link_to_video, name_for_video):
	YouTube(link_to_video).streams.get_highest_resolution().download(filename=f"{name_for_video}.mp4", output_path="videos")

tk.Label(root, text="YouTube Video Link", bg="#14b6e2").place(relx=.5, rely=.1,anchor= tk.CENTER)
tk.Label(root, text="Video Name", bg="#14b6e2").place(relx=.5, rely=.3,anchor= tk.CENTER)

youtube_download_input = tk.Entry(root)
video_name_input = tk.Entry(root)

youtube_download_input.place(width=270, relx=.5, rely=.2,anchor= tk.CENTER)
video_name_input.place(width=270, relx=.5, rely=.4,anchor= tk.CENTER)

def on_click(text):
	link_to_video = youtube_download_input.get()
	name_for_video = video_name_input.get()
	download_youtube_video(link_to_video, name_for_video)
    # answer.config(text= "Downloading...")

download_button = tk.Button(width = 16, height=5, text= "Download", bg="#1fc72a", command = lambda:on_click("text"))
download_button.place(relx=.5, rely=.6,anchor= tk.CENTER)

# add a feature which displays downloading text and goes away when downloaded
# add threading to make it work
# make the gui widgets pretty
# answer = tk.Label(root, text = "")
# answer.place(relx=.5, rely=.7,anchor= tk.CENTER)
# handle errors of download button with no entries in command line
# ask how to make filename optional in the program
# think about making a folder and downloading all the videos there
# make about page


exit_button = tk.Button(width = 16, height=3, text= "Exit", bg="#e23e1e", command = lambda: root.destroy())
exit_button.place(relx=.5, rely=.9,anchor= tk.CENTER)


root.mainloop()
