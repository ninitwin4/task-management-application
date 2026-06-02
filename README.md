# 📋 Task Management Application

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

> *A command-line tool that helps small business teams manage, track, and report on their tasks.*

---

## 🌟 Highlights

- Secure login with username and password authentication
- Role-based access — **admin** and **regular users** see different menus
- Add, view, edit, complete, and delete tasks from the command line
- Tasks and users stored persistently in text files
- Admin can generate reports and view detailed statistics
- Recursive input validation and defensive error handling throughout
- Users can only edit their own tasks — secure by design

---

## ℹ️ Overview

**Task Management Application** is an intermediate Python project built as a capstone assignment. It simulates a real-world scenario where a small business needs a command-line tool to manage tasks assigned to each team member.

The program uses core Python concepts like file I/O, functions, dictionaries, loops, exception handling, and recursion to deliver a fully working task management system — complete with authentication, role-based permissions, and automated reporting.

### ✍️ Author

**NiNi** — [@ninitwin4](https://github.com/ninitwin4)

---

## 🚀 Usage

When you run the program, you'll be prompted to log in. Once authenticated, you'll see a menu based on your role:

```
Enter username: admin
Enter password: adm1n

Welcome, admin!

Please select one of the following options:
r  - register a user
a  - add task
va - view all tasks
vm - view my tasks
vc - view completed tasks
del - delete a task
gr - generate reports
ds - display statistics
e  - exit
```

**Example — Viewing My Tasks:**
```
Enter your choice: vm

----------------------------------------
Task 1:
Task:             Fix login bug
Assigned to:      admin
Due date:         30 Jun 2026
Task Complete?    No
----------------------------------------
Enter task number or -1 to return: 1
What would you like to do? c - mark complete, e - edit: c

Task marked as complete!
```

---

## ⬇️ Installation

### Prerequisites

- Python 3.x installed on your machine. Check by running:

```bash
python --version
```

If you don't have Python, download it from [python.org](https://www.python.org/downloads/).

### Steps

1. **Clone the repository:**

```bash
git clone https://github.com/ninitwin4/task-management-application.git
```

2. **Navigate into the project folder:**

```bash
cd task-management-application
```

3. **Run the program:**

```bash
python task_manager.py
```

> No external libraries needed — the program only uses Python's built-in `datetime` module. ✅
>
> Make sure `task_manager.py`, `user.txt`, and `tasks.txt` are all in the same folder. The default login is username `admin`, password `adm1n`.

---

## 📁 File Structure

```
task-management-application/
│
├── task_manager.py       # Main program
├── user.txt              # Stores usernames and passwords
├── tasks.txt             # Stores all task data
├── task_overview.txt     # Generated task statistics report
└── user_overview.txt     # Generated user statistics report
```

---

## 🔐 Roles and Permissions

| Feature | Admin | Regular User |
|---------|:-----:|:------------:|
| Register new user | ✅ | ❌ |
| Add task | ✅ | ✅ |
| View all tasks | ✅ | ✅ |
| View my tasks | ✅ | ✅ |
| Mark task complete | ✅ | ✅ (own only) |
| Edit task | ✅ | ✅ (own only) |
| View completed tasks | ✅ | ❌ |
| Delete tasks | ✅ | ❌ |
| Generate reports | ✅ | ❌ |
| Display statistics | ✅ | ❌ |

---

## 💭 Feedback and Contributing

Found a bug or have a feature idea? Feel free to open an issue or start a discussion in the repo. Contributions and suggestions are always welcome! 😊
