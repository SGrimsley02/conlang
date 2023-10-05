#####To run in terminal, run the following:

##python3
##from Dictionary import *

#####This will import all the functions as well
#####as initialize the dictionary from the file.

##import pickle
##from word import *
from GUI import inputGUI, wordDisplay
from SQLDictionary import *

def addToDict():
    addWord(inputGUI("Word: "), inputGUI("IPA: "), [(inputGUI("PoS: "), inputGUI("Defs: "))], inputGUI("Translations: ").split('; '), inputGUI("Synonyms: ").split('; '))

def viewWord():
    wordDisplay(inputGUI('Word: '))

def removeWordDict():
    removeWord(inputGUI('Word to remove: '))

def editWordDict():
    editWord(inputGUI("Word: "), inputGUI("IPA: "), [(inputGUI('PoS:'), inputGUI("Defs:"))], inputGUI("Translations:").split('; '), inputGUI("Synonyms:").split('; '))

def end():
    conn.close()
    quit()