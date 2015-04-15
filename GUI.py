
import Strongbox
from Tkinter import *

# Main GUI Window
class MainWindow(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.Strongboxes = Strongbox.StrongboxManager()

        self.geometry("800x500")
        self.title("Strongbox GUI")
        self.addElements()

        for Strongbox in self.Strongboxes.Strongboxes:
            self.StrongboxList.insert(END, Strongbox.IP)

        self.mainloop()

    def addElements(self):
        self.StrongboxList = Listbox(self, height=20, width=25)
        self.StrongboxList.place(x=39, y=60)

        self.StrongboxList.bind('<<ListboxSelect>>', self.strongboxListSelect)

        Button(self, text="Add Strongbox", width=22, command=self.addStrongboxClick).place(x=39, y=390)

        Button(self, text="Filesets", width=10, command=self.showFilesetsClick).place(x=280, y=25)
        Button(self, text="Operations", width=10,command=self.showOperationsClick).place(x=390, y=25)

        self.OperationFrame = Frame(self, height=360, width=500)
        self.OperationFrame.place(x=280, y=60)

        self.OperationList = Listbox(self.OperationFrame, height=20, width=62)
        self.OperationList.place(x=0, y=0)
        self.OperationList.bind("<<ListboxSelect>>", self.operationListboxSelect)

        self.CancelOperationButton = Button(self.OperationFrame, text="Cancel Operation", width=12, state=DISABLED, command=self.cancelOperationClick)
        self.CancelOperationButton.place(x=0, y=330)

        self.FilesetFrame = Frame(self, height=360, width=500)
        self.FilesetFrame.place(x=280, y=60)

        self.FilesetList = Listbox(self.FilesetFrame, height=20, width=62)
        self.FilesetList.place(x=0, y=0)
        self.FilesetList.bind("<<ListboxSelect>>", self.filesetListboxSelect)

        self.CreateFilesetButton = Button(self.FilesetFrame, text="Create Fileset", width=10, state=DISABLED, command=self.createFilesetClick)
        self.CreateFilesetButton.place(x=0, y=330)

        self.DeleteFilesetButton = Button(self.FilesetFrame, text="Delete Fileset", width=10, state=DISABLED, command=self.deleteFilesetClick)
        self.DeleteFilesetButton.place(x=110, y=330)

        self.PrefetchFilesetButton = Button(self.FilesetFrame, text="PrefetchFileset", width=10, state=DISABLED, command=prefetchFilesetClick)
        self.PrefetchFilesetButton.place(x=220, y=330)

    def showOperationsClick(event=None):
        pass

    def showFilesetsClick(event=None):
        pass

    def filesetListboxSelect(event=None):
        pass

    def operationListboxSelect(event=None):
        pass

    def addStrongboxClick(event=None):
        pass

    def addStrongbox(IP, User, Pass, Save):
        pass

    def strongboxListSelect(event=None):
        pass

    def createFilesetClick(event=None):
        pass

    def createFileset(FilesetInfo):
        pass

    def deleteFilesetClick(event=None):
        pass

    def prefetchFilesetClick(event=None):
        pass

    def updateOperation(Strongbox, Operation):
        pass

    def cancelOperationClick(event=None):
        pass


# Strongbox Info Popup
class StrongboxPopup(Tk):

    def __init__(self, app):
        Tk.__init__(self)

        self.app = app

        self.geometry("350x160")
        self.title("Strongbox GUI - Connect to Strongbox")
        self.addElements()
        self.mainloop()

    def addElements(self):
        Label(self, text="Strongbox IP:").place(x=20, y=20)
        self.StrongboxIPText = Entry(self, width=25)
        self.StrongboxIPText.place(x=120, y=20)

        Label(self, text="API Username: ").place(x=20, y=50)
        self.APIUserText = Entry(self, width=25)
        self.APIUserText.place(x=120, y=50)

        Label(self, text="API Password: ").place(x=20, y=80)
        self.APIPassText = Entry(self, width=25)
        self.APIPassText.place(x=120, y=80)

        Button(self, text="Connect", width=10, command=self.connect).place(x=40, y=115)
        Button(self, text="Quit", width=10, command=self.destroy).place(x=180, y=115)

    def connect(self):
        IP = self.StrongboxIPText.get()
        User = self.APIUserText.get()
        Pass = self.APIPassText.get()

        self.app.addStrongbox(IP, User, Pass)
        self.destroy()


class FilesetPopup(Tk):
    CREATEFILESET = 1

    def __init__(self):
        Tk.__init__(self)

        self.geometry("350x160")
        self.title("Strongbox GUI - Create Fileset")
        self.addElements()
        self.mainloop()

    def addElements(self):
        pass


class PrefetchPopup(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.geometry("350x160")
        self.title("Strongbox GUI - Start Prefetch")
        self.addElements()
        self.mainloop()

    def addElements(self):
        pass

if __name__ == "__main__":
    app = MainWindow()
