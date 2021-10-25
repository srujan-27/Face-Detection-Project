import os
import tkinter
from tkinter import*



top=tkinter.Tk()

def helloCallBack():
    os.system('facedet.py')
def goo():
    os.system('photo.py')

B=tkinter.Button(top,bg="red",text="Cam Det",command= helloCallBack)
C=tkinter.Button(top,bg="red",text="Img Det",command= goo)

B.pack()
C.pack()

top.mainloop()
