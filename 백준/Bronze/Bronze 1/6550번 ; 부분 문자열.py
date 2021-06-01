# https://www.acmicpc.net/problem/6550

from sys import stdin

while True:
    strings = stdin.readline().rstrip()

    s, t = strings.split(' ')
    s_char_idx = [0] * len(s)

    for character in s:
        try:
            s_char_idx[]