# https://www.acmicpc.net/problem/21756

from sys import stdin


N = int(stdin.readline())
nums = [num for num in range(1, N + 1)]
nums_len = len(nums)
result = []

while result == []:
    for idx in range(nums_len):
        if (idx + 1) % 2 == 0:
            result