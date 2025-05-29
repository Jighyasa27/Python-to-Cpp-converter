# 🌀 Python to C++ Compiler

A custom-built compiler that translates a subset of Python code into equivalent C++ code using Python’s built-in `ast` module.

---

## 📚 Description

This project parses Python source code using the Abstract Syntax Tree (AST), walks the tree, and converts recognized structures (functions, variables, loops, conditionals, expressions, etc.) into C++ syntax.

Supports:
- Variable assignment
- Arithmetic operations
- Function definitions & calls
- `if`, `elif`, `else` conditions
- `for` loops (based on `range`)
- `while` loops
- `print()` statements

---

## 🛠️ Features

- AST-based code parsing
- Modular design using the Visitor pattern
- Converts both manual and file-based input
- Saves generated C++ output to `.cpp` file
- Handles common Python constructs

---

## 📁 Project Structure

project/
│
├── main.py # Entry point (user interface + compiler usage)
├── util/
│ ├── core.py # Compiler class using ast.NodeVisitor
│ ├── statements.py # Handlers for if, while, for, assign, etc.
│ ├── expressions.py # Expression & operator translation
│ └── functions.py # Function definition handling
│
├── test/ # Sample Python input test files
│ └── test1.py # Example: add.py, condition.py, loop.py etc.
│
├── output/ # Generated C++ files are saved here
│
└── README.md # Project documentation



