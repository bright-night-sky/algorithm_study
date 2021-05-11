# https://www.acmicpc.net/problem/17206

# 첫째 줄에는 문제의 수 T를 입력합니다.
# 1 <= T <= 100,000
T = int(input())

Ns = list(map(int, input().split(' ')))

for N in Ns:
    multiple_3_7_sum = 0

