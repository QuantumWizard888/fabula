import math
from math import pi
from math import e
import re

def postfix_calc(seq: list):

    stack = []
    for i in range(len(seq)):
            if (re.search(r'\d+|-\d+', seq[i]) is not None) and (re.search(r'[\d]+\.', seq[i]) is None):
                stack.append(int(seq[i]))
            elif re.search(r'[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+', seq[i]) is not None:
                stack.append(float(seq[i]))
            elif re.search(r'\bpi\b', seq[i]) is not None:
                stack.append(pi)
            elif re.search(r'\be\b', seq[i]) is not None:
                stack.append(e)
            elif seq[i] == '+':
                y = stack.pop()
                x = stack.pop()
                z = x + y
                stack.append(z)
            elif seq[i] == '-':
                y = stack.pop()
                x = stack.pop()
                z = x - y
                stack.append(z)
            elif seq[i] == '*':
                y = stack.pop()
                x = stack.pop()
                z = x * y
                stack.append(z)
            elif seq[i] == '/':
                y = stack.pop()
                x = stack.pop()
                z = (float(x) / float(y))
                stack.append(z)
            elif seq[i] == '**':
                y = stack.pop()
                x = stack.pop()
                z = x ** y
                stack.append(z)
                
    result = stack.pop()

    return result

def to_int(seq):
    try:
        number = int(seq)
        return number
    except ValueError:
        pass

def to_float(seq):
    try:
        number = float(seq)
        return number
    except ValueError:
        pass

def tokenizer(seq):
    return list(filter(lambda s: s.isdigit() or (re.search(r'\bpi\b', s)) or (re.search(r'\be\b', s)) or s == '**' or s == '-' or s == '+' or s == '*' or s == '/' or to_float(s) or to_int(s), seq.split(' ')))

def shell():
    print('####################################')
    print('#             FABULA               #')
    print('#    A little postfix calculator   #')
    print('#                                  #')
    print('# Type whereami() if you need help #')
    print('####################################')

    while True:

        sequence = input('>>> ')
        if sequence == 'whereami':
            print('############### HELP ##############')
            print('# Operators: + , - , * , / , **')
            print('# Mathematical constants: pi , e')
            print('############# EXAMPLES ############')
            print('# 2 9 * pi +')
            print('# <<< [\'2\', \'9\', \'*\', \'pi\', \'+\']')
            print('# <<< 21.141592653589793')
            print('###################################')
        elif sequence == 'exit':
            exit()
        else:
            print('<<<', tokenizer(sequence))
            try:
                print('<<<', postfix_calc(tokenizer(sequence)))
            except:
                print('<<< [Unknown sequence]')

shell()
