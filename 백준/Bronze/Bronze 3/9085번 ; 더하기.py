# https://www.acmicpc.net/problem/9085

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫 줄에는 테스트 케이스의 개수 T를 입력합니다.
# 정수형으로 변환합니다.
# 1 <= T <= 10
T = int(stdin.readline())

# 테스트 케이스의 개수 T만큼 반복해봅니다.
for _ in range(T):
    # 자연수의 개수 N을 입력합니다.
    # 정수형으로 변환합니다.
    # 1 <=N <= 100
    N = int(stdin.readline())
    # N개의 자연수를 공백으로 구분해 입력합니다.
    # 각각 정수형으로 변환합니다.
    numbers = list(map(int, stdin.readline().split(' ')))

    # numbers에 있는 수들의 합을 출력합니다.
    print(sum(numbers))