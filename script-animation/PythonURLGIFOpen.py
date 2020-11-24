# Programmer: Christian Winds
# Program Name: PythonURLGIFOpen
# Description: This program is intended to open a GIF from a provided URL.

import tkinter

# Code by Keith Hall and noob oddy from Stack Overflow, https://stackoverflow.com/questions/7960600/python-tkinter-display-animated-gif-using-pil
# Accessed Monday, November 23rd, 2020

from tkinter import * 
from PIL import Image, ImageTk


class MyLabel(Label):
    def __init__(self, master, filename):
        im = Image.open(filename)
        seq =  []
        try:
            while 1:
                seq.append(im.copy())
                im.seek(len(seq)) # skip to next frame
        except EOFError:
            pass # we're done

        try:
            self.delay = im.info['duration']
        except KeyError:
            self.delay = 100

        first = seq[0].convert('RGBA')
        self.frames = [ImageTk.PhotoImage(first)]

        Label.__init__(self, master, image=self.frames[0])

        temp = seq[0]
        for image in seq[1:]:
            temp.paste(image)
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))

        self.idx = 0

        self.cancel = self.after(self.delay, self.play)

    def play(self):
        self.config(image=self.frames[self.idx])
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0
        self.cancel = self.after(self.delay, self.play)        


root = Tk()
anim = MyLabel(root, '8650-bishun.gif')
anim.pack()

def stop_it():
    anim.after_cancel(anim.cancel)

Button(root, text='stop', command=stop_it).pack()

root.mainloop()