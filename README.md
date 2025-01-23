# 1hr - A Stack-Based Programming Language made in 1 hour

## Overview

**1hr** is a minimalist stack-based programming language, created as part of a one-hour coding challenge. Only the `1hr.py` and `program.1hr` files were written within the hour-long challenge and were not altered afterwards. This `README.md` file and everything in `after-hour-showcases/` was written afterwards. Inspired by Forth and Tsoding's [Porth](https://gitlab.com/tsoding/porth), this language showcases simplicity and utility, interpreted directly via Python. Programs are written in `.1hr` files, featuring essential stack manipulation and arithmetic operations. Check out [this](https://github.com/DromadaireFache/1hr-language-vscode-extention.git) extension that provides language support and syntax highlighting for the 1hr programming language in Visual Studio Code.

**No A.I. was used to enhance nor speedup the process of coding this language!**

### Features:
- **Stack-based design**: Operates by pushing and popping values to/from a stack.
- **Error handling**: Provides meaningful error messages for invalid operations.
- **Interpreted**: Python acts as the interpreter.
- **Minimalist syntax**: Focused on essential operations.
- **Support for syntax highlighting on VSCode**: Keywords, comments, strings, types, etc.

---

## Supported Operations

Here is a list of all operations supported by **1hr**:

### Arithmetic Operations
- `+` : Adds the top two elements on the stack.
- `-` : Subtracts the second element on the stack from the top element.
- `*` : Multiplies the top two elements on the stack.
- `/` : Divides the second element on the stack by the top element.
- `**` : Raises the second element on the stack to the power of the top element.

### Comparison Operations
- `=` : Pushes `1` if the top two elements are equal, otherwise `0`.
- `!=` : Pushes `1` if the top two elements are not equal, otherwise `0`.
- `>` : Pushes `1` if the second element is greater than the top element, otherwise `0`.
- `<` : Pushes `1` if the second element is less than the top element, otherwise `0`.
- `>=` : Pushes `1` if the second element is greater than or equal to the top element, otherwise `0`.
- `<=` : Pushes `1` if the second element is less than or equal to the top element, otherwise `0`.

### Stack Manipulation
- `dup` : Duplicates the top element of the stack.
- `2dup` : Duplicates the top two elements of the stack.
- `swap` : Swaps the top two elements of the stack.
- `rot` : Rotates the top three elements of the stack.

### Input/Output
- `print` : Prints the top element of the stack.
- `scan` : Prints the top element of the stack, and then reads input from the user and pushes it onto the stack.

### Type Conversion
- `int` : Converts the top element to an integer.
- `float` : Converts the top element to a floating-point number.
- `str` : Converts the top element to a string.

### Control Flow
- `while ... do ... end` : Executes a loop while the top of the stack is not equal to `0`.
- `if ... do ... end` : Executes conditional code if the top of the stack is not equal to `0`.

### Variables
- `=name` : Stores the top element of the stack in a variable named `name`.
- `name` : Pushes the value of the variable `name` onto the stack.

---

## Writing Code in 1hr

Code for **1hr** is written in `.1hr` files. Lines starting with `#` are treated as comments and ignored by the interpreter. Example files showcase typical usage.

### Examples

#### Printing "Hello, World!"
```1hr
"Hello, World!" print
```
Output:
```
Hello, World!
```

#### Simple Arithmetic
```1hr
5 3 + print
10 2 / print
```
Output:
```
8
5.0
```

#### Conditional Execution
```1hr
if 3 5 < do "5 is greater than 3" print end
if 3 5 > do "This won't print" print end
```
Output:
```
5 is greater than 3
```

#### Loops
```1hr
3 =count
while
    count 0 >=
do
    count print
    count 1 - =count
end
```
Output:
```
3
2
1
```

#### If statements
```1hr
"Enter a number: " scan int
if 4 > do
    "This number is greater than 4" print
end
```
Output:
```
Enter a number: 69
This number is greater than 4
```

## Running a 1hr Program

To run a `.1hr` file, execute the Python interpreter script:

```bash
python3 1hr.py path/to/yourFile.1hr
```

### Example:
```bash
python3 1hr.py calculator.1hr
```

---

## Error Handling
- `error 1` : Missing or incorrect number of arguments to the interpreter.
- `error 2` : File not found or inaccessible.
- `unknown symbol: ...` : Undefined variable or operation.
- `cannot convert to an int` : Invalid conversion to an integer.
- `cannot convert to float` : Invalid conversion to a float.

---

## Installation for syntax highlighting extension

1. Open Visual Studio Code.
2. Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window.
3. Search for `1hr Language Support`.
4. Click `Install`.

## Author
This language was created as a fun and educational coding challenge. Enjoy experimenting with **1hr**!
