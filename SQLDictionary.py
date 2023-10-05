import sqlite3

## Connect to or create a SQLite database (if it doesn't exist)
conn = sqlite3.connect("mydictionary.db")
cursor = conn.cursor()

## Initialize if necessary
cursor.execute('''CREATE TABLE IF NOT EXISTS words (
                    word_id INTEGER PRIMARY KEY,
                    word TEXT NOT NULL UNIQUE,
                    ipa TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS parts_of_speech (
                    pos_id INTEGER PRIMARY KEY,
                    word_id INTEGER,
                    part_of_speech TEXT,
                    FOREIGN KEY (word_id) REFERENCES words (word_id))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS definitions (
                    def_id INTEGER PRIMARY KEY,
                    pos_id INTEGER,
                    definition TEXT,
                    FOREIGN KEY (pos_id) REFERENCES parts_of_speech (pos_id))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS translations (
                    trans_id INTEGER PRIMARY KEY,
                    word_id INTEGER,
                    translation TEXT,
                    FOREIGN KEY (word_id) REFERENCES words (word_id))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS synonyms (
                    syn_id INTEGER PRIMARY KEY,
                    word_id INTEGER,
                    synonym TEXT,
                    FOREIGN KEY (word_id) REFERENCES words (word_id))''')
conn.commit()

##### Sample #####

new_word = "example"
ipa_representation = "/ɪɡˈzæmpl/"
parts_of_speech_and_definitions = [
    ("Noun", "A representative of a group; a typical instance."),
    ("Verb", "To be illustrated or exemplified (by)."),
    ("Adjective", "Serving as a pattern; typical."),
    ("Verb", "To prove; to make an example (out of)")
]
translations = ["ejemplo (Spanish)", "exemplo (Portuguese)"]
synonyms = ["illustration", "instance"]

def addWord(new_word, ipa_rep, PoSandDefs, translations=[], synonyms=[]): ## Adds word to dictionary
    '''Takes a word, ipa, list of tuples with PoS and defs, optional translations and synonyms lists.'''
    cursor.execute("INSERT INTO words (word, ipa) VALUES (?, ?)", (new_word, ipa_rep))
    word_id = cursor.lastrowid
    for part_of_speech, definition in PoSandDefs:
        cursor.execute("INSERT INTO parts_of_speech (word_id, part_of_speech) VALUES (?, ?)", (word_id, part_of_speech))
        pos_id = cursor.lastrowid
        cursor.execute("INSERT INTO definitions (pos_id, definition) VALUES (?, ?)", (pos_id, definition))
    if translations:
        for translation in translations:
            cursor.execute("INSERT INTO translations (word_id, translation) VALUES (?, ?)", (word_id, translation))
    if synonyms:
        for syn in synonyms:
            cursor.execute("INSERT INTO synonyms (word_id, synonym) VALUES (?, ?)", (word_id, syn))
    conn.commit()

def editWord(word_to_edit, new_ipa=None, newPoSandDef=None, newTrans=[], newSyns=[]):
    cursor.execute("SELECT word_id FROM words WHERE word=?", (word_to_edit,))
    word_id = cursor.fetchone()
    if word_id:
        if new_ipa:
            cursor.execute("UPDATE words SET ipa = ? WHERE word_id = ?", (new_ipa, word_id[0]))
        if newPoSandDef:
            for part_of_speech, definition in newPoSandDef:
                cursor.execute("UPDATE parts_of_speech SET part_of_speech = ? WHERE word_id = ?", (part_of_speech, word_id[0]))
                pos_id = cursor.lastrowid
                cursor.execute("UPDATE definitions SET definition = ? WHERE pos_id = ?", (definition, pos_id))
        if newTrans:
            for translation in newTrans:
                cursor.execute("UPDATE translations SET translation = ? WHERE word_id = ?", (translation, word_id[0]))
        if newSyns:
            for synonym in newSyns:
                cursor.execute("UPDATE synonyms SET synonym = ? WHERE word_id = ?", (synonym, word_id))
        conn.commit()
    else:
        raise IndexError("Word does not exist.")

def removeWord(word_to_remove):
    cursor.execute("SELECT word_id FROM words WHERE word = ?", (word_to_remove,))
    word_id = cursor.fetchone()
    if word_id:
        word_id = word_id[0]
        cursor.execute("DELETE FROM words WHERE word_id = ?", (word_id,))
        conn.commit()
    else:
        raise IndexError("Word does not exist.")

def printWord(word_to_find): ## Mostly just for testing
    # Retrieve the word and its IPA representation from the "words" table
    cursor.execute("SELECT word_id, ipa FROM words WHERE word = ?", (word_to_find,))
    word_info = cursor.fetchone()  # Fetch the first matching row
    if word_info:
        word_id, ipa = word_info
        print(f"Word: {word_to_find}")
        print(f"IPA: {ipa}")

        # Retrieve parts of speech and associated definitions
        cursor.execute("""
            SELECT ps.part_of_speech, d.definition
            FROM parts_of_speech ps
            JOIN definitions d ON ps.pos_id = d.pos_id
            WHERE ps.word_id = ?
        """, (word_id,))
        pos_definitions = cursor.fetchall()

        for pos, definition in pos_definitions:
            print(f"Part of Speech: {pos}")
            print(f"Definition: {definition}")

        # Retrieve translations
        cursor.execute("SELECT translation FROM translations WHERE word_id = ?", (word_id,))
        translations = cursor.fetchall()

        if translations:
            print("Translations:")
            for translation in translations:
                print(f"- {translation[0]}")

        # Retrieve synonyms
        cursor.execute("SELECT synonym FROM synonyms WHERE word_id = ?", (word_id,))
        synonyms = cursor.fetchall()

        if synonyms:
            print("Synonyms:")
            for synonym in synonyms:
                print(f"- {synonym[0]}")
    else:
        print(f"The word '{word_to_find}' was not found in the database.")

#addWord(new_word, ipa_representation, parts_of_speech_and_definitions, translations= translations, synonyms= synonyms)
#printWord('example')
#editWord('example', new_ipa="ExAmPlE")
#printWord('example')
#removeWord('example')

##################





## End
#conn.close()