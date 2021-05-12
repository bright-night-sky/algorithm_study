# https://www.acmicpc.net/problem/1110

from sys import stdin

N = int(stdin.readline().rstrip())
temp_N = str(N)
cycle = 0

while True:
    one_ten_sum = int(temp_N[-1]) + int(temp_N[0])
    new_num = temp_N[-1] + str(one_ten_sum)[-1]

    cycle += 1

    if int(new_num) == N:
        print(cycle)
        break

    temp_N = new_num
