import sqlite3

def create_tables():
    conn = sqlite3.connect('event_planning.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')

    # Create tasks table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            name TEXT PRIMARY KEY,
            description TEXT,
            deadline TEXT,
            budget TEXT
        )
    ''')

    # Create attendees table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attendees (
            name TEXT,
            email TEXT,
            registered_event TEXT,
            PRIMARY KEY (name, email)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
