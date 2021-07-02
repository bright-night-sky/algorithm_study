# https://www.acmicpc.net/problem/16462

from sys import stdin


N = int(stdin.readline())
Q = [None] * N

for i in range(N):
    Qi = stdin.readline().rstrip()

    Qi = Qi.replace('0', '9').replace('6', '9')
    Qi = int(Qi)

    if Qi > 100:
        score = 100

    Q[i] = Qi

avg = sum(Q) / N

print(avg)