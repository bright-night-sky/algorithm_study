# https://www.acmicpc.net/problem/2408

from sys import stdin
from math import floor


N = int(stdin.readline())

equation = ''

for _ in range(2 * N - 1):
    oper = stdin.readline().rstrip()
    equation += oper

print(equation)
equation_len = len(equation)

for idx in range(1, equation_len, 2):
    if equation[idx] == 