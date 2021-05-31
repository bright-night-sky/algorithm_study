# https://www.acmicpc.net/problem/1748

from sys import stdin

N = stdin.readline().rstrip()
N_len = len(N)
result_cipher = 0

for zero_cnt in range(N_len):
    result_cipher += int('9' + '0' * zero_cnt)

result_cipher += (int(N) - int('1' + '0' * (N_len - 1)) + 1) * N_len

print(result_cipher)