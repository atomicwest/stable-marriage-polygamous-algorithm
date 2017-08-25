#===========================================================

        
class Customer():
    def __init__(self, prefs):
        self.maxsellers = len(prefs)
        self.prefs = prefs
        self.matches = []
        self.full = False
        self.visited = []
    
    def addMatch(self, value):
        if not self.full:
            self.matches.append(value)
            if len(self.matches) == self.maxsellers:
                self.full = True
            return True
        else:
            return False
    
    def removeMatch(self,value):
        try:
            if not self.isPref(value):
                self.matches.remove(value)
                self.full = False
        except:
            return False
        
    
    def removeNonPref(self):
        for n in self.matches:
            if not self.isPref(n):
                self.matches.remove(n)
                return n
        return None
        
    def isPref(self,seller):
        if seller in self.prefs:
            return True
        else:
            return False
    
    def seeAttr(self):
        print '....................'
        print "Has max allowable sellers? %s" % str(self.full)
        print "Max number of sellers: %s" % str(self.maxsellers)
        print "Preference list: %s" % str(self.prefs)
        print "Matches: %s" % str(self.matches)
        print '....................'
        
