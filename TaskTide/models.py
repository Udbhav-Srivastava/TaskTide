import sqlite3

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('event_planning.db')
    conn.row_factory = sqlite3.Row
    return conn

# Function to create a new user
def create_user(username, password, role):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                       (username, password, role))
        conn.commit()
    except sqlite3.IntegrityError:
        print("User already exists.")
    finally:
        conn.close()

# Function to get a user by username and password
def get_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", 
                   (username, password))
    user = cursor.fetchone()
    conn.close()
    return dict(user) if user else None

# Function to create a new task
def create_task(name, description, deadline, budget):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO tasks (name, description, deadline, budget) VALUES (?, ?, ?, ?)",
                       (name, description, deadline, budget))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Task already exists.")
    finally:
        conn.close()

# Function to retrieve all tasks
def get_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return [dict(task) for task in tasks]

# Function to create a new attendee
def create_attendee(name, email, registered_event):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO attendees (name, email, registered_event) VALUES (?, ?, ?)",
                       (name, email, registered_event))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Attendee already exists.")
    finally:
        conn.close()

# Function to retrieve all attendees
def get_attendees():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM attendees")
    attendees = cursor.fetchall()
    conn.close()
    return [dict(attendee) for attendee in attendees]

# Function to delete a task from the database
def delete_task_from_db(task_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM tasks WHERE name = ?", (task_name,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

# Function to delete a user from the database
def delete_user_from_db(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM users WHERE username = ?", (username,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

# Function to retrieve all users
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT username, role FROM users")
    users = cursor.fetchall()
    conn.close()
    return [dict(user) for user in users]
