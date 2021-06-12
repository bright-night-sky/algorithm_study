# https://www.acmicpc.net/problem/1384

from sys import stdin


group_num = 1

while True:
    n = int(stdin.readline())

    if n == 0:
        break

    kids_infos = [None] * n
    kid_names = [None] * n

    for kid_idx in range(n):
        kid_info = stdin.readline().rstrip().split(' ')
        kids_infos[kid_idx] = kid_info
        kid_names[kid_idx] = kid_info[0]

    for kid_info in kids_infos:
