# https://www.acmicpc.net/problem/21965

from sys import stdin


N = int(stdin.readline())
sequence = list(map(int, stdin.readline().split(' ')))
peak = max(sequence)
peak_idx = sequence.index(peak)
is_mountain = "YES"

for idx in range(1, peak_idx + 1):
    if sequence[idx - 1] >= sequence[idx]:
        is_mountain = "NO"
        break

if is_mountain == "YES":
    for idx in range(peak, N - 1):
        if sequence[idx] >= sequence[idx + 1]:
            is_mountain = "NO"
            break

print(is_mountain)