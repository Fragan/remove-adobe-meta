#!/bin/python


import subprocess
import sys
if sys.platform == 'linux':
  print("Found Linux distribution -")
  from tkinter import *
  import tkinter as tk
  import tkinter.filedialog as fd
elif sys.platform == 'darwin':
  print("Found Mac OSX distribution -")
  from Tkinter import *
  import Tkinter as tk
  import tkFileDialog as fd


class Interface(Frame):
     
     
  def __init__(self, frame, **kwargs):
    Frame.__init__(self, frame, width=768, height=576, **kwargs)
    self.pack()

    # layout
    self.browse_panel = Frame(self)
    # show panel
    self.browse_panel.pack()

    # text field
    self.path_txt = StringVar()
    self.txt_line = Entry(self.browse_panel, textvariable=self.path_txt, width=90)
    self.txt_line.pack(padx=5, pady=20, side=LEFT)

    self.browse_btn = Button(self.browse_panel, text="Browse", command=self.browse)
    self.browse_btn.pack(padx=5, pady=10, side=RIGHT)


    self.button_panel = Frame(self)
    self.button_panel.pack()


    self.exit_btn = Button(self.button_panel, text="Exit", command=self.quit)
    self.exit_btn.pack(padx=5, pady=20, side=LEFT)

    self.clean_btn = Button(self.button_panel, text="Clean", command=self.clean)
    self.clean_btn.pack(padx=5, pady=20, side=RIGHT)



  def clean(self):
    # tester directory.exist()
    subprocess.call(['remove-adobe-meta.sh', self.path_txt.get()])

  def browse(self):
    self.path = fd.askdirectory(title="Select a directory")
    self.txt_line.insert(0, self.path)



###########################
# Launch the maine frame
###########################

frame = Tk()
# frame's title
frame.wm_title("Removal Tool for Adobe's metadata")
interface = Interface(frame)

# show view
interface.mainloop()
interface.destroy()

