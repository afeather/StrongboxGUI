
class Fileset:

    def __init__(self, JSON):
        self.ID = JSON[u'id]
        self.Name = JSON[u'name']

        if 'path' in JSON.allkeys():
            self.Paths = JSON['paths']
            self.Includes = ""
            self.Recursive = ""
        else if 'files' in JSON.allkeys():
            self.Paths = JSON['files']
            self.Includes = JSON['includes']
            self.Recursive = JSON['recursive']

        self.Fileount = JSON['filecount']
