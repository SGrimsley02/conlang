#####To run in terminal, run the following:

##python3
##from Dictionary import *

#####This will import all the functions as well
#####as initialize the dictionary from the file.

import pickle
from word import *
from GUI import inputGUI, wordDisplay

def loadDict(filename):
    '''Enter the file to load in.'''
    with open(filename, 'rb') as file:
        Dictionary = pickle.load(file)
        return Dictionary

def saveDict(filename):
    '''Enter the file to save to.'''
    with open(filename, 'wb') as file:
        pickle.dump(Dictionary, file)
    print("File saved")
##Note: Recommended to save to different file than loaded, that way
##      a backup is maintained.
def addWord():
    '''Enter word to add.'''
    try:
        word = inputGUI("Word: ")
        if word in Dictionary.keys():
            print(f"{Dictionary[word]}")
            print("Enter the following for the new definition, or 'None' to skip")
            tempPoS = PoS()
            tempPoS.type = inputGUI("Part of Speech: ")
            tempPoS.definition = inputGUI("Definition: ")
            tempPoS.translation = inputGUI("Translation: ")
            tempPoS.example = inputGUI("Example sentence(s): ").split('===')
            tempPoS.synonym = inputGUI("Synonym(s): ").split(',')
            tempPoS.antonym = inputGUI("Antonym(s): ").split(',')
            Dictionary[word].forms.append(tempPoS)
        else:
            tempWord = Word()
            tempPoS = PoS()
            tempWord.word = word
            print("Congratulations on a new word!")
            print("Enter 'None' when skipping an element")
            tempWord.ipa = inputGUI("Enter IPA: ")
            tempPoS.type = inputGUI("Part of Speech: ")
            tempPoS.definition = inputGUI("Definition: ")
            tempPoS.translation = inputGUI("Translation: ")
            tempPoS.example = inputGUI("Example sentence(s) (Split by ===): ").split('===')
            tempPoS.synonym = inputGUI("Synonym(s): ").split(',')
            tempPoS.antonym = inputGUI("Antonym(s): ").split(',')
            tempWord.forms.append(tempPoS)
            Dictionary[word] = tempWord
    except:
        print("Please try not to close in the middle of creating a word.")

def viewWord():
    '''Enter word you wish to view.'''
    word = inputGUI("Word: ")
    try:
        x = Dictionary[word]
        wordDisplay(x)
    except KeyError:
        print("Error: word doesn't exist")
    except:
        pass

def editWord(word, index):
    '''Enter word to edit, then number of form to edit.'''
    index = int(index) - 1
    x = Dictionary[word]
    if word not in Dictionary:
        print("Word does not exist")
        return
    if index > len(x.forms) or index < 0:
        print("Invalid definition index")
        return
    
    x = Dictionary[word].forms[index]
    print("Update word, type nothing to skip")
    prtOSpch = inputGUI("New part of speech: ")
    defn = inputGUI("New definition: ")
    trans = inputGUI("New translation: ")
    ex = inputGUI("New example(s): ")
    syn = inputGUI("New synonym(s): ")
    ant = input("New antonym(s): ")
    if prtOSpch != '':
        x.type = prtOSpch
    if defn != '':
        x.definition = defn
    if trans != '':
        x.translation= trans
    if ex != '':
        x.example = ex
    if syn != '':
        x.synonym = syn
    if ant != '':
        x.antonym = ant
    print("Word updated")
    return

def deleteWord(word):
    verification = input(f"Are you sure you want to delete {word} (y/n): ")
    if verification != 'y':
        return
    else:
        print(f"Just to be clear, {word} will be gone forever if you delete it.")
        verification = input("Are you really sure? (type YES): ")
        if verification != "YES":
            return
        else:
            print(f"Bye bye {word}")
            Dictionary.pop(word)

Dictionary = loadDict('pickleTest.Dictionary') ##Using this for testing, cleaner option to be implemented soon
