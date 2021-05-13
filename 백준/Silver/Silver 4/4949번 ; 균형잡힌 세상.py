# https://www.acmicpc.net/problem/4949

from sys import stdin

small_bracket_stack = []
big_bracket_stack = []

for line in stdin:
    yes_or_no = "yes"
    line = line.rstrip('\n')
    print(line)

    if not line:
        break

    for char in line:
        if char == '(':
            small_bracket_stack.append(char)
        elif char == ')':
            if not small_bracket_stack:
                yes_or_no = "no"
                break
            small_bracket_stack.pop(-1)
        elif char == '[':
            big_bracket_stack.append(char)
        elif char == ']':
            if not big_bracket_stack:
                yes_or_no = "no"
                break
            big_bracket_stack.pop(-1)

    if not small_bracket_stack and not big_bracket_stack:
        print(yes_or_no)
    else:
        yes_or_no = "no"
        print(yes_or_no)