# Python Fundamentals Practice

A collection of Python exercises and projects built while learning Python fundamentals on a path toward a **Junior Data Engineer** role.

---

## About

**Author:** Muhammad Faizan  
**Goal:** Junior Data Engineer within 12 months  
**Stack:** Python → SQL → Cloud → Portfolio → Job  

---

## Folder Structure

```
Python_Fundamentals_Practice/
├── Excercises/       # Structured exercises covering core Python concepts
└── Games/            # Mini projects built independently
```

---

## Exercises (`Excercises/`)

| File | Concepts Covered |
|------|-----------------|
| `list_operations.py` | List indexing, `.append()`, `.pop()`, slicing |
| `dict_operations.py` | Dictionary creation, `.items()`, `.keys()`, `.values()` |
| `grade_checker.py` | Functions, `if/elif/else`, `while True` loop, `ValueError` handling |
| `save_names.py` | File I/O — writing to a `.txt` file with `open()` |
| `load_names.py` | File I/O — reading from a `.txt` file, `.strip()`, `.readlines()` |
| `safe_file_read.py` | Error handling — `FileNotFoundError`, returning `None` safely |
| `safe_divide.py` | Error handling — `ZeroDivisionError`, `TypeError` |
| `age_validator.py` | Input validation loop, `ValueError`, range checking |
| `list_comprehension.py` | List comprehensions — filter, transform, combined |
| `scores_stats.py` | Data-style stats — average, max, passing count using list comprehensions |

---

## Games (`Games/`)

### Number Guessing Game — `num guess.py`
- Generates a random number between 1–10
- Player guesses until correct
- Tracks number of attempts
- Handles invalid input with `try/except ValueError`
- **Modules used:** `random`

### Rock Paper Scissors — `Rock paper Scissor.py`
- Full game logic with all 9 win/lose/tie conditions
- Computer picks randomly each round
- Input validation — rejects anything not in `["rock", "paper", "scissors"]`
- Play again feature
- **Modules used:** `random`

---

## Key Concepts Learned

- **Variables, loops, conditionals** — core Python syntax
- **Functions** — `def`, parameters, `return` values
- **File I/O** — `open()`, `read()`, `write()`, `readlines()`, `.strip()`
- **Error handling** — `try/except` with `ValueError`, `ZeroDivisionError`, `FileNotFoundError`, `TypeError`
- **List comprehensions** — filter and transform lists in one line
- **Dictionaries** — storing and iterating over structured data
- **Random module** — `random.randint()`, `random.choice()`

---

## Projects Built

| Project | Description |
|---------|-------------|
| To-Do List App | Menu-driven app to add, view, and delete tasks |
| Number Guessing Game | Random number game with attempt counter and error handling |
| Rock Paper Scissors | Full RPS game with input validation and play-again loop |
| Student Report Card | Combines dicts, functions, loops and list comprehensions to generate grades |

---

## Learning Roadmap

- [x] Python fundamentals (variables, loops, functions, file I/O, error handling)
- [x] List comprehensions
- [x] Built mini projects independently (no Copilot)
- [ ] Pandas & data manipulation
- [ ] SQL basics
- [ ] Python + SQL integration
- [ ] ETL pipeline project
- [ ] Cloud basics (AWS/Azure)
- [ ] Junior Data Engineer role
