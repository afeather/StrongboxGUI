from Strongbox import *


class StrongboxManager:
    # new StrongboxManager
    def __init__(self):
        self.Strongboxes = []

        # adds any Strongboxes that have been saved
        try:
            lines = []
            with open('STRONGBOXINFO', 'r') as f:
                lines = f.read().split('\n')[:-1]

            for line in [ l.split(" ") for l in lines ]:
                SB = Strongbox(line[0], line[1], line[2])
                if SB.getSystemInfo():
                    self.Strongboxes.append(SB)
        except IOError as e:
            pass

    # toString method
    def __str__(self):
        return "\n".join([ str(SB) for SB in self.Strongboxes ])

    # retrieve all the Strongboxes
    def getStrongboxes(self):
        return self.Strongboxes

    # create and add a Strongbox
    def addStrongbox(self, IP, User, Pass, Save):
        SB = Strongbox(IP, User, Pass)

        # if we can get the system info we must be connected
        if SB.getSystemInfo():
            self.Strongboxes.append(SB)

            if Save:
                with open('STRONGBOXINFO', 'a+') as f:
                    f.write(str(self) + "\n")

            return True

        return False

    # retrieve all the Filesets for a given Strongbox
    def getFilessets(self, StrongboxIndex):
        SB = self.Strongboxes[StrongboxIndex]
        FS = SB.getFilesets()
        return FS

    # retrieve all the Operations for a given Strongbox
    def getOperations(self, StrongboxIndex):
        SB =self.Strongboxes[StrongboxIndex]
        OP = SB.getOperations()
        return OP

    # create a fileset using the paths to files
    def createFilesetFromPath(self, StrongboxIndex, Paths):
        SB =self.Strongboxes[StrongboxIndex]
        FS = SB.createFilesetFromPath(Paths)
        return FS

    # create filesets using a pattern
    def createFilesetFromPattern(self, StrongboxIndex, Pattern, Includes, Recursive):
        SB =self.Strongboxes[StrongboxIndex]
        FS = SB.createFilesetFromPattern(Pattern, Includes, Recursive)
        return FS

    # delete a fileset given a StrongboxID and FilesetID
    def deleteFileset(self, StrongboxIndex, FilesetIndex):
        SB = self.Strongboxes[StrongboxIndex]
        isDeleted = SB.deleteFileset(FilesetIndex)
        return isDeleted

    # prefetch a fileset given StrongboxID and FilesetID
    def prefetchFileset(self, StrongboxIndex, FilesetIndex):
        SB = self.Strongboxes[StrongboxIndex]
        OP = SB.prefetchFileset(FilesetIndex)

        # Operation is return to update the GUI
        return OP

    # get the progress of an operation given the StrongboxID and FilesetID
    def getProgress(self, StrongboxIndex, OperationIndex):
        SB = self.Strongboxes[StrongboxIndex]
        OP = SB.getProgress(OperationIndex)

        # Operation is returned to update the GUI
        return OP

    # operations can only be cancelled and not deleted
    def cancelOperation(self, StrongboxIndex, OperationIndex):
        SB = self.Strongboxes[StrongboxIndex]
        isCancelled = SB.cancelOperation(OperationIndex)
        return isCancelled

if __name__ == "__main__":
    SBManager = StrongboxManager()
    SBManager.addStrongbox("123","123","123", True)
    print (str(SBManager))
    print str(SBManager.Strongboxes)
