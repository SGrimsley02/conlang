from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('InputsPage.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    Word = request.form.get('Word')
    Ipa = request.form.get('IPA')
    PoS = request.form.get('PoS')
    Definition = request.form.get('Definition')
    Translation = request.form.get('Translation')
    Example = request.form.get('Example')
    Synonym = request.form.get('Synonym')
    Antonym = request.form.get('Antonym')

    ## Print to make sure it worked
    print(f"Input 1: {Word}")
    print(f"Input 2: {Ipa}")
    print(f"Input 3: {PoS}")
    print(f"Input 4: {Definition}")
    print(f"Input 5: {Translation}")
    print(f"Input 6: {Example}")
    print(f"Input 7: {Synonym}")
    print(f"Input 8: {Antonym}")

    return "Inputs processed successfully"

if __name__ == '__main__':
    app.run(debug=True)

