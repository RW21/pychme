import operator


class Environment:
    def __init__(self):
        self.keywords = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
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
    if type(t) == int or type(t) == float:
        return t
    else:
        procedure = environment.keywords[t[0]]
        args = [evaluate(k) for k in t[1:]]
        print(procedure)
        print(args)
        return procedure(*args)


a = '(+ 1 (+ 123 2))'
p = '(define (name a b) (+ a b )'

parsed = parse(a)
print(parsed)
print(evaluate(parsed))
