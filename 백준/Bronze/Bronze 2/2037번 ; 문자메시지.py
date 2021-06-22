# https://www.acmicpc.net/problem/2037

from sys import stdin


p, w = map(int, stdin.readline().split(' '))
string = stdin.readline().rstrip()
str_len = len(string)

for idx in range(str_len):
    prev_char = None

    if idx > 0:
        prev_char = string[idx - 1]

