import sqlite3
import threading
## Connect to or create a SQLite database (if it doesn't exist)

local = threading.local()
def get_db_connection():
    if not hasattr(local, 'db'):
        local.db = sqlite3.connect('mydictionary.db')
    return local.db
def get_db_cursor():
    conn = get_db_connection()
    return conn.cursor()
conn = get_db_connection()
cursor = get_db_cursor()

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
                    word_id INTEGER,
                    definition TEXT,
                    FOREIGN KEY (word_id) REFERENCES words (word_id),
                    FOREIGN KEY (pos_id) REFERENCES parts_of_speech (pos_id))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS examples (
                examp_id INTEGER PRIMARY KEY,
                pos_id INTEGER,
                word_id INTEGER,
                example TEXT,
                FOREIGN KEY (word_id) REFERENCES words (word_id),
                FOREIGN KEY (pos_id) REFERENCES parts_of_speech (pos_id))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS translations (
                    trans_id INTEGER PRIMARY KEY,
                    pos_id INTEGER,
                    word_id INTEGER,
                    translation TEXT,
                    FOREIGN KEY (word_id) REFERENCES words (word_id),
                    FOREIGN KEY (pos_id) REFERENCES parts_of_speech (pos_id))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS synonyms (
                    syn_id INTEGER PRIMARY KEY,
                    pos_id INTEGER,
                    word_id INTEGER,
                    synonym TEXT,
                    FOREIGN KEY (word_id) REFERENCES words (word_id),
                    FOREIGN KEY (pos_id) REFERENCES parts_of_speech (pos_id))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS antonyms (
                    ant_id INTEGER PRIMARY KEY,
                    pos_id INTEGER,
                    word_id INTEGER,
                    antonym TEXT,
                    FOREIGN KEY (word_id) REFERENCES words (word_id),
                    FOREIGN KEY (pos_id) REFERENCES parts_of_speech (pos_id))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS grammar (
                id INTEGER PRIMARY KEY,
                overview BLOB,
                highlights BLOB,
                nouns BLOB,
                verbs BLOB,
                adwords BLOB,
                adpositions BLOB,
                determiners BLOB,
                particles BLOB,
                interjections BLOB,
                other BLOB)''')
conn.commit()
cursor.close()
conn.close()

def addWord(new_word, ipa_rep, PoS, definition, example=None, translation=None, synonym=None, antonym=None): ## Adds word to dictionary
    '''Takes a word, ipa, list of tuples with PoS and defs, optional examples, translations, synonyms, and antonyms lists.'''
    conn = sqlite3.connect("mydictionary.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO words (word, ipa) VALUES (?, ?)", (new_word, ipa_rep))
    word_id = cursor.lastrowid

    cursor.execute("INSERT INTO parts_of_speech (word_id, part_of_speech) VALUES (?, ?)", (word_id, PoS))
    pos_id = cursor.lastrowid
    cursor.execute("INSERT INTO definitions (pos_id, word_id, definition) VALUES (?, ?, ?)", (pos_id, word_id, definition))
    if example:
        cursor.execute("INSERT INTO examples (pos_id, word_id, example) VALUES (?, ?, ?)", (pos_id, word_id, example))
    if translation:
        cursor.execute("INSERT INTO translations (pos_id, word_id, translation) VALUES (?, ?, ?)", (pos_id, word_id, translation))
    if synonym:
        cursor.execute("INSERT INTO synonyms (pos_id, word_id, synonym) VALUES (?, ?, ?)", (pos_id, word_id, synonym))
    if antonym:
        cursor.execute("INSERT INTO antonyms (pos_id, word_id, antonym) VALUES (?, ?, ?)", (pos_id, word_id, antonym))
    conn.commit()

def addDef(word_adding, PoS, definition, examples=None, translations=None, synonyms=None, antonyms=None):
    conn = sqlite3.connect("mydictionary.db")
    cursor = conn.cursor()
    cursor.execute("SELECT word_id, ipa FROM words WHERE word = ?", (word_adding,))
    word_info = cursor.fetchone()
    if word_info:
        word_id, ipa = word_info ##Still figuring out if I need ipa for anything here
        cursor.execute("INSERT INTO parts_of_speech (word_id, part_of_speech) VALUES (?, ?)", (word_id, PoS))
        pos_id = cursor.lastrowid
        cursor.execute("INSERT INTO definitions (pos_id, definition) VALUES (?, ?)", (pos_id, definition))
        if examples:
            cursor.execute("INSERT INTO examples (pos_id, example) VALUES (?, ?)", (pos_id, examples))
        if translations:
            cursor.execute("INSERT INTO translations (pos_id, translation) VALUES (?, ?)", (pos_id, translations))
        if synonyms:
            cursor.execute("INSERT INTO synonyms (pos_id, synonym) VALUES (?, ?)", (pos_id, synonyms))
        if antonyms:
            cursor.execute("INSERT INTO antonyms (pos_id, antonym) VALUES (?, ?)", (pos_id, antonyms))
    conn.commit()

def editWord(word_to_edit, new_ipa=None, newPoSandDef=None, newEx=[], newTrans=[], newSyns=[], newAnts=[]): ##Needs reworking
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
                if newEx:
                    for example in newEx:
                        cursor.execute("UPDATE examples SET example = ? WHERE pos_id = ?", (example, pos_id))
                if newTrans:
                    for translation in newTrans:
                        cursor.execute("UPDATE translations SET translation = ? WHERE pos_id = ?", (translation, pos_id))
                if newSyns:
                    for synonym in newSyns:
                        cursor.execute("UPDATE synonyms SET synonym = ? WHERE pos_id = ?", (synonym, pos_id))
                if newAnts:
                    for antonym in newAnts:
                        cursor.execute("UPDATE antonyms SET antonym = ? WHERE pos_id = ?", (antonym, pos_id))
        conn.commit()
    else:
        raise IndexError("Word does not exist.")

def removeWord(word_to_remove):
    conn = sqlite3.connect("mydictionary.db")
    cursor = conn.cursor()
    cursor.execute("SELECT word_id FROM words WHERE word = ?", (word_to_remove,))
    word_id = cursor.fetchone()
    if word_id:
        word_id = word_id[0]
        cursor.execute("DELETE FROM words WHERE word_id = ?", (word_id,))
        conn.commit()
    else:
        raise IndexError("Word does not exist.")

def printWord(word_to_find): ##Needs reworking, for testing purposes only
    # Retrieve the word and its IPA representation from the "words" table
    conn = sqlite3.connect("mydictionary.db")
    cursor = conn.cursor()
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

        cursor.execute("SELECT example FROM examples WHERE word_id = ?", (word_id,))
        examples = cursor.fetchall()

        ## Retrieve examples
        if examples:
            print("Examples:")
            for example in examples:
                print(f"- {example[0]}")

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
        
        ## Retrieve antonyms
        cursor.execute("SELECT antonym FROM antonyms WHERE word_id = ?", (word_id,))
        antonyms = cursor.fetchall()

        if antonyms:
            print("Antonyms:")
            for antonym in antonyms:
                print(f"- {antonym[0]}")
    else:
        print(f"The word '{word_to_find}' was not found in the database.")

def search(word_to_find):
    conn = sqlite3.connect("mydictionary.db")
    cursor = conn.cursor()
    cursor.execute("SELECT word_id, ipa FROM words WHERE word = ?", (word_to_find,))
    word_info = cursor.fetchone()
    if word_info:
        word_id, ipa = word_info
        word = {}
        word["Word"] = word_to_find
        word["IPA"] = ipa
        cursor.execute("SELECT part_of_speech FROM parts_of_speech WHERE word_id = ?", (word_id,))
        word['pos'] = cursor.fetchall()
        cursor.execute("SELECT pos_id FROM parts_of_speech WHERE word_id = ?", (word_id,))
        pos_ids = [row[0] for row in cursor.fetchall()]
        word['definitions'] = []
        word['examples'] = []
        word['translations'] = []
        word['synonyms'] = []
        word['antonyms'] = []
        for id in pos_ids:
            cursor.execute("SELECT definition FROM definitions WHERE pos_id = ?", (id,))
            word['definitions'].append(cursor.fetchall())

            cursor.execute("SELECT example FROM examples WHERE pos_id = ?", (id,))
            word['examples'].append(cursor.fetchall())

            cursor.execute("SELECT translation FROM translations WHERE pos_id = ?", (id,))
            word['translations'].append(cursor.fetchall())

            cursor.execute("SELECT synonym FROM synonyms WHERE pos_id = ?", (id,))
            word['synonyms'].append(cursor.fetchall())

            cursor.execute("SELECT antonym FROM antonyms WHERE pos_id = ?", (id,))
            word['antonyms'].append(cursor.fetchall())

        return word

