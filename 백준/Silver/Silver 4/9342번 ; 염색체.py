# https://www.acmicpc.net/problem/9342

from sys import stdin

T = int(stdin.readline())

for test_case_idx in range(T):
    string = stdin.readline().rstrip()
    result = "Infected!"

    if string[0] not in ['A', 'B', 'C', 'D', 'E', 'F']:
        result = "Good"
    elif 