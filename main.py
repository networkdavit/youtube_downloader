import tkinter as tk
from pytube import YouTube
import threading

root = tk.Tk()

root_w = 300 # width for the Tk root
root_h = 300 # height for the Tk root

# get screen width and height
root_ws = root.winfo_screenwidth() # width of the screen
root_hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
root_x = (root_ws/2) - (root_w/2)
root_y = (root_hs/2) - (root_h/2)


root.geometry('%dx%d+%d+%d' % (root_w, root_h, root_x, root_y))
root.title("Youtube Downloader")
root.configure(bg="#14b6e2")
root.iconbitmap("C:/Users/netwo/Desktop/youtube_downloader/youtube_icon.ico")
link_to_video = ""
name_for_video = ""


def download_youtube_video(link_to_video, name_for_video):
	link_to_video = youtube_download_input.get()
	name_for_video = video_name_input.get()
	top= tk.Toplevel(root)

	top_w = 350 
	top_h = 100 

	top_ws = top.winfo_screenwidth() 
	top_hs = top.winfo_screenheight() 

	top_x = (top_ws/2) - (top_w/2)
	top_y = (top_hs/2) - (top_h/2)

	top.geometry('%dx%d+%d+%d' % (top_w, top_h, top_x, top_y))
	top.title("Youtube Downloader")
	top.configure(bg="#14b6e2")
	top.iconbitmap("C:/Users/netwo/Desktop/youtube_downloader/youtube_icon.ico")
	tk.Label(top, text= "Downloading...", font=('Mistral 18 bold')).place(relx=.5, rely=.2,anchor= tk.CENTER)
	YouTube(link_to_video).streams.get_highest_resolution().download(filename=f"{name_for_video}.mp4", output_path="videos")
	tk.Label(top, text= "Download complete!", font=('Mistral 18 bold')).place(relx=.5, rely=.2,anchor= tk.CENTER)
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

download_button = tk.Button(width = 16, height=1, text= "Download", bg="#1fc72a", command = lambda: thread_download_button(link_to_video, name_for_video))
download_button.place(relx=.5, rely=.5,anchor= tk.CENTER)

about_button = tk.Button(width = 16, height=1, text= "About", bg="#dfb026")
about_button.place(relx=.5, rely=.6,anchor= tk.CENTER)

exit_button = tk.Button(width = 16, height=1, text= "Exit", bg="#e23e1e", command = lambda: root.destroy())
exit_button.place(relx=.5, rely=.7,anchor= tk.CENTER)

root.mainloop()
