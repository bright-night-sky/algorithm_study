# https://www.acmicpc.net/problem/2581

# 첫째 줄에 M을 입력합니다.
M = int(input())

N = int(input())

prime_number = [num for num in range(M, N + 1)]

for number in range(2, N + 1):
