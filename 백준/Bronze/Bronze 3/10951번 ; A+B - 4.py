# https://www.acmicpc.net/problem/10951

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 일단 계속 반복해봅니다.
while True:
    # try 구문에 있는 코드를 실행해봅니다.
    try:
        # 두 정수 A, B를 공백으로 구분해 입력합니다.
        # 0 < A, B < 10
        # 각각 정수형으로 변환합니다.
        A, B = map(int, stdin.readline().split(' '))

        # A + B를 출력합니다.
        print(A + B)
    # ValueError가 발생하면
    except ValueError:
        # 입력이 끝났으므로 반복문을 탈출합니다.
        break