# https://www.acmicpc.net/problem/4949

from sys import stdin

while True:
    string = stdin.readline().rstrip()

    if string == '.':
        break

    small_bracket_stack = []
    big_bracket_stack = []
    is_balance = "yes"

    for character in string:
        if character == '(':
            small_bracket_stack.append(character)
        elif character == ')':
            if small_bracket_stack != []:
                small_bracket_stack.pop()
            else:
                is_balance = "no"
                break
        elif character == '[':
            big_bracket_stack.append(character)
        elif character == ']':
            if big_bracket_stack != []:
                big_bracket_stack.pop()
            else:
                is_balance = "no"
                break

    if small_bracket_stack == [] and big_bracket_stack == []:
        print(is_balance)
    else:
        is_balance = "no"
        print(is_balance)