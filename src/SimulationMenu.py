#Simdilik bu dosya dummy kalsin sonra kodu moduler yaparken kullaniriz



from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
from src.GUI import GUI

class Sim(Tk):
    def __init__(self, master=None):
        Tk.__init__(self, master)
        self.grid()

        self.grid_columnconfigure(0, weight=5)
        self.grid_rowconfigure(0, weight=1)

        self.title("Exome Analyzer")
        self.geometry("800x500")
        self.resizable(width=False, height=False)

        self.fileList = []
        self.checkboxes = []

        self.level1 = [['FastQC', 'commands', 'input file', 'output file']]
        self.level2 = [['BWA-MEM', 'commands', 'input file', 'output file']]
        self.level3 = [['Picard', 'commands', 'input file', 'output file']]
        self.level4 = [['Samtools', 'commands', 'input file', 'output file'],
                       ['GATK', 'commands', 'input file', 'output file'],
                       ['Freebayes', 'commands', 'input file', 'output file']]
        self.level5 = [['Annovar', 'commands', 'input file', 'output file']]

        self.submitButton = Button(self, text="Start Simulation", width=25, bg="#009f9a", command=GUI.buttonClick)
        self.submitButton.grid(column=0, row=0)

