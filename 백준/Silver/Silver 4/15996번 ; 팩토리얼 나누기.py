# https://www.acmicpc.net/problem/15996

from sys import stdin

N, A = map(int, stdin.readline().split(' '))
k = 0
N_numbers = []

if N == 0:
    N_numbers = [1]
else:
    N_numbers = [number for number in range(N, 1, -1)]

while True:
    Ak = A ** k

    for number in N_numbers:
        remainder = number % Ak

        if remainder