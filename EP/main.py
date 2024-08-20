import tkinter as tk
from tkinter import ttk, messagebox
from models import create_user, get_user, create_task, get_tasks, create_attendee, get_attendees

# Initialize the main application window
root = tk.Tk()
root.title("Event Planning Assistant")
root.geometry("800x600")
root.configure(bg="#f0f4f7")  # Light blue-grey background

# Global variables for dynamic widgets
username_entry = None
password_entry = None
reg_username_entry = None
reg_password_entry = None
role_var = None
task_name_entry = None
task_desc_entry = None
deadline_entry = None
budget_entry = None
attendee_name_entry = None
attendee_email_entry = None
event_name_entry = None

def login():
    username = username_entry.get()
    password = password_entry.get()

    user = get_user(username, password)
    if user:
        messagebox.showinfo("Login", f"Welcome {username}")
        main_app(user['role'])
    else:
        messagebox.showerror("Login", "Invalid username or password")

def register_user():
    username = reg_username_entry.get()
    password = reg_password_entry.get()
    role = role_var.get()

    create_user(username, password, role)
    messagebox.showinfo("Register", "User registered successfully")

def add_task():
    task_name = task_name_entry.get()
    description = task_desc_entry.get()
    deadline = deadline_entry.get()
    budget = budget_entry.get()

    create_task(task_name, description, deadline, budget)
    messagebox.showinfo("Task", "Task added successfully")

def view_tasks():
    tasks_window = tk.Toplevel(root)
    tasks_window.title("View Tasks")
    tasks_window.geometry("600x400")
    tasks_window.configure(bg="#f0f4f7")  # Light blue-grey background

    tasks_tree = ttk.Treeview(tasks_window, columns=("Name", "Description", "Deadline", "Budget"), show="headings")
    tasks_tree.heading("Name", text="Name")
    tasks_tree.heading("Description", text="Description")
    tasks_tree.heading("Deadline", text="Deadline")
    tasks_tree.heading("Budget", text="Budget")
    tasks_tree.pack(fill=tk.BOTH, expand=True)

    tasks = get_tasks()
    for task in tasks:
        tasks_tree.insert("", tk.END, values=(task['name'], task['description'], task['deadline'], task['budget']))

def register_attendee():
    attendee_name = attendee_name_entry.get()
    attendee_email = attendee_email_entry.get()
    registered_event = event_name_entry.get()

    create_attendee(attendee_name, attendee_email, registered_event)
    messagebox.showinfo("Registration", "Attendee registered successfully")

def view_attendees():
    attendees_window = tk.Toplevel(root)
    attendees_window.title("View Attendees")
    attendees_window.geometry("600x400")
    attendees_window.configure(bg="#f0f4f7")  # Light blue-grey background

    attendees_tree = ttk.Treeview(attendees_window, columns=("Name", "Email", "Event"), show="headings")
    attendees_tree.heading("Name", text="Name")
    attendees_tree.heading("Email", text="Email")
    attendees_tree.heading("Event", text="Event")
    attendees_tree.pack(fill=tk.BOTH, expand=True)

    attendees = get_attendees()
    for attendee in attendees:
        attendees_tree.insert("", tk.END, values=(attendee['name'], attendee['email'], attendee['registered_event']))

def main_app(user_role):
    main_window = tk.Toplevel(root)
    main_window.title("Event Planning Assistant - Dashboard")
    main_window.geometry("800x600")
    main_window.configure(bg="#f0f4f7")  # Light blue-grey background

    if user_role == "organizer":
        # Task Management
        task_frame = tk.Frame(main_window, bg="#ffffff", padx=20, pady=20, borderwidth=2, relief="sunken")
        task_frame.pack(pady=20, padx=40, fill=tk.X)

        tk.Label(task_frame, text="Task Name:", bg="#ffffff", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        global task_name_entry
        task_name_entry = tk.Entry(task_frame, width=40, font=("Arial", 12))
        task_name_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(task_frame, text="Description:", bg="#ffffff", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        global task_desc_entry
        task_desc_entry = tk.Entry(task_frame, width=40, font=("Arial", 12))
        task_desc_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(task_frame, text="Deadline (YYYY-MM-DD):", bg="#ffffff", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        global deadline_entry
        deadline_entry = tk.Entry(task_frame, width=40, font=("Arial", 12))
        deadline_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(task_frame, text="Budget:", bg="#ffffff", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
        global budget_entry
        budget_entry = tk.Entry(task_frame, width=40, font=("Arial", 12))
        budget_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Button(task_frame, text="Add Task", command=add_task, bg="#4caf50", fg="white", font=("Arial", 12), relief="raised").grid(row=4, column=0, padx=10, pady=10)
        tk.Button(task_frame, text="View Tasks", command=view_tasks, bg="#4caf50", fg="white", font=("Arial", 12), relief="raised").grid(row=4, column=1, padx=10, pady=10)

        # Attendee Management
        attendee_frame = tk.Frame(main_window, bg="#ffffff", padx=20, pady=20, borderwidth=2, relief="sunken")
        attendee_frame.pack(pady=20, padx=40, fill=tk.X)

        tk.Label(attendee_frame, text="Attendee Name:", bg="#ffffff", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        global attendee_name_entry
        attendee_name_entry = tk.Entry(attendee_frame, width=40, font=("Arial", 12))
        attendee_name_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(attendee_frame, text="Email:", bg="#ffffff", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        global attendee_email_entry
        attendee_email_entry = tk.Entry(attendee_frame, width=40, font=("Arial", 12))
        attendee_email_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(attendee_frame, text="Event:", bg="#ffffff", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        global event_name_entry
        event_name_entry = tk.Entry(attendee_frame, width=40, font=("Arial", 12))
        event_name_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Button(attendee_frame, text="Register Attendee", command=register_attendee, bg="#4caf50", fg="white", font=("Arial", 12), relief="raised").grid(row=3, column=0, padx=10, pady=10)
        tk.Button(attendee_frame, text="View Attendees", command=view_attendees, bg="#4caf50", fg="white", font=("Arial", 12), relief="raised").grid(row=3, column=1, padx=10, pady=10)

    else:
        # Attendee view if they log in
        tk.Label(main_window, text="Welcome to the Event Planner!", bg="#f0f4f7", font=("Arial", 16)).pack(pady=20)
        tk.Button(main_window, text="View Registered Events", command=view_attendees, bg="#4caf50", fg="white", font=("Arial", 12), relief="raised").pack(pady=10)

# Initial login/register screen
def setup_initial_screen():
    global username_entry, password_entry, reg_username_entry, reg_password_entry, role_var

    # Frame for login
    login_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20, borderwidth=2, relief="sunken")
    login_frame.pack(pady=40, padx=40, fill=tk.X)

    tk.Label(login_frame, text="Username:", bg="#ffffff", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
    username_entry = tk.Entry(login_frame, width=40, font=("Arial", 12))
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(login_frame, text="Password:", bg="#ffffff", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
    password_entry = tk.Entry(login_frame, show="*", width=40, font=("Arial", 12))
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Button(login_frame, text="Login", command=login, bg="#4caf50", fg="white", font=("Arial", 12), relief="raised").grid(row=2, columnspan=2, pady=10)

    # Frame for registration
    register_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20, borderwidth=2, relief="sunken")
    register_frame.pack(pady=20, padx=40, fill=tk.X)

    tk.Label(register_frame, text="New User? Register Here:", bg="#ffffff", font=("Arial", 14)).grid(row=0, columnspan=2, pady=10)

    tk.Label(register_frame, text="Username:", bg="#ffffff", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
    reg_username_entry = tk.Entry(register_frame, width=40, font=("Arial", 12))
    reg_username_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(register_frame, text="Password:", bg="#ffffff", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
    reg_password_entry = tk.Entry(register_frame, show="*", width=40, font=("Arial", 12))
    reg_password_entry.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(register_frame, text="Role:", bg="#ffffff", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
    role_var = tk.StringVar(value="organizer")
    tk.Radiobutton(register_frame, text="Organizer", variable=role_var, value="organizer", bg="#ffffff", font=("Arial", 12)).grid(row=3, column=1, sticky="w")
    tk.Radiobutton(register_frame, text="Attendee", variable=role_var, value="attendee", bg="#ffffff", font=("Arial", 12)).grid(row=4, column=1, sticky="w")

    tk.Button(register_frame, text="Register", command=register_user, bg="#4caf50", fg="white", font=("Arial", 12), relief="raised").grid(row=5, columnspan=2, pady=10)

setup_initial_screen()

# Start the Tkinter event loop
root.mainloop()
