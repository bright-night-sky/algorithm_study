# https://www.acmicpc.net/problem/2520

from sys import stdin


test_case = int(stdin.readline())
blank_line = stdin.readline()

for test_case_idx in range(test_case):
    cm, y, ssu, ssa, f = map(int, stdin.readline().split(' '))
    b, gs, gc, w = map(int, stdin.readline().split(' '))
    dough = min([cm // 8, y // 8, ssu // 4, ssa, f // 9]) * 16
    pancakes = 0

    pancakes += min(dough, b)
    dough -= min(dough, b)

    pancakes += min(dough, gs // 30)
    dough -= min(dough, gs // 30)

    pancakes += min(dough, gc // 25)
    dough -= min(dough, gc // 25)

    pancakes += min(dough, w // 10)
    dough -= min(dough, w // 10)

    print(pancakes)
    blank_line = stdin.readline()