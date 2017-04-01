#simple gui
from tkinter import *

class GUI(Tk):

    def __init__(self,master=None):
        Tk.__init__(self, master)
        self.grid()

        self.submitButton = Button(master, text="Start Simulation", width=25, bg = "#009f9a", command=self.buttonClick)
        self.submitButton.grid()
        self.submitButton.pack()
        self.submitButton.place(width=250, relx = 0.365, rely=0.5)

        self.title("Exome Analyzer")
        self.geometry("800x500")


    def buttonClick(self):
        """ handle button click event and output text from entry area"""
        self.submitButton.configure(bg = "green")


if __name__ == "__main__":
    guiFrame = GUI()
    guiFrame.mainloop()
#create window
#root = Tk()

#modify root window
#root.title("Exome Analyzer")
#root.geometry("800x500")

#self.but = Button(root, text="Start Simulation", width=25, command=self.buttonClick)
#self.but.configure(bg = "#009f9a")
#self.but.pack()

#root.mainloop()




