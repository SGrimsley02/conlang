from flask import Flask, request, render_template, redirect
from SQLDictionary import addWord, printWord, search
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('LangHub.html')

@app.route('/EditDictionary.html', methods=['GET', 'POST'])
def EditDictionary():
    return render_template('EditDictionary.html')

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

    addWord(Word, Ipa, [(PoS, Definition)], [Example], [Translation], [Synonym], [Antonym])
    printWord(Word)
    return redirect('/')

@app.route('/ViewDictionary.html', methods=['GET', 'POST'])
def ViewDictionary():
    return render_template('ViewDictionary.html')

@app.route('/searchDict', methods=['GET', 'POST'])
def searchDict():
    Word = request.form.get('search_query')
    word_info = search(Word)
    if word_info:
        return render_template('searchResults.html', wordInfo=word_info)
    else:
        return render_template('noResult.html', entry_name=Word)





if __name__ == '__main__':
    app.run(debug=True)