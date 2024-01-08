from tkinter import *
from PIL import ImageTk,Image
#upper wala module image ko resioze and load karne ka liye
import os

def rotate_image():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])
    # //counter%len(img_array) yeh loop ma calte rahe photo ishliye h
    counter = counter + 1
    print("ram ram ji",counter)


counter = 1
root = Tk()
root.title('Wallpaper Viewer')

root.geometry('350x400')
root.configure(background='black')

files = os.listdir('2project/wallpapers')

img_array = []
for file in files:
    img = Image.open(os.path.join('2project/wallpapers',file))
    resized_img = img.resize((200,300))
    img_array.append(ImageTk.PhotoImage(resized_img))

img_label = Label(root,image=img_array[0])
img_label.pack(pady=(15,10))

next_btn = Button(root,text='Next',bg='white',fg='black',width=28,height=2,command=rotate_image)
next_btn.pack()
root.mainloop()