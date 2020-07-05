import re
from collections import deque


def parse(p) -> list:
    p = p.replace('(', ' ( ').replace(')', ' ) ').split()
    p.reverse()
    print(p)
    token = p.pop()
    if token == '(':
        tokens = []
        while p[-1] != ')':
            token = p.pop()
            tokens.append(parse(token))
        p.pop()
        return tokens
    elif token == ')':
        raise SyntaxError
    else:
        if token[0].isalpha():
            return token
        else:
            return eval(token)

# def evaluate(t):

class Environment:
   def __init__(self):
       self.keywords = {}


print(parse('(f (f 1 1) 10)'))
