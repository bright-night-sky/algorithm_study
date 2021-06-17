# https://www.acmicpc.net/problem/9493

from sys import stdin


while True:
    M, A, B = map(int, stdin.readline().split(' '))

    if (M, A, B) == (0, 0, 0):
        break

    train_time = M // A
    plane_time = M // B
    time_gap = train_time - plane_time

    print(time_gap)