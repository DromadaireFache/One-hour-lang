# 1hr - A Stack-Based Programming Language made in 1 hour

## Overview

**1hr** is a minimalist stack-based programming language, created as part of a one-hour coding challenge. To be clear, only the `1hr.py` and `program.1hr` files were  written within the hour-long challenge. This `README.md` file and everything in `after-hour-showcases/` was written afterwards, but python-based interpreter for **1hr** was not altered. Inspired by Forth and Tsoding's [Porth](https://gitlab.com/tsoding/porth), this language showcases simplicity and utility, interpreted directly via Python. Programs are written in `.1hr` files, featuring essential stack manipulation and arithmetic operations.

### Features:
- **Stack-based design**: Operates by pushing and popping values to/from a stack.
- **Error handling**: Provides meaningful error messages for invalid operations.
- **Interpreted**: Python acts as the interpreter.
- **Minimalist syntax**: Focused on essential operations.

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

#### Simple Arithmetic
```1hr
5 3 + print # Outputs: 8
10 2 / print # Outputs: 5.0
```

#### Conditional Execution
```1hr
if 3 5 > do "This won't print" print end
if 3 5 > do "This won't print" print end
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
    "This number is greater that 4" print
end
```

## Running a 1hr Program

To run a `.1hr` file, execute the Python interpreter script:

```bash
python3 1hr.py path/to/yourFile.1hr
```

### Example:
```bash
python3 1hr.py simpleCalculator.1hr
```

---

## Error Handling
- `error 1` : Missing or incorrect number of arguments to the interpreter.
- `error 2` : File not found or inaccessible.
- `unknown symbol: ...` : Undefined variable or operation.
- `cannot convert to an int` : Invalid conversion to an integer.
- `cannot convert to float` : Invalid conversion to a float.

---

## Author
This language was created as a fun and educational coding challenge. Enjoy experimenting with **1hr**!