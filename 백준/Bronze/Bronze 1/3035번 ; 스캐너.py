# https://www.acmicpc.net/problem/3035

from sys import stdin

R, C, ZR, ZC = map(int, stdin.readline().split(' '))

newspaper = []
scanned_newspaper = []

for row in range(R):
    newspaper += stdin.readline().rstrip()

for row in newspaper:
    new_row = ''

    for char in row:
        new_row += char * ZC

    print(new_row * ZR)