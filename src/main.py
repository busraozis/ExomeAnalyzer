import subprocess
from src.GUI import GUI
import sqlite3


if __name__ == "__main__":

    guiFrame = GUI()
    guiFrame.mainloop()

    returnCode = subprocess.call(['ls'])
    print(returnCode)
    os.chdir("/home/tolun/Documents/TEX84-87")
    returnCode = subprocess.call(['pwd'])
    print(returnCode)
    print(subprocess.call(['gunzip Tex84-002-001_S23_L004_R2_001.fastq.gz'], shell=True))
    """returnCode = subprocess.call(['bwa index -a bwtsw /home/tolun/Documents/TEK84-87/all_chr_hg19.fasta'])"""
    returnCode = subprocess.Popen(['bwa aln -n 0.01 -t 8 /home/tolun/Documents/TEK84-87/all_chr_hg19.fasta /home/tolun/Documents/TEX84-87/Tex84-002-001_S23_L004_R1_001.fastq > /home/tolun/Documents/TEX84-87/Tex84-002-001_S23_L004_R1_001.sai'],stdout=subprocess.PIPE,shell=True)  # COMMAND LINE'A ULASMAMIZI SAGLAYACAK( oluyor, index olmadığı için problemli sadece bwa aln
    # stdout u da alabiliyoruz
    cmd = 'bwa aln -n 0.01 -t 8 /home/tolun/Documents/TEK84-87/all_chr_hg19.fasta /home/tolun/Documents/TEX84-87/Tex84-002-001_S23_L004_R1_001.fastq > /home/tolun/Documents/TEX84-87/Tex84-002-001_S23_L004_R1_001.sai'
    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,close_fds=True)
    output = p.stdout.read()
    print(output)

    print(returnCode)

