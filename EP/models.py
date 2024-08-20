import sqlite3
import hashlib
import os

DATABASE = 'event_planner.db'

def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt + hashed_password

def verify_password(stored_password, provided_password):
    salt = stored_password[:16]
    stored_password = stored_password[16:]
    return stored_password == hash_password(provided_password, salt)[16:]

def get_connection():
    return sqlite3.connect(DATABASE)

def create_user(username, password, role):
    conn = get_connection()
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                   (username, hashed_password, role))
    conn.commit()
    conn.close()

def get_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT username, password, role FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    if user and verify_password(user[1], password):
        return {'username': user[0], 'role': user[2]}
    return None

def create_task(name, description, deadline, budget):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (name, description, deadline, budget) VALUES (?, ?, ?, ?)",
                   (name, description, deadline, budget))
    conn.commit()
    conn.close()

def get_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, description, deadline, budget FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return [{'name': task[0], 'description': task[1], 'deadline': task[2], 'budget': task[3]} for task in tasks]

def create_attendee(name, email, registered_event):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO attendees (name, email, registered_event) VALUES (?, ?, ?)",
                   (name, email, registered_event))
    conn.commit()
    conn.close()

def get_attendees():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, email, registered_event FROM attendees")
    attendees = cursor.fetchall()
    conn.close()
    return [{'name': attendee[0], 'email': attendee[1], 'registered_event': attendee[2]} for attendee in attendees]
