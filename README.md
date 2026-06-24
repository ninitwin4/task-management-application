# 📋 Task Management Application — A Refactor Story

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-unittest-success)
![Lint](https://img.shields.io/badge/Lint-Flake8%20clean-brightgreen)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

> **One application, two architectures.** This repository shows the same task
> manager built first as a working procedural script (`v1`), then re-engineered
> into a clean, layered, test-covered application (`v2`) — the way production
> teams actually structure code.

---

## 🧭 The Story: Before → After

I originally built this task manager as a single-file Python program. It worked,
and it was feature-rich — login, role-based permissions, reporting, the lot. But
everything lived in one file, file access was scattered across every function,
and none of it could be unit tested without touching real files.

So I refactored it. **`v2` keeps the same core behaviour but re-architects it**
into separated layers using the repository and service patterns — the goal being
to demonstrate clean architecture, separation of concerns, and testability, not
to re-implement every feature. The procedural `v1` is preserved so the
before/after contrast is visible.

This is the arc I care about as an engineer: taking something that *works* and
making it something a team could *maintain*.

---

## 🆚 Before vs After

| Aspect | `v1` Procedural | `v2` OOP (Refactored) |
|---|---|---|
| Organisation | Single file | 5 layered modules |
| Paradigm | Functions + direct file I/O | Classes + repository/service |
| Data access | File reads/writes everywhere | Isolated in one data layer |
| Testability | Hard (logic tied to files & input) | Unit tested, logic isolated |
| Tooling | None | Flake8, venv, requirements.txt |
| Feature scope | Full (RBAC, reports, stats) | Focused core (login, add, view) |
| Best demonstrates | Feature breadth | Architectural maturity |

> ℹ️ **On scope:** `v2` is intentionally a focused *architectural* refactor. It
> reproduces the core flow (authenticate → add → view) cleanly rather than
> porting every `v1` feature. The point is the structure, not the surface area.

---

## 🏛️ The v2 Architecture

The refactor separates the program into layers, where each layer only talks to
the one directly below it:

```
main.py                → entry point (starts the app, nothing else)
   │
user_interface.py      → all menus, input, and output (the "front desk")
   │
business_logic.py      → Task, User, TaskService, UserService (the "manager")
   │
data_access.py         → raw text file read/write (the "loading dock")
   │
tasks.txt / user.txt
```

- **`data_access.py`** reads and writes *raw records* (lists of strings). It has
  no knowledge of `Task` or `User` — fully decoupled from the domain.
- **`business_logic.py`** owns the domain classes and the services that convert
  raw records into objects and back. This is the only layer that understands
  what a "task" actually *is*.
- **`user_interface.py`** handles every `input` and `print`. It asks the
  services to do work; it never touches files itself.
- **`main.py`** does one job: start the application.

---

## 🧪 Testing

`v2/tests.py` contains isolated unit tests that verify the business logic without
relying on any file structure — exactly because the logic was decoupled from
file access during the refactor:

```bash
cd v2-oop
python -m unittest tests -v
```

Tests cover password verification, task completion, and overdue detection. Each
test is self-documenting via a docstring that appears in the verbose runner.

---

## 📁 Repository Structure

```
task-management-application/
├── README.md
├── v1-procedural/
│   ├── task_manager.py       # original single-file program
│   ├── user.txt
│   └── tasks.txt
└── v2-oop/
    ├── main.py               # entry point
    ├── user_interface.py     # menus + input/output
    ├── business_logic.py     # Task, User, services
    ├── data_access.py        # raw file read/write
    ├── tests.py              # isolated unit tests
    ├── requirements.txt
    ├── user.txt
    └── tasks.txt
```

---

## 🚀 Running Each Version

**v1 (procedural):**
```bash
cd v1-procedural
python task_manager.py
```

**v2 (OOP):**
```bash
cd v2-oop
python main.py
```

> Default login — username `admin`, password `adm1n`. Make sure `user.txt` and
> `tasks.txt` sit in the same folder as the code.

---

## 💡 What the Refactor Taught Me

- **Separation of concerns** — each layer has one responsibility, so a change in
  one rarely ripples into another.
- **Decoupling** — keeping the data layer ignorant of the domain means `Task` can
  evolve without breaking file access.
- **Designing for testability** — pulling pure logic out of file/input
  dependencies (e.g. passing `today` into the overdue check rather than reading
  the clock inside it) is what makes fast, reliable unit tests possible.
- **Dependency direction** — higher layers depend on lower ones, never the
  reverse.

---

## ✍️ Author

**NiNi** — [@ninitwin4](https://github.com/ninitwin4)

*Operator turned builder — from design and ops into engineering.*
