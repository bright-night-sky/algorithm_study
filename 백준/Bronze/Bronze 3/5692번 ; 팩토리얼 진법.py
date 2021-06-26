# https://www.acmicpc.net/problem/5692

# readline을 사용하기 위해 import합니다.
from sys import stdin
# factorial을 사용하기 위해 import합니다.
from math import factorial


# 0을 입력할 때까지 반복합니다.
while True:
    # 팩토리얼 진법 숫자를 입력합니다.
    # 길이는 최대 5자리입니다.
    # 맨 끝의 \n은 떼어줍니다.
    number = stdin.readline().rstrip()
    # 입력한 팩토리얼 진법 숫자의 길이를 저장하는 변수를 선언합니다.
    number_len = len(number)
    # 팩토리얼 진법 숫자를 10진법으로 읽은 값을 저장할 변수를 선언합니다.
    decimal_number = 0

    # 입력한 팩토리얼 진법 숫자가 0이라면
    if number == '0':
        # 반복문을 탈출합니다.
        break

    # 팩토리얼 진법 숫자의 길이만큼 반복합니다.
    for i in range(number_len):
        # 팩토리얼 진법 숫자에서 i번 자리의 값을 10진법으로 계산해 decimal_number에 더해줍니다.
        decimal_number += int(number[i]) * factorial(number_len - i)

    # 팩토리얼 진법 숫자를 10진법 숫자로 읽은 값을 출력합니다.
    print(decimal_number)