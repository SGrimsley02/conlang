from flask import Flask, request, render_template, redirect
from SQLDictionary import addWord, search, addDef, removeWord

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('LangHub.html')

##EDIT FUNCTIONS
@app.route('/EditDictionary.html', methods=['GET', 'POST'])
def EditDictionary():
    return render_template('Edit/EditDictionary.html')

@app.route('/addToDict', methods=['POST'])
def addToDict():
    Word = request.form.get('Word')
    Ipa = request.form.get('IPA')
    PoS = request.form.get('PoS')
    Definition = request.form.get('Def')
    Translation = request.form.get('Trans')
    Example = request.form.get('Example')
    Synonym = request.form.get('Syns')
    Antonym = request.form.get('Ants')

    addWord(Word, Ipa, PoS, Definition, Example, Translation, Synonym, Antonym)
    return redirect('/')

@app.route('/addToWord', methods=['POST'])
def addToWord():
    Word = request.form.get('Word')
    PoS = request.form.get('PoS')
    Definition = request.form.get('Def')
    Translation = request.form.get('Trans')
    Example = request.form.get('Example')
    Synonym = request.form.get('Syns')
    Antonym = request.form.get('Ants')
    
    addDef(Word, PoS, Definition, examples=Example, translations=Translation, synonyms=Synonym, antonyms=Antonym)
    return redirect('/')

@app.route('/editExistingWord', methods=['GET', 'POST'])
def editExistingWord():
    pass

@app.route('/remove', methods=['POST'])
def remove():
    Word = request.form.get('Word')
    removeWord(Word)
    return redirect('/EditDictionary.html')

@app.route('/EditGrammar.html', methods=['GET', 'POST'])
def EditGrammar():
    return render_template('Edit/Grammar/EditGrammar.html')

@app.route('/editPronouns.html', methods=['GET', 'POST'])
def editPronouns():
    return render_template('Edit/Grammar/Nouns/Pronouns.html')

##VIEW FUNCTIONS
@app.route('/ViewDictionary.html', methods=['GET', 'POST'])
def ViewDictionary():
    return render_template('View/Dict/ViewDictionary.html')

@app.route('/searchDict', methods=['GET', 'POST'])
def searchDict():
    Word = request.form.get('search_query')
    word_info = search(Word)
    if word_info:
        return render_template('View/Dict/searchResults.html', wordInfo=word_info)
    else:
        return render_template('View/Dict/noResult.html', entry_name=Word)

@app.route('/viewAll', methods=['GET', 'POST'])
def viewAll(): ##View like a physical dictionary
    pass











##TRANSLATE FUNCTIONS

##Run
if __name__ == '__main__':
    app.run(debug=True)