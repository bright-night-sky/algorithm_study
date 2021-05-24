# https://www.acmicpc.net/problem/1037

from sys import stdin

real_divisor_cnt = int(stdin.readline())
real_divisors = sorted(list(map(int, stdin.readline().split(' '))))
max_divisor = max(real_divisors)

number = max_divisor + 1

while True:
    

    number += 1