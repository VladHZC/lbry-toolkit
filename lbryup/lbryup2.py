from tkinter import *
import os 
import requests

root = Tk()
# width and height variables
can_width = 300
can_height = 400
root.geometry(f"{can_width}x{can_height}")
root.title("Event handling")
# video weblink 
video_entry = Entry(root, width =40)
video_entry.insert(0, "Insert video Link")
video_entry.pack()
video_url= ""
# lbryname
name_entry = Entry(root,width =40)
name_entry.insert(0, "Insert Lbry Name")
name_entry.pack()
name = ""
# post title
title_entry = Entry(root,width= 40)
title_entry.insert(0, "Insert Post Title")
title_entry.pack()
title =""
# thumbnail entry 
thumb_entry = Entry(root , width =40)
thumb_entry.insert(0, "Insert Thumbnail URL")
thumb_entry.pack()
# Bid Entry
bid_entry = Entry(root , width=40 )
bid_entry.insert(0, "Enter Bid Value")
bid_entry.pack()
# Tag selection
tags_entry = Entry(root , width =40)
tags_entry.insert(0 ,'Insert TAGS (Use comma to separate tags)')
tags_entry.pack()
# ChannelId Entry
channel_entry = Entry(root , width = 40)
channel_entry.insert(0, 'Insert Channel Claim ID')
channel_entry.pack()
channel_id=""
def Click():
    global video_url
    video_url = str(video_entry.get())
    Label(root, text=video_url).pack()
    global name 
    name =  str(name_entry.get())
    Label(root, text = name).pack()
    global title
    title = str(title_entry.get())
    global thumbnail_url
    thumbnail_url = str(thumb_entry.get())
    global bid
    bid = str(bid_entry.get())
    global tags
    tags = tags_entry.split(',')
    global channel_id
    channel_id = str(channel_entry.get())

win = Button(root, text="OK", command = Click)

win.pack()
global download_path
download_path = os.getcwd()
global file_path
file_path = os.path.join(download_path, "video.mkv")
audio_answer=""
audio_= IntVar()
def audio():
    if audio_.get() == 1:
        global audio_answer
        audio_answer = "--extract-audio --audio-format mp3"
        Label(root, text=audio_answer).pack()
        file_path = os.path.join(download_path, "video.mp3")
        Label(root, text=file_path).pack()
    else:
        audio_answer = ""
        Label(root, text=audio_answer).pack()
        file_path = os.path.join(download_path, "video.mp4")
        Label(root, text=file_path).pack()
audiobtn =Checkbutton(root, text="audio only", variable =audio_, command = audio)
audiobtn.pack()
        
def download(): 

    download_path = os.getcwd()
    stringa = f'youtube-dl -22 {video_url} -o "video.%(ext)s" {audio_answer}'
    os.system(stringa)
    channel_account_id = channel_id                 
    
    return_stream_create = requests.post("http://localhost:5279",
                    json={"method": "stream_create",
                        "params": {"name": name,
                                    "title": title,
                                    "bid": bid,
                                    "file_path": file_path,
                                    "validate_file": False, 
                                    "optimize_file": True, 
                                    "tags": tags,
                                    "languages": [], 
                                    "locations": [],
                                    "channel_id": channel_id,
                                    "channel_account_id": "",
                                    "funding_account_ids": [],
                                    "preview": False,
                                    "thumbnail_url": thumbnail_url,
                                    "blocking": False}}).json()
    print(return_stream_create)    

download_btn = Button(root , text="Upload" ,command = download)
download_btn.pack()

root.mainloop()
