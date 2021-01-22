from tkinter import * 
from tkinter.ttk import * 
import os
from art import *
import webbrowser
from platform import system
import json 
import pprint
import tkinter.messagebox

# FRAME

root = Tk()
root.geometry("600x600")
frame = Frame(root)
frame.pack()
  
frame = Frame(root)
frame.pack(side = BOTTOM)

platformD = system()

if platformD == 'Windows':
    root.iconbitmap(default='images/2.ico')
    image = PhotoImage(file='images/1.png') 
    
else: 
    root.iconbitmap(os.path.dirname(os.path.abspath(__file__))+'/images/2.ico')
    image = PhotoImage(os.path.dirname(os.path.abspath(__file__))+'/images/1.png')

label = Label(root, image = image)
label.pack(side= TOP)
root.title("LBRY TOOLS")
tprint("\nLBRY TOOLS","rnd-medium")

# FUNCTIONS

def list_tips ():
    if platformD == 'Windows':
        os.system('cmd /c "lbrynet txo spend --type=support --is_not_my_input --preview --include_full_tx"')
    else:
        os.system('./lbrynet txo spend --type=support --is_not_my_input --preview --include_full_tx')
def unlock_tips():
    tkinter.messagebox.showinfo('Be Careful', 'It will Reduce Your Claims Discoverability, enter to Continue')
    
    if platformD == 'Windows':
        os.system('cmd /c "lbrynet txo spend --type=support --is_not_my_input"')
        os.system('python matrix.py')
    else:
        os.system('./lbrynet txo spend --type=support --is_not_my_input')
        os.system('python3 matrix.py')
def vanity():
    if platformD == 'Windows':
        os.system('cmd /c "python vanity.py"')
    else:
        os.system('python3 vanity.py') 
def seed():
    if platformD == 'Windows':
        os.system('cmd /c "python seed.py"') 
    else:
        os.system('python3 seed.py') 
def ratio():
    if platformD == 'Windows':
        os.system('cmd /c "python ratio.py"')
    else:
        os.system('python3 ratio.py')
def lbryup():
    if platformD == 'Windows':
        os.system('cd lbryup && python lbryup2.py')
        
    else:
        os.system('cd lbryup && python3 lbryup2.py')      
def lbrynomics():
    webbrowser.open_new(r"http://www.lbrynomics.com")
def coindodo():
    webbrowser.open_new(r"https://coindodo.io/lbry")
def whalebot():
    webbrowser.open_new(r"https://lbrywhale.herokuapp.com/")
def foundation():
    webbrowser.open_new(r"http://chat.lbry.org")
def lbctoday():
    webbrowser.open_new(r"https://chrome.google.com/webstore/detail/lbc-today/ealgadmpgaefckfpclemccenfkjihedn")
def watch_on_lbry():
    webbrowser.open_new(r"https://chrome.google.com/webstore/search/whatch%20on%20lbry%20")
def dump():
    if platformD == 'Windows':
        os.system('cd lbrydump && cmd /c start LBRYMeta-Win-x64')
        
    else:
        os.system('cd lbrydump && start LBRYMeta-Linux-x64')   
    
# BUTTONS
style = Style() 
style.configure('W.TButton', font =
               ('calibri', 10, 'bold', 'underline'), 
                foreground = 'red') 
  
button1 = Button(frame, text = "List Tips",width = 560, command = list_tips)
button1.pack(padx = 3, pady = 3)
button2 = Button(frame, text = "Unlock ALL Tips",style = 'W.TButton',width = 560, command= unlock_tips)
button2.pack(padx = 3, pady = 3)
button3 = Button(frame, text = "Check Vanity Names",width = 560, command = vanity)
button3.pack(padx = 3, pady = 3)
button4 = Button(frame, text = "Seeding Ratio",width = 560, command = ratio)
button4.pack(padx = 3, pady = 3)
button5 = Button(frame, text = "Seed Channels",width = 560, command = seed)
button5.pack(padx = 3, pady = 3)
button13 = Button(frame,text="LBRY Dump", width=560 , command = dump)
button13.pack(padx=3, pady =3)
button6 = Button(frame, text = "LBRY Uploader",width = 560, command = lbryup)
button6.pack(padx = 3, pady = 3)
button11 = Button(frame,text="LBC today", width=560 , command = lbctoday)
button11.pack(padx=3, pady =3)
button12 = Button(frame,text="Watch on LBRY", width=560 , command = watch_on_lbry)
button12.pack(padx=3, pady =3)
label = Label(frame, text = "Great Websites and Communities", foreground = 'green')
label.pack()
button7 = Button(frame, text = "LBRYnomics",width = 560, command = lbrynomics)
button7.pack(padx = 3, pady = 3)
button8 = Button(frame, text = "Coindodo",width = 560, command = coindodo)
button8.pack(padx = 3, pady = 3)
button9 = Button(frame, text = "WhaleBot",width = 560,command = whalebot)
button9.pack(padx = 3, pady = 3)  
button10 = Button(frame, text = "Foundation Server",width = 560, command = foundation)
button10.pack(padx = 3, pady = 3)


root.mainloop()
