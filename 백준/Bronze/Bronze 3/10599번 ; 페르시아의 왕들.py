# https://www.acmicpc.net/problem/10599

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 0 0 0 0을 입력할 때까지 반복합니다.
while True:
    # 4개의 정수 a, b, c, d를 공백으로 구분해 입력합니다.
    # -5000 <= a <= b <= c <= d <= 2000
    # [a, b]는 출생일의 범위, [c, d]는 사망일의 범위입니다.
    # 각각 정수형으로 변환합니다.
    a, b, c, d = map(int, stdin.readline().split(' '))

    # a, b, c, d가 모두 0이라면
    if (a, b, c, d) == (0, 0, 0, 0):
        # 반복문을 탈출합니다.
        break

    # 최소나이를 저장하는 변수를 선언합니다.
    min_age = c - b
    # 최대나이를 저장하는 변수를 선언합니다.
    max_age = d - a

    # 최소나이와 최대나이를 공백으로 나눠 출력합니다.
    print(min_age, max_age)