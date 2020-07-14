import operator
import sys


class Environment:
    def __init__(self, params=[], args=[], env=None):
        self.keywords = {}
        self.keywords.update(zip(params, args))


primitives = {
    '+': operator.add,
    '-': operator.sub,
    'atom?': lambda a: type(a) != list,
    'car': lambda a: a[0],
    'cdr': lambda a: a[1:],
    'cons': lambda a, b: [a] + b
}


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
        elif token in primitives:
            return token
        else:
            return eval(token)


class Procedure:
    def __init__(self, params, body, env):
        self.params, self.body, self.env = params, body, env

    def __call__(self, *args, **kwargs):
        return evaluate(self.body, Environment(self.params, args))


def evaluate(t, environment):
    if type(t) == int or type(t) == float or (type(t) == str and t not in environment.keywords):
        return t
    elif type(t) == str and t in environment.keywords:
        # variable reference
        return environment.keywords[t]
    elif t[0] == 'define':
        environment.keywords[t[1]] = evaluate(t[2], environment)
    elif t[0] == 'lambda':
        params, body = t[1], t[2]
        return Procedure(params, body, environment)
    else:
        procedure = evaluate(t[0], environment)
        args = [evaluate(k, environment) for k in t[1:]]
        return procedure(*args)


standard_env = Environment(params=primitives.keys(), args=primitives.values())


def repl():
    while True:
        parsed = parse(input('scheme> '))
        print(evaluate(parsed, standard_env))



if len(sys.argv) == 1:
    repl()
elif len(sys.argv) == 2:
    f = open(sys.argv[1])
    for line in f:
        print(evaluate(parse(line)))
