#from src.GUI import GUI
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import subprocess
import time

class GUI(Tk):

    commandFile = "commands.txt"
    fileList = []
    vcfFiles = []
    checkboxes = []
    checkboxes2 = []
    checkboxesForIndex = []

    tools = []
    levelNumber = 5
    dict = {}

    def __init__(self,master=None):
        Tk.__init__(self, master)
        self.grid()

        self.grid_columnconfigure(0, weight=5)
        self.grid_rowconfigure(0, weight=1)

        self.title("Exome Analyzer")
        self.geometry("800x500")
        self.resizable(width=False, height=False)

        #background_image = PhotoImage(file="dna.gif")
        #self.background_label = Label(self, image=background_image, bd=0)
        #self.background_label.pack(fill=BOTH, expand=YES)

        self.addTool = Button(self, text="Start Simulation", width=25, command=self.toolScreen, bg="#009f9a")
        self.addTool.grid(column=0, row=0)
        self.chooseReference = Button(self, text="Choose Reference File",width=25, bg="#009f9a", command=self.chooseRef)
        self.chooseReference.grid(column=0, row=1)
        self.chooseVcf = Button(self, text="Choose Vcf Files", width=25, bg="#009f9a", command=self.chooseVcf)
        self.chooseVcf.grid(column=0, row=2)
        self.makeIndex = Button(self, text="Make Index", width=25, bg="#009f9a", command=self.indexTools)
        self.makeIndex.grid(column=0, row=3)
        self.submitButton = Button(self, text="Settings", width=25, bg = "#009f9a", command=self.settings)
        self.submitButton.grid(column=0,row=4)

        level = 0

        """ Opens the file commands.txt and initilizes
        the lists that contain the tool information"""
        with open(self.commandFile, "r") as commands:
            toolInfo = []
            commandArray = []
            indexArray = []
            toolsInLevel = []
            for line in commands:
                array = line.split()
                if(array[0] == 'level'):
                    level = array[1]
                elif (array[0] == 'end'):
                    toolInfo.append(indexArray)
                    toolInfo.append(commandArray)
                    toolsInLevel.append(toolInfo)
                    commandArray = []
                    indexArray = []
                    toolInfo = []
                elif(array[0]=='end-of-level'):
                    self.tools.append(toolsInLevel)
                    toolsInLevel = []
                elif(array[0] == 'index:'):
                    indexArray.append(line)
                elif(len(array) == 1):
                    toolName = array[0]
                    toolInfo.append(toolName)
                else:
                    commandArray.append(line)

        #print(self.tools)

        for i in range(1, self.levelNumber+1):
            self.dict[i] = self.tools[i-1]

        """self.submitButton.pack()
        self.submitButton.place(width=250, relx = 0.365, rely=0.5)"""

    def chooseRef(self):
        cwd = os.getcwd()
        self.reference =  filedialog.askopenfilename(initialdir = cwd,
                                                    title = "Choose Reference File",
                                                    filetypes = (("fasta","*.fasta"),("fa","*.fa")))
    def chooseVcf(self):
        cwd = os.getcwd()
        self.vcf =  filedialog.askopenfilename(initialdir = cwd, title = "Choose Vcf Files", filetypes = (("vcf","*.vcf"),("all files","*.*")))
        self.vcfFiles.append(self.vcf)

    def settings(self):
        self.destroy()
        Tk.__init__(self)
        self.grid()

        self.title("Exome Analyzer")
        self.geometry("800x500")
        self.resizable(width=False, height=False)

        self.labelframe = LabelFrame(self, text="Settings")
        self.labelframe.pack(fill="both", expand="yes")

        index = 0

        for key in self.dict.keys() :
            checkboxConditions = []
            self.label = Label(self.labelframe, text= "Step " + str(key))
            self.label.place(x=200, y=50 + (index+1) * 30)

            for item in self.dict[key] :
                index += 1
                variable = IntVar()
                self.cbox1 = Checkbutton(self.labelframe,variable=variable)

                checkboxConditions.append(variable)
                self.cbox1.place(x=250, y=50 + index * 30)
                self.label1 = Label(self.labelframe, text=item[0], relief=RAISED, bg="#009f9a", width=25)
                self.label1.place(x=280, y=50 + index * 30)
            self.checkboxes2.append(checkboxConditions)

        self.updateT = Button(self, text="Update", bg="#009fff", command=self.updateTool)
        self.updateT.place(x=280, y=100 + index * 30)

        self.deleteT = Button(self, text="Delete", bg = "#ffe7b5", command=self.deleteTool)
        self.deleteT.place(x=280, y=130 + index * 30)

        self.returnMain = Button(self, text="Return to Main Menu \u279C", bg="#009fff", command=self.returnMainMenu)
        self.returnMain.pack(side="bottom")

        self.addT = Button(self, text="Add New Tool", bg="#ffe7b5", command=self.addToolScreen)
        self.addT.pack(side="bottom")



    def updateTool(self):
        #Open a new update page
        self.destroy()
        Tk.__init__(self)
        self.grid()

        self.title("Exome Analyzer")
        self.geometry("800x500")
        self.resizable(width=False, height=False)

        #get selected tool to update
        level = 0
        for item in self.checkboxes2:
            level += 1
            number = -1
            for i in item:
                number += 1
                print(i.get())
                if (i.get() == 1):
                    updatedToolName = self.dict[level][number][0]
                    updatedToolLevel = level
                    if len(self.dict[level][number][1]) > 0:
                        updatedToolIndexCommand = self.dict[level][number][1]
                    else:
                        updatedToolIndexCommand = ""
                    if len(self.dict[level][number][2]) > 0:
                        updatedToolCommands = self.dict[level][number][2]
                    else:
                        updatedToolCommands = ['']
        self.checkboxes2.clear()

        self.updatePageTitle = Label(self, text="Update " + updatedToolName, fg="blue", font="Verdana 15 bold").pack()

        args = ['Indexing Command', 'Commands', 'Input File Format', 'Output File Format', 'Step']
        i = 0
        lastCommandPosition = 1
        for arg in args:
            self.arg = Label(self, text=arg + ": ")
            if i == 0:
                self.indexCommand = Label(self, text=updatedToolIndexCommand, font="Verdana 15 bold").pack()      # INDEX COMMAND
                #self.indexCommand.place(x=250, y=90 + i * 30)
                self.arg.place(x=100, y=90 + i * 30)
            elif i == 1:    #COMMANDS
                j = 0
                for commands in updatedToolCommands:
                    self.command = Label(self, text=updatedToolCommands[j])
                    self.command.place(x=250, y=90 + i * (j+1) * 30)
                    self.arg.place(x=100, y=90 + i * 30)
                    j += 1
                lastCommandPosition = j
            elif i == 2:    # INPUT FILE FORMAT
                lastCommandPosition += 1
                self.arg.place(x=100, y=90 + (i-1) * lastCommandPosition * 30)
            elif i == 3:    # OUTPUT FILE FORMAT
                lastCommandPosition += 1
                self.arg.place(x=100, y=90 + (i-2) * lastCommandPosition * 30)
            elif i == 4:
                var = StringVar()
                var.set(level)
                self.inputName5 = Spinbox(self, from_=1, to=len(self.dict), width=2, textvariable=var, state ='disabled')
                self.inputName5.place(x=250, y=90 + (i-3) * (lastCommandPosition+1) * 30)
                self.arg.place(x=100, y=90 + (i-3) * (lastCommandPosition+1) * 30)
            i += 1

        self.returnMain = Button(self, text="Return to Main Menu \u279C", bg="#009fff", command=self.returnMainMenu)
        self.returnMain.pack(side="bottom")

    def deleteTool(self):
        #Delete the tool from dictionary
        level = 0
        for item in self.checkboxes2:
            level += 1
            number = -1
            for i in item:
                number += 1
                print(i.get())
                if (i.get() == 1):
                    array = self.dict[level]
                    del self.dict[level]
                    del array[number]
                    self.dict[level] = array
        self.checkboxes2.clear()

        #Rewrite the content
        with open(self.commandFile, 'w') as file:
            for level in range(1,self.levelNumber+1):
                toolLevel = self.dict[level]
                file.write("level " + str(level) + "\n") # Level name
                for tool in toolLevel:
                    file.write(tool[0] + '\n') #Tool name
                    for index in tool[1]: # indexing commands
                        file.write(index)
                    for command in tool[2]:
                        file.write(command)
                    file.write('end' + '\n')
                file.write('end-of-level' + '\n')
        self.settings()

    def indexTools(self):
        self.destroy()
        Tk.__init__(self)
        self.grid()

        self.title("Exome Analyzer")
        self.geometry("800x500")
        self.resizable(width=False, height=False)

        self.labelframe = LabelFrame(self, text="Select Tools for Indexing")
        self.labelframe.pack(fill="both", expand="yes")

        index = 0
        self.checkboxes.clear()

        for key in self.dict.keys():

            self.label = Label(self.labelframe, text="Step " + str(key))
            # self.label.grid(column=0, row= index)
            self.label.place(x=200, y=50 + (index + 1) * 30)

            for item in self.dict[key]:
                index += 1
                var = IntVar()
                self.cbox1 = Checkbutton(self.labelframe, variable=var)
                self.checkboxesForIndex.append(var)
                self.cbox1.place(x=250, y=50 + index * 30)
                self.label1 = Label(self.labelframe, text=item[0], relief=RAISED, bg="#009f9a", width=25)
                self.label1.place(x=280, y=50 + index * 30)

        self.startProgress = Button(self, text="Start Indexing \u279C", bg="#009fff", command=self.indexing)
        self.startProgress.pack(side="bottom")

        self.chooseInput = Button(self, text="Choose reference files", bg="#ffe7b5", command=self.chooseReference)
        self.chooseInput.pack(side="bottom")

        self.returnMain = Button(self, text="Return to Main Menu \u279C", bg="#009fff", command=self.returnMainMenu)
        self.returnMain.pack(side="bottom")

    def indexing(self):
        self.indexing = Tk()
        self.indexing.title("Index")
        self.indexing.geometry("800x500")
        self.indexing.resizable(width=False, height=False)
        self.info = Label(self.indexing, text="Indexing has started.")
        self.info.place(x=10, y=20)
        self.progress = ttk.Progressbar(self.indexing, orient=HORIZONTAL, length=500, mode='determinate')
        self.progress.place(x=50, y=50)
        #subprocess.call(['bwa', 'index', '-a', 'bwtsw', self.reference ])

    def toolScreen(self):
        self.destroy()
        Tk.__init__(self)
        self.grid()

        self.title("Exome Analyzer")
        self.geometry("800x500")
        self.resizable(width=False, height=False)

        self.labelframe = LabelFrame(self, text="Select Tools")
        self.labelframe.pack(fill="both", expand="yes")

        index = 0
        self.checkboxes.clear()

        for key in self.dict.keys() :
            checkboxConditions = []
            self.label = Label(self.labelframe, text= "Step " + str(key))
            self.label.place(x=200, y=50 + (index+1) * 30)

            for item in self.dict[key] :
                index += 1
                var = IntVar()
                if len(self.dict[key]) == 1 and key != 1 :
                    self.cbox1 = Checkbutton(self.labelframe,state=DISABLED, variable=var)
                    self.cbox1.select()
                else :
                    self.cbox1 = Checkbutton(self.labelframe,variable=var)

                checkboxConditions.append(var)
                self.cbox1.place(x=250, y=50 + index * 30)
                self.label1 = Label(self.labelframe, text=item[0], relief=RAISED, bg="#009f9a", width=25)
                self.label1.place(x=280, y=50 + index * 30)
            self.checkboxes.append(checkboxConditions)

        self.startProgress = Button(self, text="Start Progress \u279C", bg="#009fff", command=self.startSimulation)
        self.startProgress.pack(side="bottom")

        self.chooseInput = Button(self, text="Choose input files", bg = "#ffe7b5", command=self.clickForSelectFiles)
        self.chooseInput.pack(side="bottom")

        self.returnMain = Button(self, text="Return to Main Menu \u279C", bg="#009fff", command=self.returnMainMenu)
        self.returnMain.pack(side="bottom")

    def returnMainMenu(self):
        self.destroy()
        self.__init__()

    """This method creates the simulation screen
            and calls the process method """
    def startSimulation(self):
        if len(self.fileList) == 0 :
            self.popup = Tk()
            self.popup.title("Warning!")
            self.popup.geometry("400x100")
            self.popup.resizable(width=False, height=False)
            self.warning = Label(self.popup, text="You must choose at least one input file to start progress!")
            self.warning.place(x=10, y=20)
            return

        self.progressDialog = Tk()
        self.progressDialog.title("Simulation has started!")
        self.progressDialog.geometry("800x500")
        self.progressDialog.resizable(width=False, height=False)
        self.info = Label(self.progressDialog, text="Çalışan programın ismi ve progress durumu: ")
        self.info.place(x=10, y=20)
        self.progressBar = ttk.Progressbar(self.progressDialog, orient=HORIZONTAL, length=500, mode='determinate')
        self.progressBar.place(x=50, y=500)
        self.process()
        #self.ilerle()


    """This method parses the commands of the selected tools,
        assignes appropriate files according to the extentions,
        and calls subprocess to run the commands """
    def process(self):
        level = 0
        index = 0
        outputFileNumber = 1
        for item in self.checkboxes:
            level += 1
            number = -1
            for i in item:
                number += 1
                #print(i.get())
                if( i.get() == 1 ):
                    toolLevel = self.dict[level]
                    tool = toolLevel[number]
                    commands = tool[2]
                    for command in commands:
                        index += 1
                        countOfFiles = command.count('{fastq}') # Total number of fastq files in the command
                        array = command.split()
                        #If command has only one fastq, commmand runs repeatedly for every selected input file
                        if(countOfFiles == 1):
                            for i in range(0,len(self.fileList)):
                                for item in array:
                                    if (item.startswith('{')):
                                        newitem = item[1:len(item) - 1]
                                        if (newitem == 'fasta' or newitem == 'fa'):
                                            array[array.index(item)] = self.reference
                                        elif (newitem == 'vcf'):
                                            array[array.index(item)] = self.vcfFiles[0]
                                        elif (newitem == 'fastq'):
                                            array[array.index(item)] = self.fileList[i]
                                        else:
                                            array[array.index(item)] = self.fileList[0] + str(outputFileNumber - 1) + '.' + newitem
                                            outputFileNumber += 1
                                    elif (item.startswith('[')):
                                        newitem = item[1:len(item) - 1]
                                        #Output file always takes the first files name + its extention
                                        outputFile = self.fileList[0] + str(outputFileNumber) + '.' + newitem
                                        outputFileNumber += 1
                                        array[array.index(item)] = outputFile
                        elif(countOfFiles > 1):
                            fileNumber = 0
                            for item in array:
                                if(item.startswith('{')):
                                    newitem = item[1:len(item)-1]
                                    if(newitem == 'fasta' or newitem == 'fa'):
                                        array[array.index(item)] = self.reference
                                    elif(newitem == 'vcf'):
                                        array[array.index(item)] = self.vcfFiles[0]
                                    elif(newitem == 'fastq'):
                                        array[array.index(item)] = self.fileList[fileNumber]
                                        fileNumber += 1
                                    else:
                                        #Probably Wrong Solution!!!!!
                                        array[array.index(item)] = self.fileList[0]+ str(outputFileNumber-2) + '.' + newitem
                                        outputFileNumber += 1
                                elif(item.startswith('[')):
                                    newitem = item[1:len(item) - 1]
                                    # Output file always takes the first files name + its extention
                                    outputFile = self.fileList[0] + str(outputFileNumber) +'.' + newitem
                                    outputFileNumber +=1
                                    array[array.index(item)] = outputFile
                        else:
                            for item in array:
                                if (item.startswith('{')):
                                    newitem = item[1:len(item) - 1]
                                    if (newitem == 'fasta' or newitem == 'fa'):
                                        array[array.index(item)] = self.reference
                                    elif (newitem == 'vcf'):
                                        array[array.index(item)] = self.vcfFiles[0]
                                    else:
                                        array[array.index(item)] = self.fileList[0] + str(outputFileNumber - 1) + '.' + newitem
                                elif (item.startswith('[')):
                                    newitem = item[1:len(item) - 1]
                                    outputFile = self.fileList[0] + str(outputFileNumber) + '.' + newitem
                                    outputFileNumber += 1
                                    array[array.index(item)] = outputFile

                        self.runningTool = Label(self.progressDialog, text=array[0] + ' ' + array[1])
                        self.runningTool.place(x=10, y=50+ index*20)
                        #returnCode = subprocess.call(array)
                        #print(returnCode)
                        #print(array)

    def ilerle(self):
        self.progressBar["value"] = self.progressBar["value"] + 1
        if self.progressBar["value"] < 100:
            # read more bytes after 100 ms
            self.after(100, self.ilerle)

        else:
            self.finish = Label(self.progressDialog, text="Simulation finished successfully!\n Check output directory to see the result!")
            self.finish.place(x=50, y=100)

        """for i in range(len(self.checkboxes)):
            self.dummy = Label(self.progressDialog, text=self.checkboxes[i].get())
            self.dummy.place(x=30, y=50+i*50)"""


    def clickForSelectFiles(self):
        cwd = os.getcwd()
        self.filenames =  filedialog.askopenfilenames(initialdir = cwd, title = "Choose input file",filetypes = (("fastq","*.fastq"),("fastq.gz","*.fastq.gz"),("all files","*.*")))
        self.fileList = list(self.filenames)   ##seçilen dosyalar fileList listesinde!!

        #for index in range(len(self.fileList)):
         #   print(self.fileList[index])

    def addToolScreen(self):
        self.destroy()
        Tk.__init__(self)
        self.grid()

        self.title("Exome Analyzer")
        self.geometry("800x500")
        self.resizable(width=False, height=False)

        self.labelframe1 = LabelFrame(self, text="Add New Tool")
        self.labelframe1.pack(fill="both", expand="yes")

        args = ['Tool Name', 'Indexing Command','Commands', 'Input File Format', 'Output File Format', 'Step']
        i = 0
        for arg in args:
            self.arg = Label(self, text= arg + ": ")
            self.arg.place(x=100, y=90 + i*30)
            if i == 0:
                self.inputName = Entry(self, width=35)    #TOOL NAME
                self.inputName.place(x=250, y=90 + i * 30)
            elif i == 1:
                self.inputName1 = Entry(self, width=35)   #INDEX COMMAND
                self.inputName1.place(x=250, y=90 + i * 30)
            elif i == 2:
                self.inputName2 = Entry(self, width=35)   #COMMANDS
                self.inputName2.place(x=250, y=90 + i * 30)
            elif i == 3:
                self.inputName3 = Entry(self, width=35)   #INPUT FILE FORMAT
                self.inputName3.place(x=250, y=90 + i * 30)
            elif i == 4:
                self.inputName4 = Entry(self, width=35)   #OUTPUT FILE FORMAT
                self.inputName4.place(x=250, y=90 + i * 30)
            elif i == 5:
                self.inputName5 = Spinbox(self,from_=1, to=len(self.dict), width= 2)
                self.inputName5.place(x=250, y=90 + i * 30)
            else:
                self.inputName6 = Entry(self, width=35)
                self.inputName6.place(x=250, y=90 + i * 30)
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
        self.returnMain = Button(self, text="Return to Main Menu \u279C", bg="#009fff", command=self.returnMainMenu)
        self.returnMain.pack(side="bottom")

    def addButtonClick(self):

        level = int(self.inputName5.get())
        tool = [self.inputName.get(),self.inputName1.get(),self.inputName2.get()]

        if len(self.inputName.get()) != 0 :
            self.dict[level].append(tool)

        #Rewrite the content
        with open(self.commandFile, 'w') as file:
            for level in range(1,self.levelNumber+1):
                toolLevel = self.dict[level]
                file.write("level " + str(level) + "\n") # Level name
                for tool in toolLevel:
                    file.write(tool[0] + '\n') #Tool name
                    for index in tool[1]: # indexing commands
                        file.write(index)
                    for command in tool[2]:
                        file.write(command)
                    file.write('end' + '\n')
                file.write('end-of-level' + '\n')

        #print(self.tools)

        self.labelframe1.destroy()
        self.addButton.destroy()
        #self.button.destroy()
        self.list.destroy()
        self.inputName.destroy()

        self.settings()


if __name__ == "__main__":

    guiFrame = GUI()
    guiFrame.mainloop()

    """returnCode = subprocess.call(['ls'])
    print(returnCode)
    os.chdir("/home/tolun/Documents/TEX84-87")
    returnCode = subprocess.call(['pwd'])
    print(returnCode)
    print(subprocess.call(['gunzip Tex84-002-001_S23_L004_R2_001.fastq.gz'], shell=True))
    #returnCode = subprocess.call(['bwa index -a bwtsw /home/tolun/Documents/TEK84-87/all_chr_hg19.fasta'])
    returnCode = subprocess.Popen(['bwa aln -n 0.01 -t 8 /home/tolun/Documents/TEK84-87/all_chr_hg19.fasta /home/tolun/Documents/TEX84-87/Tex84-002-001_S23_L004_R1_001.fastq > /home/tolun/Documents/TEX84-87/Tex84-002-001_S23_L004_R1_001.sai'],stdout=subprocess.PIPE,shell=True)  # COMMAND LINE'A ULASMAMIZI SAGLAYACAK( oluyor, index olmadığı için problemli sadece bwa aln
    # stdout u da alabiliyoruz
    cmd = 'bwa aln -n 0.01 -t 8 /home/tolun/Documents/TEK84-87/all_chr_hg19.fasta /home/tolun/Documents/TEX84-87/Tex84-002-001_S23_L004_R1_001.fastq > /home/tolun/Documents/TEX84-87/Tex84-002-001_S23_L004_R1_001.sai'
    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,close_fds=True)
    output = p.stdout.read()
    print(output)

    print(returnCode)"""

