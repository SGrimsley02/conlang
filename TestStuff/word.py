class PoS:
    def __init__(self):
        self.type = ''
        self.definition = ''
        self.translation = ''
        self.example = []
        self.synonym = []
        self.antonym = []

class Word:
    def __init__(self):
        self.word = ''
        self.ipa = ''
        self.forms = [] ##List of PoS objects
    
    def __str__(self):
        return f"{self.word} ({self.ipa})"