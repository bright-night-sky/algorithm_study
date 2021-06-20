# https://www.acmicpc.net/problem/10950

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 테스트 케이스의 개수 T를 입력합니다.
# 정수형으로 변환합니다.
T = int(stdin.readline())

# 테스트 케이스의 개수 T만큼 반복합니다.
for test_case_idx in range(T):
    # A, B를 공백으로 구분해 입력합니다.
    # 0 < A, 0 < B
    # 각각 정수형으로 변환합니다.
    A, B = map(int, stdin.readline().split(' '))

    # A + B를 출력합니다.
    print(A + B)