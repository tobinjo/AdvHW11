import sys
import re
def topic():
    thingtosearchfor = sys.argv[1]
    occurancetimes = sys.argv[2]
    x = 3
    filelist = []
    while x < len(sys.argv):
        filelist.append(sys.argv[x])
        x += 1

    for fileName in filelist:
        occurances = 0
        filecontent = file(fileName).read()
        for m in re.finditer(thingtosearchfor, filecontent):
            occurances += 1
        if occurances == float(occurancetimes):
            print fileName


#Need to make some sort of class or some bs like that

class Searcher:
    
    def __init__(self):
        self.filestoiterate = []
    
    def search(self, word, compareNum, filelist):
        for fileName in filelist:
            occurances = 0;
            filecontent = file(fileName).read()
            for m in re.finditer(word, filecontent):
                occurances += 1
            if occurances == float(compareNum):
                self.filestoiterate.append(fileName)

        return self.filestoiterate



