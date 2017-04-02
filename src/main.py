#simple gui
from tkinter import *
from tkinter import filedialog
import os

class GUI(Tk):

    def __init__(self,master=None):
        Tk.__init__(self, master)
        self.grid()

        self.title("Exome Analyzer")
        self.geometry("800x500")

        self.fileList = []

        self.level1 = [['FastQC', 'commands', 'input file' , 'output file' ]]
        self.level2 = [['BWA-MEM', 'commands', 'input file', 'output file']]
        self.level3 = [['Picard', 'commands', 'input file', 'output file']]
        self.level4 = [['Samtools', 'commands', 'input file', 'output file'],
                       ['GATK', 'commands', 'input file', 'output file'],
                       ['Freebayes', 'commands', 'input file', 'output file']]
        self.level5 = [['Annovar', 'commands', 'input file', 'output file']]

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

        self.dict = {1: self.level1, 2: self.level2, 3: self.level3, 4: self.level4 , 5: self.level5}
        index = 0

        for key in self.dict.keys() :

            self.label = Label(self, text= "Step " + str(key))
            self.label.place(x=100, y=10 + (index+1) * 30)
    ###cbox değerlerinin ayrı değerlendirilebilmesi!!!
            for item in self.dict[key] :
                index += 1
                if len(self.dict[key]) == 1 :
                    self.cbox1 = Checkbutton(state=DISABLED)
                    self.cbox1.select()
                else :
                    self.cbox1 = Checkbutton()

                self.cbox1.place(x=150, y=10 + index * 30)
                self.label1 = Label(self, text=item[0] , relief=RAISED, bg="#009f9a", width=25)
                self.label1.place(x=180, y=10 + index * 30)


        self.button = Button(self, text="Add new tool", width=10, command=self.button2Click, bg="#009fff")
        self.button.place(x=180, y = 10 + (index +1)*30)

        self.button2 = Button(self, text="Next \u279C", width=10, bg="#009fff", command=self.clickForSelectFiles)
        self.button2.pack(side="bottom")

    def clickForSelectFiles(self):
        cwd = os.getcwd()
        self.filename =  filedialog.askopenfilename(initialdir = cwd, title = "Choose your file",filetypes = (("fastq","*.fastq"),("fastq.gz","*.fastq.gz"),("all files","*.*")))
        self.fileList.append(self.filename)   ##seçilen dosyalar fileList listesinde!!

        #for index in range(len(self.fileList)):
         #   print(self.fileList[index])

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
            if i == 0:
                self.inputName = Entry(self, width=35)
                self.inputName.place(x=250, y=90 + i * 30)
            elif i == 1:
                self.inputName1 = Entry(self, width=35)
                self.inputName1.place(x=250, y=90 + i * 30)
            elif i == 2:
                self.inputName2 = Entry(self, width=35)
                self.inputName2.place(x=250, y=90 + i * 30)
            elif i == 3:
                self.inputName3 = Entry(self, width=35)
                self.inputName3.place(x=250, y=90 + i * 30)
            elif i == 4:
                self.inputName4 = Spinbox(self,from_=1, to=len(self.dict), width= 2)
                self.inputName4.place(x=250, y=90 + i * 30)
            else:
                self.inputName5 = Entry(self, width=35)
                self.inputName5.place(x=250, y=90 + i * 30)
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

        level = int(self.inputName4.get())
        #tool = [self.inputName.get(),self.inputName1.get(),self.inputName2.get(),self.inputName3.get()]

        ##yeni eklenen tool'un adı tam gözükmüyor add tool ekranında!!!! sadece ilk harfi!!!!
        self.dict[level].append(self.inputName.get())


        self.labelframe1.destroy()
        self.addButton.destroy()
        #self.button.destroy()
        self.list.destroy()
        self.inputName.destroy()

        self.toolScreen()


if __name__ == "__main__":
    guiFrame = GUI()
    guiFrame.mainloop()

