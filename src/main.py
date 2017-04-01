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


        self.button = Button(self, text="Add new tool", width=10, command=self.button2Click, bg="#009fff")
        self.button.place(x=180, y = 10 + (index +1)*30)

        self.button2 = Button(self, text="Next \u279C", width=10, bg="#009fff")
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

        args = ['Tool Name', 'Commands', 'Input File Format', 'Output File Format', 'Step']
        i = 0
        for arg in args:
            self.arg = Label(self, text= arg + ": ")
            self.arg.place(x=100, y=90 + i*30)
            if i == 1:
                self.inputName = Entry(self, width=50)
                self.button = Button(self, text="Add Command", bg="#009fff")
                self.button.place(x=600, y=90+ i*30)
            elif i == 4:
                self.inputName = Spinbox(self,from_=1, to=len(self.dict))
            else:
                self.inputName = Entry(self, width=50)
            self.inputName.place(x=250, y=90 + i * 30)
            i += 1

        self.list = Listbox(self, width= 50, height= 6)
        self.list.insert(END, "Hint")
        self.list.insert(END, "Step 1: Quality Control")
        self.list.insert(END, "Step 2: Initial Alingment")
        self.list.insert(END, "Step 3: Removing Duplicates")
        self.list.insert(END, "Step 4: Recalibration, Calling and Filtering Variants")
        self.list.insert(END, "Step 5: Annovar")
        self.list.pack()

        self.addButton = Button(self, text="Add", width=15, command=self.addButtonClick)
        self.addButton.pack()



    def addButtonClick(self):


        self.labelframe1.destroy()
        self.addButton.destroy()
        self.button.destroy()
        self.list.destroy()
        self.inputName.destroy()

        self.toolScreen()


if __name__ == "__main__":
    guiFrame = GUI()
    guiFrame.mainloop()

