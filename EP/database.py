import sqlite3

def get_db_connection():
    conn = sqlite3.connect('event_planner.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT,
        deadline DATE,
        budget REAL
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS attendees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        registered_event TEXT
    )
    ''')

    conn.commit()
    conn.close()

# Initialize the database when the script is run
if __name__ == "__main__":
    init_db()
