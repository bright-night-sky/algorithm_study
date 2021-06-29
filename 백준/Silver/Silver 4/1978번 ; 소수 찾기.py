# https://www.acmicpc.net/problem/1978

from sys import stdin


N = int(stdin.readline())
numbers = list(map(int, stdin.readline().split(' ')))
prime_num_cnt = 0
max_num = max(numbers)
primes = [False] * max_num
