# https://www.acmicpc.net/problem/7481

from sys import stdin


test_case_cnt = int(stdin.readline())

for test_case_idx in range(test_case_cnt):
    a, b, S = map(int, stdin.readline().split(' '))
    a_cnt = 0
    b_cnt = 0

    if a > b:
        a_cnt = S // a
        S -= a * a_cnt

        b_cnt = S // b
        S -= b * b_cnt
    else:
        b_cnt = S // b
        S -= b * b_cnt

        a_cnt = S // a
        S -= a * a_cnt

    if S == 0:
        print(a_cnt, b_cnt)
    else:
        print("Impossible")
