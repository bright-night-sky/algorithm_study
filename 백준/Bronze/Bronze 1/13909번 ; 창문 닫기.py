# https://www.acmicpc.net/problem/13909

from sys import stdin

N = int(stdin.readline())
windows = [0] * N

for person in range(1, N + 1):
    for window_idx in range(N):
        if (window_idx + 1) % person == 0:
            if windows[window_idx] == 0:
                windows[window_idx] = 1
            else:
                windows[window_idx] = 0

print(windows.count(1))