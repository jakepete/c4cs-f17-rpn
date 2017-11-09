#!/usr/bin/env python3

import operator


opers = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,

}


def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            stack.appent(int(token))
        except ValueError:
            arg2 = stack.pop()
            arg1 = stack.pop()
            calc = opers[token]
            stack.append(calc(arg1, arg2))

    return stack.pop()


def main()
    while True:
        calculate(input("rpn calc> "))


if __name__ == '__main__':
    main()
