import sys

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]


def apply_operator(op, a, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a // b


def evaluate(expr):

    stack = Stack()

    tokens = expr.replace('(', ' ( ').replace(')', ' ) ').split()

    for token in tokens:

        if token != ')':
            stack.push(token)

        else:
            b = int(stack.pop())
            a = int(stack.pop())
            op = stack.pop()

            stack.pop()

            result = apply_operator(op, a, b)

            stack.push(str(result))

    return stack.pop()


if __name__ == "__main__":

    expression = sys.argv[1]

    result = evaluate(expression)

    print(result)
