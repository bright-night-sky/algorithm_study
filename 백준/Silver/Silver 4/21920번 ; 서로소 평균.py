# https://www.acmicpc.net/problem/21920

from sys import stdin
from math import gcd

N = int(stdin.readline())
A = list(map(int, stdin.readline().split(' ')))
X = int(stdin.readline())

coprimes = list(filter(lambda number: gcd(number, X) == 1, A))
avg = sum(coprimes) / len(coprimes)

if str(avg)[-2:] == '.0':
    print(int(avg))
else:
    print(avg)