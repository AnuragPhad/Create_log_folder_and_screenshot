from tkinter import *
import os
import shutil
import time
import pyautogui


master = Tk()
master.title("Game Data")
master.geometry('800x200')

Src_path = "C:\\logs\\Game"
options = os.listdir(Src_path)

if os.path.exists("C:\\Log_File_Autoamted"):
    print("path already present")
else:
    os.mkdir("C:\\Log_File_Autoamted")


if os.path.exists("C:\\Log_File_Autoamted\\Gamedata"):
    print("path already present")
else:
    os.mkdir("C:\\Log_File_Autoamted\\Gamedata")

def show():
    Label(text=clicked.get()).grid(row=4,column=0)
    return clicked.get()




clicked = StringVar()
clicked.set(" ")
drop = OptionMenu(master, clicked, *options)
drop.grid(row=0,column=0)



def copy_Folder(src,dest):
    for item in os.listdir(src):
        s=os.path.join(src,item)
        d=os.path.join(dest,item)
        if os.path.isdir(s):
            shutil.copytree(s,d)
        else:
            shutil.copy2(s,d)



def Save_log_File():
    image = pyautogui.screenshot()



    print(show())
    time.sleep(0.5)
    Src_path_1 = "C:\\logs\\Game\\{0}".format(show())
    Dest_path="C:\\Log_File_Autoamted\\Gamedata\\{0}-{1}".format(show(),int(time.time()))
    os.mkdir(Dest_path)
    image.save('C:/Log_File_Autoamted//Gamedata/{0}-{1}.png'.format(show(),int(time.time())))



    if os.path.exists(Src_path_1):
        copy_Folder(Src_path_1, Dest_path)

    shutil.make_archive("{0}-{1}".format(show(),int(time.time())), "zip",root_dir='c:/Log_File_Autoamted')

    master.destroy()


B1=Button(master,text="Start",command=Save_log_File)
B1.grid(row=2,column=0,padx=400)




master.mainloop()