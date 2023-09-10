# Import Tkinter
from tkinter import *
from time import sleep

# define master
master = Tk()

# define div
div = Frame(master)

# Vertical (y) Scroll Bar
scroll = Scrollbar(div)
scroll.pack(side=RIGHT, fill=Y)

# Text Widget
eula = Text(div, wrap=NONE, yscrollcommand=scroll.set)
# eula.insert("1.0", "text")
eula.pack(side="left")

# Configure the scrollbars
scroll.config(command=eula.yview)

i = 1.0
while(True):
    eula.insert(str(i),"Exemplo")
    # sleep(1)