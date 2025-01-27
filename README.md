1hr - A Stack-Based Programming Language made in 1 hour

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

## Xhr: The Extended 1hr

**Xhr** is an evolved version of **1hr**, built on the same stack-based foundations but adding broader programming capabilities:

- **Same Core**: All existing commands remain compatible, ensuring full backward compatibility with 1hr code.
- **Constants**: Define variables that cannot be reassigned at runtime.
- **Else blocks**: Execute conditional code in case an if block does not evaluate to true.
- **Arrays**: Create and manipulate indexed collections of values. Arrays support basic operations like indexing (`get`), setting values (`set`), and retrieving array length (`len`). Arrays can store any type of value and are zero-indexed.
- **New operations**: 
- **Functions**: Define blocks of code that can be invoked with parameters. Functions can push or pop values to interact with the stack and simplify code reuse.
- **Simple Object-Oriented Programming**: You can define objects that contain data and methods. There is no inheritance, keeping the language minimal while still allowing some encapsulation of related functionality.

### Constants
Constants are read-only variables defined using `:` instead of `=` when assigning a value. Once assigned, their values cannot be changed during program execution.

```xhr
# Define a constant PI
3.14159 :PI

# Define a greeting message
"Hello!" :GREETING

# Use constants in calculations
PI 2 * print  # Prints: 6.28318
GREETING print  # Prints: Hello!

# Attempting to modify a constant results in an error
5 :PI  # Error: Cannot redefine constant 'PI'
```

### Else blocks
The `if ... do ... else ... end` construct allows you to execute different code blocks based on a condition. If the condition (top of stack) is non-zero, the code between `do` and `else` executes. Otherwise, the code between `else` and `end` executes.

```xhr
# Example of if-else usage
5 10
if < do
    "5 is less than 10" print
else
    "5 is not less than 10" print
end

# Multiple conditions with if-else
"Enter age: " scan int =age
if age 18 >= do
    "You are an adult" print
else
    "You are a minor" print
end
```

### Arrays
Arrays in Xhr are dynamic collections of values. They support various operations for creation, access, and manipulation:

```xhr
# Creating arrays
[ 1 2 3 ] =numbers   # Array literal
3 array =empty       # Creates array of size 3 for of `None`

# Accessing elements (zero-based)
numbers 0 get print  # Prints first element: 1

# Setting elements
numbers 1 5 set      # Sets second element to 5

# Array length
numbers len print    # Prints: 3

# Array operations
numbers empty +      # Concatenates numbers and empty
numbers 4 push       # Pushes 4 at the end of the array
numbers pop          # Pops from numbers and pushes that value onto the stack
```

Arrays can store mixed types and be nested. Common operations:
- `[ ... ]`: Creates an array literal, anything can be inside there (function calls, other arrays, etc.) as they are evaluated at runtime
- `array`: Creates new array of specified size
- `get`: Gets element at index
- `set`: Sets element at index
- `len`: Gets array length
- `push`: Pushes a value to the end of the array
- `pop`: Pops the value at the end of the array onto the stack

### Functions
Functions in **Xhr** are defined using curly braces `{}`, creating function blocks that are pushed onto the stack. These function blocks can be assigned to variables or constants, stored within arrays, and manipulated just like any other data type.

To define a function within its own scope—preventing the function block from being pushed onto the stack—use the `def:` keyword followed by the function name and the function block.

#### Defining and Assigning Functions
```xhr
# Assign a function to a variable/constant
{ "Hello, World!" print } =greet

# Define a scoped function
def:farewell { "Goodbye!" print }
```

#### Calling Functions
```xhr
# Call the assigned function
!greet

# Call the scoped function
!farewell
```
Output:
```
Hello, World!
Goodbye!
```

#### Storing Functions in Arrays
```xhr
# Create an array of functions
[ { "Function 1" print } { "Function 2" print } ] =functionArray

# Call functions from the array
functionArray 0 get !
functionArray 1 get !
```
Output:
```
Function 1
Function 2
```

#### Passing Arguments to functions via the stack
```xhr
def:tripleSum { + + print }
1 3 5 !tripleSum
```
Output:
```
9
```

Functions provide a powerful way to encapsulate reusable code blocks, enabling more organized and modular programs in **Xhr**.

### Object oriented programming

**Xhr** supports object-oriented programming by allowing the creation of objects that contain variables and methods (functions) within their scope. This encapsulation facilitates code reuse and organization.

#### Defining Objects

```xhr
def:obj {
    Null =var
    def:printVar {
        var print
    }
    def:set_var {
        =var
    }
} !obj

obj :instance
obj :instance2
5 !instance.set_var
10 !instance2.set_var
!obj.printVar
!instance.printVar
!instance2.printVar
```
Output:
```
Null
5
10
```

#### Inheritance

Inheritance enables one object to acquire properties and methods from another, promoting code reuse and scalability.

```xhr
def:parent {
    Null =name
    { =name } =set_name
    { name print } =print_name
} !parent

def:child { !parent
    def:set_age {
        =age
    }
    def:print_age {
        age print
    }
} !child

child :child_instance
child :child_instance2
"ParentName" !child_instance.set_name
"ChildName" !child_instance2.set_name
30 !child_instance.set_age
25 !child_instance2.set_age
!child_instance.print_name
!child_instance.print_age
!child_instance2.print_name
!child_instance2.print_age
```
Output:
```
ParentName
30
ChildName
25
```

In this example, the `child` object inherits from the `parent` object, gaining access to its `set_name` and `print_name` methods (which have to be assigned to variables, not defined) while also introducing new methods `set_age` and `print_age`. This structure allows `child` objects to utilize and extend the functionality of `parent` objects.

### Importing modules

**Xhr** allows you to extend its functionality by importing modules. Use the `import!` command followed by the module name to include a module in your program.

#### Example 1: Standard Library Module

```xhr
import!Std
[ "The number is " 5 ] !Std.printf
```
**Output:**
```
The number is 5
```

#### Example 2: Math Module

```xhr
import!Std.Math
-12 -25 25 -100 100 !Math.mapRange print
```
**Output:**
```
-48
```

---

## Author
This language was created as a fun and educational coding challenge. Enjoy experimenting with **1hr**, or try out **Xhr** for extended functionality! 1hr - A Stack-Based Programming Language made in 1 hour