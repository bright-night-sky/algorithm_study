# https://www.acmicpc.net/problem/13877

from sys import stdin


T = int(stdin.readline())

for test_case_idx in range(T):
    K, dec_num = map(int, stdin.readline().split(' '))
    oct_num = oct(dec_num)[2:]
    hex_num = hex(dec_num)[2:]

    print(f'{K} {oct_num} {dec_num} {hex_num}')