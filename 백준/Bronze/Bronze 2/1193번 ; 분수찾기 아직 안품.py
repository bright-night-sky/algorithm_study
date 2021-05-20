# https://www.acmicpc.net/problem/1193

from sys import stdin

X = int(stdin.readline())

cnt = 1
fraction_section = 0
while True:
    if X < fraction_section + cnt:
        break
    else:
        fraction_section += cnt
        cnt += 1

print(fraction_section, cnt)

remain = X - fraction_section
if cnt % 2 == 0:
    top = 1
    bottom = cnt - top
else:
    bottom = 0
    top = cnt - bottom

    for idx in range(remain):
        bottom += 1
        top = cnt - bottom

    print(f"{top}/{bottom}")