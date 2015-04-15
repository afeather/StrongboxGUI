#import requests
#from requests.auth import HTTPBasicAuth
import base64
import hashlib
import time

class Strongbox:

    # new Strongbox with IP and login info
    def __init__(self, IP, User, Pass):
        self.IP = IP
        self.User = User
        self.Pass = Pass

        self.Filesets = []
        self.Operations = []

        if len(User) > 0 and len(Pass) > 0:
            self.URL = 'https://' + self.IP + '/api/public/'
            #self.Auth = HTTPBasicAuth(User, Pass)
        else:
            self.URL = 'http://' + self.IP + '/api/public/'
            #self.Auth = None

        self.Headers = {'Content-Type':'application/json; charset=utf8'}

        self.ClientNonce = None

    def __str__(self):
        return self.IP + " " + self.User + " " + self.Pass

    def getSystemInfo(self):

        if self.ClientNonce == None:
            hash = hashlib.sha256()
            hash.update(str(time.time()))
            self.ClientNonce = base64.standard_b64encode(hash.digest())[:28]

        URL = self.URL + 'system/identity?client_nonce=' + self.ClientNonce

        r = request.get(URL, headers=self.Headers, verify=False)
        return json.loads(r.content())

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

        if type(Paths) is str:
            Paths = [ p.strip() for p in Paths.split(',') ]

        if type(Paths) is not list:
            return None

        URL = self.URL + 'file_sets/'
        Payload = {'paths':Paths}

        r = requests.post(URL, data=json.dumps(Payload), headers=self.Headers, auth=self.Auth, verify=False)
        response = json.loads(r.content)

        FS = Fileset(response)

        if FS is not None:
            self.Filesets.append(FS)

        return FS

    # create a fileset given a pattern to match
    def createFilesetFromPattern(self, Files, Includes, Recursive):

        if type(Files) is str:
            Files = [ f.strip() for f in Files.split(',') ]

        if type(Includes) is str:
            Includes = [ i.strip() for i in Inclues.split(',') ]

        if type(Files) is not list or type(Includes) is not list or type(Recursive) is not bool:
            return None

        URL = self.URL + 'file_sets/'
        Payload = {'files':Files, 'includes': Includes, 'recursive': Recursive }

        r = requests.post(URL, data=json.dumps(Payload), headers=self.Headers, auth=self.Auth, verify=False)
        response = json.loads(r.content)

        FS = Fileset(response)

        if FS is not None:
            self.Filesets.append(FS)

        return FS

    # delete a given fileset
    def deleteFileset(self, FilesetIndex):
        URL = self.URL + '/file_sets/' + str(FilesetIndex)

        r = requests.delete(URL, headers=self.Headers, auth=self.Auth, verify=False)

        del self.Filesets[FilesetIndex]

    # prefetch a given fileset
    def prefetchFileset(self, FilesetIndex):
        URL = self.URL + '/file_sets/' + str(FilesetIndex) + "/prefetch"

        r = request.put(URL, headers=self.Headers, auth=self.Auth, verify=False)
        response = json.loads(r.content)

        op = Operation(response)

        if op is not None:
            OP.append(op)

        return op

    # get the progress of a given operation
    def getProgress(self, OperationIndex):
        URL = self.URL + '/operations/' + str(OperationIndex)

        r = request.post(URL, headers=self.Headers, auth=self.Auth, verify=False)
        response = json.loads(r.content)

        op = Operation(response)
        OP[OperationIndex] = op

        return op

    # cancel a given operation
    def cancelOperation(self, OperationIndex):
        URL = self.URL + '/operations/' + str(OperationIndex)+ '/cancel/'

        r = request.post(URL, headers=self.Headers, auth=self.Auth, verify=False)
        response = json.loads(r.content)

        op = Operation(response)
        OP[OperationIndex] = op

        return op


if __name__ == "__main__":
    n = Strongbox('ip', 'user', 'pass')
    n.getSystemInfo()

    print n.ClientNonce
    print len(n.ClientNonce)
