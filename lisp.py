import operator
import os

os.system("")

# Group of Different functions for different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

class Environment:
    def __init__(self):
        self.keywords = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            'atom?': (lambda a : type(a) != list),
            # '/': operator.di
        }


special_symbols = {'+', '/', '-', '*'}


def parse(p) -> list:
    p = p.replace('(', ' ( ').replace(')', ' ) ').split()
    p.reverse()
    return tokenize(p)


def tokenize(p):
    token = p.pop()

    if token == '(':
        p_ = []
        while p[-1] != ')':
            p_.append(tokenize(p))
        p.pop()
        return p_
    else:
        if token[0].isalpha():
            return token
        elif token in special_symbols:
            return token
        else:
            return eval(token)


environment = Environment()


def evaluate(t):
    print(t)
    if type(t) == int or type(t) == float or (type(t) == str and t not in environment.keywords):
        return t
    elif type(t) == str and t in environment.keywords:
        # variable reference
        return environment.keywords[t]
    elif t[0] == 'define':
        environment.keywords[t[1]] = evaluate(t[2])
    elif t[0] == 'lambda':
        pass
    else:
        procedure = environment.keywords[t[0]]
        args = [evaluate(k) for k in t[1:]]
        print(procedure)
        print(args)
        return procedure(*args)


a = '(+ 1 (+ 123 2))'
p = '(define name (+ 1 1 ))'

parsed = parse(p)
print(parsed)
print(evaluate(parsed))

def repl():
    while True:
        parsed = parse(input(style.MAGENTA + 'scheme> '))
        print(evaluate(parsed))

repl()
