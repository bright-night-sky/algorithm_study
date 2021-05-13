# https://www.acmicpc.net/problem/1213

from sys import stdin

hansoo_name = stdin.readline().rstrip()

result = ""

for alphabet in range(ord('A'), ord('Z') + 1):
    if hansoo_name.count(chr(alphabet)) % 2 != 0:
        result = "I'm Sorry Hansoo"

if result != "I'm Sorry Hansoo":
    hansoo_name = sorted(hansoo_name)
    print(hansoo_name)
    for idx in range(0, len(hansoo_name), 2):
        result += hansoo_name[idx]

    result = result + result[::-1]

    print(result)
else:
    print(result)