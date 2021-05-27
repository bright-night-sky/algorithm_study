# https://www.acmicpc.net/problem/2870

from sys import stdin

N = int(stdin.readline())

numbers = []

for line_idx in range(N):
    line = stdin.readline().rstrip()
    number = ''

    for character in line:
        if ord('0') <= ord(character) <= ord('9'):
            number += character
        else:
            if number != '':
                numbers.append(number)
                number = ''

numbers.sort()

for number in numbers:
    print(number)