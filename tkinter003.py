#!/usr/bin/env python2
import Tkinter

top = Tkinter.Tk()
quit = Tkinter.Button(top, text='Hello World!',
command=top.quit)
quit.pack()
Tkinter.mainloop()
