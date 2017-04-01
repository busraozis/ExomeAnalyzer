#simple gui
from tkinter import *

#create window
root = Tk()

#modify root window
root.title("Exome Analyzer")
root.geometry("800x500")

but = Button(root, text="Start Simulation", width=25)
but.pack()

root.mainloop()

