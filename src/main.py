import subprocess
from src.GUI import GUI


if __name__ == "__main__":
    guiFrame = GUI()
    guiFrame.mainloop()
    subprocess.call(['ls']) #COMMAND LINE'A ULASMAMIZI SAGLAYACAK
