# wrap command-line script in GUI redirection tool to pop up its output

from tkinter import *

from PP4E.Gui.Tools.guiStreams import redirectedGuiFunc
from packdlg import runPackDialog


def runPackDialog_Wrapped():  # callback to run in mytools.py
    redirectedGuiFunc(runPackDialog)  # wrap entire callback handler


if __name__ == '__main__':
    root = Tk()
    Button(root, text='pop', command=runPackDialog_Wrapped).pack(fill=X)
    root.mainloop()
