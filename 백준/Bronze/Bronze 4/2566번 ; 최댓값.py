# https://www.acmicpc.net/problem/2566

from sys import stdin


maxes = [None] * 9

for idx in range(9):
    line = list(map(int, stdin.readline().split(' ')))
    line_max = max(line)
    max_row = line.index(line_max)
    maxes[idx] = (line_max, max_row)

max_num = max(maxes, key=lambda number: number[0])
max_num_col = maxes.index(max_num)

print(max_num[0])
print(max_num_col + 1, max_num[1] + 1)