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
        """ handle button click event and output text from entry area"""
        self.toolScreen()

    def toolScreen(self):
        self.submitButton.destroy()

        self.labelframe = LabelFrame(self, text="Select Tools")
        self.labelframe.pack(fill="both", expand="yes")

        level1 = ['FastQC']
        level2 = ['BWA-MEM']
        level3 = ['Picard']
        level4 = ['Samtools', 'GATK', 'Freebayes']
        level5 = ['Annovar']

        dict = {1: level1, 2: level2, 3: level3, 4: level4 , 5: level5}
        index = 0

        for key in dict.keys() :

            self.label = Label(self, text= "Step " + str(key))
            self.label.place(x=100, y=10 + (index+1) * 30)

            for item in dict[key] :
                index += 1
                if len(dict[key]) == 1 :
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




