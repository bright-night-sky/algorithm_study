# https://www.acmicpc.net/problem/1110

from sys import stdin

N = stdin.readline().rstrip()
first_num = N
cycle = 0

print(list('1'))

while True:
    position_sum = sum(map(int, list(N)))
    new_num = N[-1] + str(position_sum)[-1]
    cycle += 1

    if first_num == new_num:
        print(cycle)
        break
    else:
        N = new_num