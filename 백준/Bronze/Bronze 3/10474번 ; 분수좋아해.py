# https://www.acmicpc.net/problem/10474

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 0 0을 입력할 때까지 반복합니다.
while True:
    # 분자, 분모를 공백으로 구분해 입력합니다.
    # 1 <= 분자, 분모 <= 2^31 - 1
    # 각각 정수형으로 변환합니다.
    numerator, denominator = map(int, stdin.readline().split(' '))

    # 입력한 분자, 분모가 모두 0이라면
    if (numerator, denominator) == (0, 0):
        # 반복문을 탈출하고 종료합니다.
        break

    # 대분수의 정수부를 저장하는 변수를 선언합니다.
    integer_part = numerator // denominator
    # 분자는 대분수의 정수부를 떼낸만큼 진분수 형태로 값을 변경합니다.
    numerator %= denominator

    # 출력 형식에 맞게 출력합니다.
    print(f'{integer_part} {numerator} / {denominator}')