# https://www.acmicpc.net/problem/1362

from sys import stdin


o, w = map(int, stdin.readline().split(' '))
scenario = 1

while True:
    while True:
        action, n = stdin.readline().rstrip().split(' ')

        if (action, n) == ("#", 0) or (action, n) == ("0", 0)
            break

        if action == "E":
            w -= n
        elif action == "F":
            w += n

    if (action, n) == ("0", 0):
        break