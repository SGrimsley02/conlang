import sqlite3
import threading
## Connect to or create a SQLite database (if it doesn't exist)

local = threading.local()
def get_db_connection():
    if not hasattr(local, 'db'):
        local.db = sqlite3.connect('mygrammar.db')
    return local.db
def get_db_cursor():
    conn = get_db_connection()
    return conn.cursor()
conn = get_db_connection()
cursor = get_db_cursor()

##Creates a table that will store posts for any grammar stuff
##Original grammar recording method, will be replaced by more complex stuff in future
cursor.execute('''CREATE TABLE IF NOT EXISTS grammar (
                id INTEGER PRIMARY KEY,
                title TEXT,
                tag TEXT,
                body TEXT
)''')
conn.commit()
cursor.close()
conn.close()

def createPost(title, text, tag=None):
    conn = get_db_connection()
    cursor = get_db_cursor()
    if tag:
        cursor.execute("INSERT INTO grammar (title, tag, body) VALUES (?, ?, ?)", (title, tag, text))
    else:
        cursor.execute("INSERT INTO grammar (title, body) VALUES (?, ?, ?)", (title, text))
    conn.commit()