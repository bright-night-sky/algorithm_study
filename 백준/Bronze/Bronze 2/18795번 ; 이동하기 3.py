# https://www.acmicpc.net/problem/18795

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 미로의 크기 N, M을 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
N, M = map(int, stdin.readline().split(' '))
# N개의 정수 Ai들을 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
A = map(int, stdin.readline().split(' '))
# N개의 정수 Bi들을 공백으로 구분해 입력합니다.
# # 각각 정수형으로 변환합니다.
B = map(int, stdin.readline().split(' '))

# 미로의 (0, 0)에서 (N, M)까지 오는데 최소 거리는 단순히 테두리를 따라서 오면 되므로
# 모든 Ai, Bi 개의 쓰레기를 한 번씩 주우면 됩니다.
# Ai들의 합을 저장하는 변수를 선언합니다.
sum_Ai = sum(A)
# Bi들의 합을 저장하는 변수를 선언합니다.
sum_Bi = sum(B)

# sum_Ai와 sum_Bi를 더한 값을 출력합니다.
print(sum_Ai + sum_Bi)