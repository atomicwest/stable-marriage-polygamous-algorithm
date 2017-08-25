class Vendor():
    def __init__(self, prefs):
        self.matched = False
        self.prefs = prefs
        self.match = None
        self.visited = []
    
    def addMatch(self, value):
        if not self.matched:
            self.match = value
            self.matched = True
            return True
        else:
            return False
    
    def removeMatch(self):
        if self.matched:
            old = self.match
            self.match = None
            self.matched = False
            return old
        return None

    
    def seeAttr(self):
        print '********************'
        print "Is matched? %s" % str(self.matched)
        print "Preference list: %s" % str(self.prefs)
        print "Match: %s" % str(self.match)
        print '********************'
        