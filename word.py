'''
class Word:
    def __init__(self, word):
        self.word = word
        self.PoS = []
        self.define = []
        self.trans = []
        self.pronounce = ''
        self.examples = []
        self.synonyms = []
        self.antonyms = []

    def addDef(self, PoS, definition):
        self.Pos.append(PoS)
        self.define.append(definition)
        
    
    def giveTrans(self, eng):
        self.trans = eng
    
    def giveIPA(self, ipa):
        self.pronounce = ipa
    
    def giveEx(self, ex):
        self.example.append(ex)
    
    def giveSyn(self, syn):
        self.synonyms.append(syn)
    
    def giveAnt(self, ant):
        self.antonyms.append(ant)
    
    def __str__(self):
        return f"{self.word}: {self.define}"
    
    def __eq__(self, other):
        if other.word in self.synonyms:
            return True
        else:
            return False
    
    def __neq__(self, other):
        if other.word in self.antonyms:
            return True
        else:
            return False
    
'''



class PoS:
    def __init__(self, type):
        self.type = type
        self.definition = ''
        self.trans = ''
        self.ex = []
        self.syn = []
        self.ant = []

class Word:
    def __init__(self):
        self.ipa = ''
        self.defs = [] ##List of PoS objects
        
