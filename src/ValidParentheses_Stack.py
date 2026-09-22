from typing import List


def isValid(s: str) -> bool:
    stack = []

    for par in s:
        if par in "({[":
            stack.append(par)
        if par == '}':
            if len(stack) <= 0 or stack.pop() != '{':
                return False
        elif par == ']':
            if len(stack) <= 0 or stack.pop() != '[':
                return False
        elif par == ')':
            if len(stack) <= 0 or stack.pop() != '(':
                return False

    if len(stack) == 0:
        return True
    return False


s = "()"

print(isValid(s))