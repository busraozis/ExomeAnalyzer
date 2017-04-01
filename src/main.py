#simple gui
from tkinter import *
import  operator

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
        self.submitButton.destroy()
        self.toolScreen()

    def toolScreen(self):

        self.labelframe = LabelFrame(self, text="Select Tools")
        self.labelframe.pack(fill="both", expand="yes")

        level1 = ['FastQC']
        level2 = ['BWA-MEM']
        level3 = ['Picard']
        level4 = ['Samtools', 'GATK', 'Freebayes']
        level5 = ['Annovar']

        self.dict = {1: level1, 2: level2, 3: level3, 4: level4 , 5: level5}
        index = 0

        for key in self.dict.keys() :

            self.label = Label(self, text= "Step " + str(key))
            self.label.place(x=100, y=10 + (index+1) * 30)

            for item in self.dict[key] :
                index += 1
                if len(self.dict[key]) == 1 :
                    self.cbox1 = Checkbutton(state=DISABLED)
                    self.cbox1.select()
                else :
                    self.cbox1 = Checkbutton()

                self.cbox1.place(x=150, y=10 + index * 30)
                self.label1 = Label(self, text=item , relief=RAISED, bg="#009f9a")
                self.label1.place(x=180, y=10 + index * 30)


        self.button = Button(self, text="Add new tool", width=25, command=self.button2Click, bg="#009fff")
        self.button.place(x=180, y = 10 + (index +1)*30)

        self.button2 = Button(self, text="Next \u279C", width=10, command=self.button2Click, bg="#009fff")
        self.button2.pack(side="bottom")

    def button2Click(self):
        self.destroy()      ######################
        self.addToolScreen()
        #Tk.__init__(self, master)
        #self.grid()
    def addToolScreen(self):
        Tk.__init__(self)
        self.grid()

        self.title("Exome Analyzer")
        self.geometry("800x500")

        self.labelframe1 = LabelFrame(self, text="Add New Tool")
        self.labelframe1.pack(fill="both", expand="yes")

        self.toolName = Label(self, text="Tool Name: ")
        self.toolName.place(x=100, y=90)
        self.inputName = Entry(self, width=40)
        self.inputName.place(x=350, y = 90)

        self.commLine = Label(self, text="Commands that will run the tool: ")
        self.commLine.place(x=100, y=120)
        self.inputArgs = Entry(self, width=40)
        self.inputArgs.place(x=350, y=120)

        self.inFormat = Label(self, text="Input File Format: ")
        self.inFormat.place(x=100, y=150)
        self.inInput = Entry(self, width=40)
        self.inInput.place(x=350, y=150)

        self.outFormat = Label(self, text="Output File Format: ")
        self.outFormat.place(x=100, y=180)
        self.outInput = Entry(self, width=40)
        self.outInput.place(x=350, y=180)

        self.level = Label(self, text="In which level does the tool work? ")
        self.level.place(x=100, y=210)
        self.scroll = Scrollbar(self)
       # self.scroll.place(x=350, y=210)
        self.scroll.pack()
        self.list = Listbox(self, yscrollcommand = self.scroll.set)
        for key in self.dict.keys() :
            self.list.insert(END, "Level: "+ str(key))

        self.list.pack()
        self.scroll.config(command=self.list.yview)

        self.addButton = Button(self, text="Add", width=15, command=self.addButtonClick)
        self.addButton.pack()

    def addButtonClick(self):
        self.labelframe1.destroy()
        self.addButton.destroy()

        self.toolScreen()

if __name__ == "__main__":
    guiFrame = GUI()
    guiFrame.mainloop()

