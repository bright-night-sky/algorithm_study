# https://www.acmicpc.net/problem/15701

# 첫째 줄에 자연수 N을 입력합니다.
# 1 <= N <= 1,000,000,000
N = int(input())

half_N = N // 2

divisor_count = 0

for number in range(1, half_N + 1):
    if N % number == 0:
        divisor_count += 1

print(divisor_count + 1)