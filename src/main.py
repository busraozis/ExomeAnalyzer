#simple gui
from tkinter import *

class GUI(Tk):

    def __init__(self,master=None):
        Tk.__init__(self, master)
        self.grid()

        self.title("Exome Analyzer")
        self.geometry("800x500")

        self.submitButton = Button(master, text="Start Simulation", width=25, bg = "#009f9a", command=self.buttonClick)
        self.submitButton.grid()
        self.submitButton.pack()
        self.submitButton.place(width=250, relx = 0.365, rely=0.5)


    def buttonClick(self):
        """ handle button click event and output text from entry area"""
        self.toolScreen()

    def toolScreen(self):
        self.submitButton.destroy()
        self.label1 = Label(self, text="1. FastQC", relief=RAISED, bg="#009f9a")
        self.label1.place(x=150, y=150)
        self.cbox1 = Checkbutton()
        self.cbox1.place(x=220, y=150)
        self.label2 = Label(self, text="2. BWA", relief=RAISED, bg="#009f9a")
        self.label2.place(x=150, y=170)
        self.cbox2 = Checkbutton(state=DISABLED)
        self.cbox2.select()
        self.cbox2.place(x=220, y=170)
        self.label3 = Label(self, text="3. Picard", relief=RAISED, bg="#009f9a")
        self.label3.place(x=150, y=190)
        self.cbox3 = Checkbutton(state=DISABLED)
        self.cbox3.select()
        self.cbox3.place(x=220, y=190)
        self.label4 = Label(self, text="4. Samtools", relief=RAISED, bg="#009f9a")
        self.label4.place(x=150, y=210)
        self.cbox4 = Checkbutton()
        self.cbox4.place(x=220, y=210)
        self.label5 = Label(self, text="4. GATK", relief=RAISED, bg="#009f9a")
        self.label5.place(x=150, y=230)
        self.cbox5 = Checkbutton()
        self.cbox5.place(x=220, y=230)
        self.label6 = Label(self, text="4. FreeBayes", relief=RAISED, bg="#009f9a")
        self.label6.place(x=150, y=250)
        self.cbox6 = Checkbutton()
        self.cbox6.place(x=220, y=250)
        self.label7 = Label(self, text="5. Annovar", relief=RAISED, bg="#009f9a")
        self.label7.place(x=150, y=270)
        self.cbox7 = Checkbutton(state=DISABLED)
        self.cbox7.select()
        self.cbox7.place(x=220, y=270)


        self.button = Button(self, text="Add new tool", width=25, command=self.button2Click, bg="#009fff")
        self.button.pack()

        self.button2 = Button(self, text="Next \u279C", width=10, command=self.button2Click, bg="#009fff")
        self.button2.pack(side="bottom")

    def button2Click(self):
        self.destroy()      ######################
        self.emptyScreen()
        #Tk.__init__(self, master)
        #self.grid()
    def emptyScreen(self):
        Tk.__init__(self)
        self.grid()

        self.title("Exome Analyzer")
        self.geometry("800x500")


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




