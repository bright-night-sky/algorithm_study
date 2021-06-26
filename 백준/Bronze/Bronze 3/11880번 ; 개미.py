# https://www.acmicpc.net/problem/11880

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 줄에 테스트 케이스의 개수 T를 입력합니다.
# 1 <= T <= 100,000
# 정수형으로 변환합니다.
T = int(stdin.readline())

# 테스트 케이스의 개수 T만큼 반복합니다.
for test_case_idx in range(T):
    # 지우개의 가로 길이 a, 세로 길이 b, 높이 c를 공백으로 구분해 입력합니다.
    # 1 <= a, b, c <= 10^5
    # 각각 정수형으로 변환하고 리스트 변수에 넣어줍니다.
    lengths = list(map(int, stdin.readline().split(' ')))
    # 지우개의 각 길이 중 가장 긴 것을 저장하는 변수를 선언합니다.
    max_length = max(lengths)
    # 개미 로봇이 이동한 최단 거리를 계산하고 저장한 변수를 선언합니다.
    # 최단 거리의 제곱을 저장합니다.
    # 최단 거리의 제곱은 가로, 세로, 높이 중 가장 긴 길이 외 두 길이의 합의 제곱과
    # 가장 긴 길이의 제곱의 합입니다.
    shortest = (sum(lengths) - max_length) ** 2 + max_length ** 2

    # 최단 거리의 제곱을 출력합니다.
    print(shortest)