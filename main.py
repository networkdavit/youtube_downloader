import tkinter as tk
from pytube import YouTube
import threading

root = tk.Tk()
root.geometry("300x300")
root.title("Youtube Downloader")
root.configure(bg="#14b6e2")
# youtube_icon = tk.PhotoImage(file = 'youtube.png')
# root.iconphoto(False, youtube_icon)
root.iconbitmap("C:/Users/netwo/Desktop/youtube_downloader/youtube_icon.ico")
link_to_video = ""
name_for_video = ""
def download_youtube_video(link_to_video, name_for_video):
	link_to_video = youtube_download_input.get()
	name_for_video = video_name_input.get()
	YouTube(link_to_video).streams.get_highest_resolution().download(filename=f"{name_for_video}.mp4", output_path="videos")
	# answer.config(text= "Your tweet has been posted!")
	# downloaded_message_popup()
	top= tk.Toplevel(root)
	top.geometry("350x100")
	top.title("Youtube Downloader")
	tk.Label(top, text= "Download complete!", font=('Mistral 18 bold')).place(relx=.5, rely=.1,anchor= tk.CENTER)
	close_downloaded_popup = tk.Button(top, width = 16, height=3, text= "Back", bg="#e23e1e", command = lambda: top.destroy())
	close_downloaded_popup.place(relx=.5, rely=.7,anchor= tk.CENTER)

def thread_download_button(link_to_video, name_for_video):
	# print(link_to_video)
	threading.Thread(target=download_youtube_video, args=(link_to_video, name_for_video)).start()

def downloaded_message_popup():
   top= Toplevel(root)
   top.geometry("100x500")
   top.title("Child Window")
   Label(top, text= "Hello World!", font=('Mistral 18 bold')).place(x=150,y=80)

def downloading_message():
	top= tk.Toplevel(root)
	top.geometry("350x100")
	top.title("Youtube Downloader")
	tk.Label(top, text= "Downloading, please wait", font=('Mistral 18 bold')).place(relx=.5, rely=.1,anchor= tk.CENTER)
	top.after(5000, top.destroy)
	#it works for now, but try to make the window close when downloaded message is popped up.



tk.Label(root, text="YouTube Video Link", bg="#14b6e2").place(relx=.5, rely=.1,anchor= tk.CENTER)
tk.Label(root, text="Video Name", bg="#14b6e2").place(relx=.5, rely=.3,anchor= tk.CENTER)



youtube_download_input = tk.Entry(root)
video_name_input = tk.Entry(root)

youtube_download_input.place(width=270, relx=.5, rely=.2,anchor= tk.CENTER)
video_name_input.place(width=270, relx=.5, rely=.4,anchor= tk.CENTER)

download_button = tk.Button(width = 16, height=5, text= "Download", bg="#1fc72a", command = lambda: [thread_download_button(link_to_video, name_for_video), downloading_message()])
download_button.place(relx=.5, rely=.6,anchor= tk.CENTER)

# answer = tk.Label(root, text = "")
# answer.grid(row = 7, column = 0, )

# add a feature which displays downloading text and goes away when downloaded
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
