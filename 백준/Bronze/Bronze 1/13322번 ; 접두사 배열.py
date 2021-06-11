# https://www.acmicpc.net/problem/13322

from sys import stdin


S = stdin.readline().rstrip()
chars = list(S)
sorted_chars = sorted(chars)

for idx in range(len(chars)):
    cur_char_idx = sorted_chars.index(chars[idx])
    print(cur_char_idx)
    