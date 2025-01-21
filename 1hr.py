import sys
import os

def assert_error(assertion, msg="1hr interpreter error"):
    if not assertion:
        print(msg)
        exit()

assert_error(len(sys.argv) == 2, "error 1")
assert_error(os.path.isfile(sys.argv[1]), "error 2")

with open(sys.argv[1]) as sourceFile:
    lines = sourceFile.readlines()

    tokens: list[str] = []

    for line in lines:
        if len(line.strip()) != 0 and line.strip()[0] != '#':
            line = line.split('"')
            for i in range(len(line)):
                if i % 2 == 0:
                    tokens.extend(line[i].split())
                else:
                    tokens.append('"' + line[i])
    
    stack = []
    loopStack = []
    vars = {}
    loc = 0
    while loc < len(tokens):
        token = tokens[loc]
        if token.replace('.', '', 1).isnumeric():
            try:
                stack.append(int(token))
            except ValueError:
                stack.append(float(token))
        
        elif token[0] == '"':
            stack.append(token[1:])
        
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
                case 'int':
                    try:
                        stack.append(int(stack.pop()))
                    except:
                        assert_error(False, "cannot convert to an int")
                case 'float':
                    try:
                        stack.append(float(stack.pop()))
                    except:
                        assert_error(False, "cannot convert to float")
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
                    stack.append(top[1])
                    stack.append(top[2])
                    stack.append(top[0])
                case 'while':
                    loopStack.append(('while', loc))
                case 'if':
                    loopStack.append(('if', loc))
                case 'end':
                    condType, condLoc = loopStack.pop()
                    if condType == 'while':
                        loopStack.append(('end', loc))
                        loc = condLoc - 1
                case 'do':
                    if not bool(stack.pop()):
                        loopStack.pop()
                        conditionalsCount = 1
                        while conditionalsCount != 0:
                            loc += 1
                            assert_error(loc < len(tokens), "`while` or `if` need statements an end particle")
                            if tokens[loc] in ('while', 'if'):
                                conditionalsCount += 1
                            elif tokens[loc] == 'end':
                                conditionalsCount -= 1
                case _:
                    if token[0] == '=':
                        assert_error(len(token) > 1, "variable needs name")
                        vars[token[1:]] = stack.pop()
                    else:
                        assert_error(token in vars, "unknown symbol: " + token)
                        stack.append(vars[token])
        loc += 1