# DecodeLab Internship Projects

A collection of Python projects developed during my DecodeLab internship. These projects show my progress in Python programming, problem-solving, data handling, input validation, and basic security concepts.

# Projects

### 1. To-Do List Manager

A command-line task management application that allows users to create, view, and delete tasks.

**Features**
- Add new tasks
- View all tasks
- Delete tasks by task number
- Prevent empty task titles
- Handle invalid task-number input
- Interactive menu-driven interface

**Python Concepts Used**
Functions, lists and dictionaries, loops and conditionals, user input handling, exception handling, program entry point with `if __name__ == "__main__"`.

---

### 2. Expense Tracker

A command-line expense tracking application for recording expenses and calculating total spending.

**Features**
- Enter expenses one by one
- Display the current expense list
- Calculate the running total
- Display the final total spent
- Reject negative expense values
- Handle invalid numeric input
- Stop the program using `stop` or `exit`

**Python Concepts Used**
Functions, lists, floating-point calculations, accumulator pattern, input validation, try/except error handling, loop control and sentinel values.

---

### 3. Password Generator

A secure password-generation project that creates random passwords using Python's `secrets` module and calculates their information entropy.

**Features**
- Custom password length
- Default length of 16 characters
- Lowercase and uppercase letters
- Digits and punctuation
- Cryptographically stronger random selection using `secrets.choice()`
- Information entropy calculation
- Password-strength assessment
- Generate multiple passwords in one session
- Input validation for password length

**Python Concepts Used**
`secrets`, `string`, `math`, functions and type hints, list comprehensions, string manipulation, mathematical entropy calculation, exception handling.

**Entropy Calculation**

The project estimates password entropy using:

```
Entropy = password length × log2(character pool size)
```

The program then classifies the calculated entropy as Weak, Moderate, or Enterprise Strong according to the thresholds implemented in the project.

> Note: These security labels are based on thresholds implemented in this project and should not be treated as a formal certification or guarantee of password security.

---

# Technologies

- Python 3
- Functions and modular programming
- Lists and dictionaries
- Exception handling
- Input validation
- String manipulation
- Basic mathematical calculations
- Secure random generation

# Repository Structure


DecodeLab-Internship-Projects/
│
├── To-Do-List/
│   ├── PROJECT_1.py
│   └── README.md
│
├── Expense-Tracker/
│   ├── PROJECT_2.py
│   └── README.md
│
├── Password-Generator/
│   ├── PROJECT-3.py
│   └── README.md
│
└── README.md


# How to Run

Make sure Python 3 is installed, then run the required project from the terminal:


python PROJECT_1.py
python PROJECT_2.py
python PROJECT-3.py


##Learning Outcomes

Through these projects, I am developing practical experience with:

- Python programming fundamentals
- Problem-solving and program logic
- Working with collections and application state
- Input validation and error handling
- Writing reusable functions
- Basic security and entropy concepts
- Building interactive command-line applications

# Future Improvements

Possible improvements for future versions include:

- Persistent data storage
- Better task and expense editing
- Search and filtering
- Unit testing
- Improved validation
- Graphical user interfaces
- Database integration
- More advanced Python and AI-based features

# About

I am a BS Artificial Intelligence student building my programming foundation through practical projects and internship experience.

This repository represents my learning journey and the projects I am developing as I continue improving my Python and software development skills.

> Learn. Build. Improve. Repeat.
# Acknowledgment

These projects were developed as part of my DecodeLab Internship to gain hands-on programming experience and strengthen my understanding of Python through practical implementation.
