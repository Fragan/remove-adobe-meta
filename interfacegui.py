#!/usr/bin/python3


import sys
print(sys.version)


if sys.version_info[0] < 3:
  print("This script requires Python version 3.x")
  sys.exit(1)




import subprocess
# import sys
# if sys.platform == 'linux': # it's for python 3.x
#   print("Found Linux distribution -")
from tkinter import *
import tkinter as tk
import tkinter.filedialog as fd
# elif sys.platform == 'darwin': # it's for python 2.7.x
#   print("Found Mac OSX distribution -")
#   from Tkinter import *
#   import Tkinter as tk
#   import tkFileDialog as fd


class Interface(Frame):
     
     
  def __init__(self, frame, **kwargs):
    Frame.__init__(self, frame, width=768, height=576, **kwargs)
    self.pack(fill="both", expand=True)
    # ensure a consistent GUI size
    self.grid_propagate(False)
    # implement stretchability
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)

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


    self.console = Text(self, height=40, width=110, borderwidth=3, relief="sunken")
    self.console.config(font=("consolas", 12), undo=True, wrap='word')
    self.console.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
    self.console.pack()

    self.scrollb = Scrollbar(self, command=self.console.yview)
    self.scrollb.grid(row=0, column=1, sticky='nsew')
    self.console['yscrollcommand'] = self.scrollb.set
    





  def clean(self):
    # tester directory.exist()
    process = subprocess.Popen(['./remove-adobe-meta.sh', self.path_txt.get()], stdout=subprocess.PIPE)
    print(process.stdout.read())
    # while True:
    #   line = process.stdout.readline()
    #   if line != '':
    #     print (line.rstrip()) # used by python 3.x
    #   else:
    #     break

  def browse(self):
    self.txt_line.insert(0, "") # clean the path
    self.path = fd.askdirectory(title="Select a directory")
    self.txt_line.insert(0, self.path) # set the new path



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

