#!/usr/bin/python2
#filename is tkinter002.py

import Tkinter 

from tkMessageBox import showinfo

def reply():
        showinfo(title = 'popup',message = 'Button pressed!')

window = Tkinter.Tk()
button = Tkinter.Button(window,text = 'press', command = reply)
button.pack()
window.mainloop()

