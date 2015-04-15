
class Operation:

    def __init__(self, JSON):

        self.ID = JSON[u'deferred][u'id]
        self.Fileset = JSON[u'filesetid']
        self.Progress = 0
        self.State = ""

        if 'progress' in JSON.allkeys():
            self.Progress = JSON['progress']

        if 'state' in JSON.allkeys():
            self.State = JSON['state']
