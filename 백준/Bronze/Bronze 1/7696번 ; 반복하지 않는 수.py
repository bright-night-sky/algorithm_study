# https://www.acmicpc.net/problem/7696

from sys import stdin


repeat_nums = ('11', '22', '33', '44', '55', '66', '77', '88', '99', '00')
n = int(stdin.readline())

num = 1
n_cnt = 0
while True:
    if n_cnt == n:
       print(num)
       break

    for repeat_num in repeat_nums:
        if repeat_num in str(num):
            break

    num += 1
    n_cnt += 1