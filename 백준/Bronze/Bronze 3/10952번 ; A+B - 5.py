# https://www.acmicpc.net/problem/10952

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 0 0을 입력할 때까지 반복합니다.
while True:
    # 두 정수 A, B를 공백으로 구분해 입력합니다.
    # 0 < A, B < 10
    # 각각 정수형으로 변환합니다.
    A, B = map(int, stdin.readline().split(' '))

    # A, B 모두 0이라면
    if (A, B) == (0, 0):
        # 반복문을 탈출합니다.
        break

    # A + B를 출력합니다.
    print(A + B)