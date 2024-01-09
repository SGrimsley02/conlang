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
    cursor.execute("INSERT INTO grammar (title, tag, body) VALUES (?, ?, ?)", (title, tag, text))
    conn.commit()

def getPosts(tag=None):
    conn = get_db_connection()
    cursor = get_db_cursor()
    if tag:
        cursor.execute("SELECT title, tag, body FROM grammar WHERE tag = ?", (tag,))
    else:
        cursor.execute("SELECT title, tag, body FROM grammar")
    entries = cursor.fetchall()
    
    return entries

def getTags():
    conn = get_db_connection()
    cursor = get_db_cursor()
    cursor.execute("SELECT DISTINCT tag FROM grammar")
    unique_tags = [tag[0] for tag in cursor.fetchall()]
    
    return unique_tags
