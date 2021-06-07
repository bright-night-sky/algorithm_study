# https://www.acmicpc.net/problem/13699

from sys import stdin


def t(number):
    result = 0

    if number == 0:
        return 1
    else:
        for i in range(number):
            result += t(i) * t(number - i)

    return result


n = int(stdin.readline())

print(t(n))