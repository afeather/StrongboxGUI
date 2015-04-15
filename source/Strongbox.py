import requests
from requests.auth import HTTPBasicAuth

class Strongbox:

    # new Strongbox with IP and login info
    def __init__(self, IP, User, Pass):
        self.IP = IP
        self.User = User
        self.Pass = Pass

        self.Filesets = []
        self.Operations = []

        if len(User) == 0 or len(Pass) == 0:
            self.URL = 'https://' + self.IP + '/api/public/'
            self.Auth = HTTPBasicAuth(User, Pass)
        else:
            self.URL = 'http://' + self.IP + '/api/public/'
            self.Auth = None

        self.Headers = {'Content-Type':'application/json; charset=utf8'}

    def __str__(self):
        return self.IP + " " + self.User + " " + self.Pass

    def getSystemInfo(self):
        URL = self.URL + 'system/'
        # r = request.get(URL, headers=self.Headers, auth=self.Auth, verify=False)
        # return r.status_code == 200

        return True

    # method to retrieve Strongbox IP
    def getIP(self):
        return self.IP

    # method to retrieve all the filesets
    def getFilesets(self):
        return self.Filesets

    # method to retrieve all the operations
    def getOperations(self):
        return self.Operations

    # create a fileset given a path
    def createFilesetFromPath(self, Paths):
        URL = self.URL + 'file_sets/'
        Payload = {'paths':Paths}
        # r = requests.put(URL, data=json.dumps(Payload), headers=self.Headers, auth=self.Auth, verify=False)
        # response = json.loads(r.content)
        return Fileset(response)

    # create a fileset given a pattern to match
    def createFilesetFromPattern(self, Pattern, Includes, Recursive):
        URL = self.URL + 'file_sets/'
        Payload = {'files':Pattern, 'includes': Includes, 'recursive': Recursive }
        # r = requests.put(URL, data=json.dumps(Payload), headers=self.Headers, auth=self.Auth, verify=False)
        # response = json.loads(r.content)
        return Fileset(response)

    # prefetch a given fileset
    def deleteFileset(self, FilesetIndex):
        URL = self.URL + '/file_sets/' + str(FilesetIndex)
        # r = requests.delete(URL, headers=self.Headers, auth=self.Auth, verify=False)
        # response = json.loads(r.content)
        #fs = Fileset(response)
        #FS.remove(FilesetIndex)

        return not (fs == None)

    # prefetch a given fileset
    def prefetchFileset(self, FilesetIndex):
        URL = self.URL + '/file_sets/' + str(FilesetIndex) + "/prefetch"
        # r = request.post(URL, headers=self.Headers, auth=self.Auth, verify=False)
        # response = json.loads(r.content)
        op = Operation(response)
        OP.append(op)
        return op

    # get the progress of a given operation
    def getProgress(self, OperationIndex):
        URL = self.URL + '/operations/' + str(OperationIndex)
        # r = request.post(URL, headers=self.Headers, auth=self.Auth, verify=False)
        # response = json.loads(r.content)
        op = Operation(response)
        OP[OperationIndex] = op
        return op

    # cancel a given operation
    def cancelOperation(self, OperationIndex):
        URL = self.URL + '/operations/' + str(OperationIndex)+ '/cancel/'
        # r = request.post(URL, headers=self.Headers, auth=self.Auth, verify=False)
        # response = json.loads(r.content)
        op = Operation(response)
        OP[OperationIndex] = op
        return op


if __name__ == "__main__":
    Strongbox('ip', 'user', 'pass')
