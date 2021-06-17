# https://www.acmicpc.net/problem/9501

from sys import stdin


T = int(stdin.readline())

for test_case_idx in range(T):
    N, D = map(int, stdin.readline().split(' '))
    can_arrive_cnt = 0

    for rocket_idx in range(N):
        vi, fi, ci = map(int, stdin.readline().split(' '))

        fuel_for_unit_time = fi / ci

        if vi * fuel_for_unit_time >= D:
            can_arrive_cnt += 1

    print(can_arrive_cnt)