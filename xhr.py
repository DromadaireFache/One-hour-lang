import sys
import os
from copy import deepcopy
from time import time
from random import random

def assert_error(assertion, msg="unspecifiedError ~ assertion failed"):
    if not assertion:
        print("Fatal:" + msg)
        # exit()
        raise Exception()

assert_error(len(sys.argv) == 2, "programArgumentError ~ please provide file path as argument")

class ArrayBuilder:
    def __init__(self):
        self.array = []
        self.finished = False
    
    def append(self, item):
        peek = self.peek()
        if isinstance(peek, ArrayBuilder) and peek.finished == False:
            self.array[-1].append(item)
        else:
            self.array.append(item)
    
    def finish(self, asTuple=False):
        peek = self.peek()
        if isinstance(peek, ArrayBuilder) and peek.finished == False:
            self.array.pop()
            self.array.append(peek.finish())
            return self
        else:
            self.finished = True
            return tuple(self.array) if asTuple else self.array
    
    def pop(self):
        peek = self.peek()
        if isinstance(peek, ArrayBuilder) and peek.finished == False:
            return self.array[-1].pop()
        else:
            assert_error(len(self.array) > 0, "arrayBuilderError ~ cannot pop from an empty stack")
            return self.array.pop()

    def peek(self):
        return self.array[-1] if len(self.array) > 0 else None
    
    def __str__(self):
        if len(self.array) == 0:
            return 'ArrayBuilder[]'
        return 'ArrayBuilder[ ' + ', '.join(map(str, self.array)) + ' ]'

class Stack:
    def __init__(self):
        self.stack = []
    
    def append(self, item):
        peek = self.peek()
        if isinstance(peek, ArrayBuilder) and peek.finished == False:
            self.stack[-1].append(item)
        else:
            self.stack.append(item)
    
    def pop(self, ignoreBuilder=False):
        if ignoreBuilder: return self.stack.pop()
        peek = self.peek()
        if isinstance(peek, ArrayBuilder) and peek.finished == False:
            return self.stack[-1].pop()
        else:
            assert_error(len(self.stack) > 0, "stackUnderflow ~ cannot pop from an empty stack")
            return self.stack.pop()
    
    def peek(self):
        return self.stack[-1] if len(self.stack) > 0 else None
    
    def __str__(self):
        return 'Stack( ' + ', '.join(map(str, self.stack)) + ' )'
    
    def __len__(self):
        return len(self.stack)

class Function(ArrayBuilder):
    def __init__(self):
        super().__init__()
        self.name = ''
        self.vars = None
        self.consts = None
    
    def __str__(self):
        return '{ ' + ' '.join(map(str, self.array)) + ' }'
    
    def finish(self):
        peek = self.peek()
        if isinstance(peek, Function) and peek.finished == False:
            peek.finish()
        else:
            self.finished = True

    def __iter__(self):
        return iter(self.array)
    
    def __len__(self):
        return len(self.array)
    
    def __getitem__(self, index):
        return self.array[index]
    
    def rename(self, name):
        self.name = name
        return
    
    def addNonLocals(self, vars, consts):
        self.vars = vars
        self.consts = consts
        return
    
    def __call__(self, stack: Stack):
        try:
            self.call(stack)
        except Exception as e:
            msg = f"runtimeError:{type(e).__name__} ~ runtime interpreter exception: here@{'~global~' if self.name == '' else self.name}"
            assert_error(False, msg)

    def call(self, stack: Stack):
        tokens: list[str] = self.array
        loopStack = []
        vars = self.vars if self.vars != None else {}
        consts = self.consts if self.consts != None else {}
        if self.name != '':
            consts[self.name] = self
        defFunc = ''
        loc = 0
        while loc < len(tokens):
            token = tokens[loc]
            
            if isinstance(token, Function):
                # print(defFunc, vars, consts)
                token.addNonLocals(vars, consts)
                if defFunc == '':
                    stack.append(token)
                else:
                    token.rename(defFunc)
                    consts[defFunc] = token
                    defFunc = ''
            
            elif token.replace('.', '', 1).isnumeric():
                try:
                    stack.append(int(token))
                except ValueError:
                    stack.append(float(token))

            elif token[0] == '-' and token[1:].replace('.', '', 1).isnumeric():
                try:
                    stack.append(int(token))
                except ValueError:
                    stack.append(float(token))
            
            elif token[0] == '"':
                stack.append(token[1:-1])

            
            else:
                match token:
                    case '+':
                        first = stack.pop()
                        stack.append(stack.pop() + first)
                    case '-':
                        first = stack.pop()
                        stack.append(stack.pop() - first)
                    case '*':
                        first = stack.pop()
                        stack.append(stack.pop() * first)
                    case '/':
                        first = stack.pop()
                        stack.append(stack.pop() / first)
                    case '=':
                        first = stack.pop()
                        stack.append(int(stack.pop() == first))
                    case '!=':
                        first = stack.pop()
                        stack.append(int(stack.pop() != first))
                    case '>':
                        first = stack.pop()
                        stack.append(int(stack.pop() > first))
                    case '<':
                        first = stack.pop()
                        stack.append(int(stack.pop() < first))
                    case '<=':
                        first = stack.pop()
                        stack.append(int(stack.pop() <= first))
                    case '>=':
                        first = stack.pop()
                        stack.append(int(stack.pop() >= first))
                    case '**':
                        first = stack.pop()
                        stack.append(stack.pop() ** first)
                    case 'print':
                        print(stack.pop())
                    case 'scan':
                        stack.append(input(stack.pop()))
                    case 'Null':
                        stack.append(None)
                    case 'int':
                        try:
                            stack.append(int(stack.pop()))
                        except:
                            assert_error(False, "typeError ~ cannot convert to an int")
                    case 'float':
                        try:
                            stack.append(float(stack.pop()))
                        except:
                            assert_error(False, "typeError ~ cannot convert to float")
                    case 'str':
                        stack.append(str(stack.pop()))
                    case 'dup':
                        top = stack.pop()
                        stack.append(top)
                        stack.append(top)
                    case '2dup':
                        top = stack.pop(), stack.pop()
                        stack.append(top[0])
                        stack.append(top[0])
                        stack.append(top[1])
                        stack.append(top[1])
                    case 'swap':
                        top = stack.pop(), stack.pop()
                        stack.append(top[0])
                        stack.append(top[1])
                    case 'rot':
                        top = stack.pop(), stack.pop(), stack.pop()
                        stack.append(top[0])
                        stack.append(top[2])
                        stack.append(top[1])
                    case 'drop':
                        stack.pop()
                    case 'set':
                        value, index, array = stack.pop(), stack.pop(), stack.pop()
                        assert_error(isinstance(array, list), "argumentError ~ `set` expected array, instead got: " + str(array))
                        assert_error(0 <= index < len(array), "indexOutOfBoundsError ~ index out of bounds" + str(index) + 'for array: ' + str(array))
                        array[index] = value
                    case 'get':
                        index, array = stack.pop(), stack.pop()
                        assert_error(isinstance(array, list), "argumentError ~ `get` expected array, instead got: " + str(array))
                        assert_error(0 <= index < len(array), "indexOutOfBoundsError ~ index out of bounds" + str(index) + 'for array: ' + str(array))
                        stack.append(array[index])
                    case 'len':
                        assert_error(isinstance(stack.peek(), list), "argumentError ~ `len` expected array, instead got: " + str(stack.peek()))
                        stack.append(len(stack.pop()))
                    case '...':
                        array = stack.pop()
                        assert_error(isinstance(array, list), "argumentError ~ `...` expected array, instead got: " + str(array))
                        for el in array:
                            stack.append(el)
                    case 'time':
                        stack.append(time())
                    case 'rand':
                        stack.append(random())
                    case 'array':
                        assert_error(isinstance(stack.peek(), int), "argumentError ~ `array` expected int, instead got: " + str(stack.peek()))
                        assert_error(stack.peek() >= 0, "argumentError ~ `array` expected non-negative int, instead got: " + str(stack.peek()))
                        stack.append([None] * stack.pop())
                    case 'push':
                        value, array = stack.pop(), stack.pop()
                        assert_error(isinstance(array, list), "argumentError ~ `push` expected array, instead got: " + str(array))
                        array.append(value)
                    case 'pop':
                        array = stack.pop()
                        assert_error(isinstance(array, list), "argumentError ~ `pop` expected array, instead got: " + str(array))
                        assert_error(len(array) > 0, "indexOutOfBoundsError ~ cannot pop from an empty array")
                        stack.append(array.pop())
                    case '!':
                        func = stack.pop()
                        assert_error(isinstance(func, Function), "functionCallError ~ cannot call a non-function: " + str(func))
                        func(stack)
                    case 'Special:debug':
                        print("Special:debug ~", stack)
                    case 'Special:exit':
                        try:
                            code = stack.pop()
                            print("Special:exit ~ Exiting with code:", code)
                            exit(int(code))
                        except:
                            exit()
                    case 'Exception:throw':
                        assert_error(False, "throw ~ " + str(stack.pop()))
                    case 'while':
                        loopStack.append(('while', loc))
                    case 'if':
                        loopStack.append(('if', loc))
                    case 'else':
                        condType, condLoc = loopStack.pop()
                        if condType == 'if':
                            conditionalsCount = 1
                            while conditionalsCount != 0:
                                loc += 1
                                assert_error(loc < len(tokens), "syntaxError ~ `while` statements need an end particle")
                                if tokens[loc] in ('while', 'if'):
                                    conditionalsCount += 1
                                elif tokens[loc] == 'end':
                                    conditionalsCount -= 1
                        else:
                            assert_error(False, "syntaxError ~ else without if")
                    case 'end':
                        condType, condLoc = loopStack.pop()
                        if condType == 'while':
                            loopStack.append(('end', loc))
                            loc = condLoc - 1
                    case 'do':
                        if not bool(stack.pop()):
                            condType, condLoc = loopStack.pop()
                            conditionalsCount = 1
                            ifToElseCount = 0 if condType == 'while' else 1
                            while conditionalsCount != 0 and (ifToElseCount != 0 or condType == 'while'):
                                loc += 1
                                # print(tokens[loc], ifToElseCount, condType)
                                assert_error(loc < len(tokens), "syntaxError ~ `while` statements need an end particle")
                                assert_error(ifToElseCount >= 0, "syntaxError ~ `else` without `if`")
                                if tokens[loc] == 'while':
                                    conditionalsCount += 1
                                elif tokens[loc] == 'if':
                                    conditionalsCount += 1
                                    ifToElseCount += 1
                                elif tokens[loc] == 'else':
                                    ifToElseCount -= 1
                                elif tokens[loc] == 'end':
                                    conditionalsCount -= 1
                            
                            if ifToElseCount == 0 and condType != 'while':
                                loopStack.append(('else', loc))
                    case '[':
                        stack.append(ArrayBuilder())
                    case ']':
                        arr = stack.pop(ignoreBuilder=True)
                        assert_error(isinstance(arr, ArrayBuilder), "syntaxError ~ missing `[` in array declaration")
                        stack.append(arr.finish())
                    case _:
                        if token[0] == '=':
                            name = token[1:]
                            assert_error(len(token) > 1, "syntaxError ~ variable needs name: " + token)
                            assert_error(name.isidentifier(), "syntaxError ~ invalid variable name: " + name)
                            assert_error(name not in consts, "constantMeddlingError ~ cannot assign to a constant: " + name)
                            vars[name] = stack.pop()
                            # if isinstance(vars[name], Function):
                            #     vars[name].vars['var'] = 69
                            #     print(name, id(vars[name]))
                            #     print(vars[name].vars, id(vars[name].vars))
                        elif token[0] == ':':
                            name = token[1:]
                            assert_error(len(token) > 1, "syntaxError ~ variable needs name: " + token)
                            assert_error(name.isidentifier(), "syntaxError ~ invalid variable name: " + name)
                            assert_error(name not in consts, "constantMeddlingError ~ cannot reassign a constant: " + name)
                            consts[name] = stack.pop()
                        elif token[0] == '!':
                            name = token[1:]
                            assert_error(len(token) > 1, "syntaxError ~ function call needs name: " + token)
                            thing = searchFor(name, vars, consts)
                            assert_error(thing != None, "nameError ~ function does not exist: " + name)
                            assert_error(isinstance(thing, Function), "functionCallError ~ cannot call a non-function: " + name)
                            thing(stack)
                        elif token[:4] == 'def:':
                            assert_error(len(token) > 4, "syntaxError ~ function needs name: " + token)
                            name = token[4:]
                            assert_error(name.isidentifier(), "syntaxError ~ invalid function name: " + name)
                            assert_error(name not in consts, "nameError ~ function exists as a constant: " + name)
                            assert_error(name not in vars, "nameError ~ function exists as a variable: " + name)
                            defFunc = name
                        elif token[:7] == 'import!':
                            assert_error(len(token) > 7, "syntaxError ~ import needs name: " + token)
                            name = token[7:]
                            assert_error(name not in consts, "nameError ~ import exists as a constant: " + name)
                            assert_error(name not in vars, "nameError ~ import exists as a variable: " + name)
                            modules = name.split('.')
                            if modules[0] == '':
                                importDir = '..'
                                modules = modules[1:]
                            else:
                                importDir = '.'
                            withinFileModules = modules[:]
                            importModuleName = ""
                            path = ".xhr"
                            for module in modules:
                                path = path[:-4] + '/' + module + path[-4:]
                                importModuleName += '.' + withinFileModules.pop(0)
                                if os.path.isfile(importDir + path):
                                    importedModule = readFile(importDir + path)
                                    withinFileModules = '.'.join(withinFileModules)
                                    if withinFileModules == '':
                                        consts[importModuleName[1:]] = importedModule
                                    else:
                                        consts[withinFileModules] = searchFor(withinFileModules, importedModule.vars, importedModule.consts)
                                        assert_error(consts[withinFileModules] != None, "nameError ~ module not found: " + name)
                                    break
                            
                            assert_error(os.path.isfile(importDir + path), "invalidFileError ~ file not found: " + importDir + path)

                        else:
                            if token in consts:
                                const = consts[token]
                                if isinstance(const, Function):
                                    if defFunc != '':
                                        consts[defFunc] = const
                                    else:
                                        stack.append(deepcopy(const))
                                else:
                                    stack.append(const)
                            elif token in vars:
                                var = vars[token]
                                if isinstance(var, Function) and defFunc != '':
                                    if defFunc != '':
                                        consts[defFunc] = const
                                    else:
                                        stack.append(deepcopy(const))
                                else:
                                    stack.append(var)
                            else:
                                thing = searchFor(token, vars, consts)
                                assert_error(thing != None, "syntaxError ~ unknown symbol: " + token)
                                stack.append(thing)
            loc += 1
        self.vars = vars
        self.consts = consts

def searchFor(name, vars, consts):
    if '.' in name:
        module, name = name.split('.', 1)
        # print(module, name, module in consts)
        if module in vars:
            assert_error(isinstance(vars[module], Function), "nameError ~ module is not a function: " + module)
            assert_error(vars[module].consts != None and vars[module].vars != None,
                         "nameError ~ module has not been called: " + module)
            return searchFor(name, vars[module].vars, vars[module].consts)
        elif module in consts:
            assert_error(isinstance(consts[module], Function), "nameError ~ module is not a function: " + module)
            assert_error(consts[module].consts != None and consts[module].vars != None,
                         "nameError ~ module has not been called: " + module)
            return searchFor(name, consts[module].vars, consts[module].consts)
        else:
            return None
    elif name in vars:
        return vars[name]
    elif name in consts:
        return consts[name]
    else:
        return None
    
def readFile(path):
    assert_error(path.endswith('.xhr') or path.endswith('.1hr'), "invalidFileError ~ file must have .xhr or .1hr extension")
    assert_error(os.path.isfile(path), "invalidFileError ~ file not found: " + path)
    with open(path) as sourceFile:
        lines = sourceFile.readlines()
        tokens = Function()

        for line in lines:
            if len(line.strip()) != 0 and line.strip()[0] != '#':
                line = line.split('"')
                line[-1] = line[-1].split('#')[0]
                for i in range(len(line)):
                    if i % 2 == 0:
                        lSplit = line[i].split()
                        for token in lSplit:
                            if token == '{':
                                tokens.append(Function())
                            elif token == '}':
                                peek = tokens.peek()
                                # print(tokens)
                                assert_error(isinstance(peek, Function),
                                            "syntaxError ~ missing `{` in function body declaration: " + '"'.join(line)[:-1])
                                peek.finish()
                            else:
                                tokens.append(token)
                    else:
                        tokens.append('"' + line[i] + '"')
        
        peek = tokens.peek()
        assert_error(not isinstance(peek, Function) or peek.finished,
                     "syntaxError ~ missing `{` in function body declaration")
        stack = Stack()
        tokens(stack)
        return tokens

try:
    readFile(sys.argv[1])
except Exception as e:
    # raise e
    pass