# https://www.acmicpc.net/problem/1247

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 3개의 테스트 케이스를 반복해봅니다.
for test_case_idx in range(3):
    # 각 테스트 셋의 첫째 줄에는 N을 입력합니다.
    # 1 <= N <= 100,000
    # 정수형으로 변환해줍니다.
    N = int(stdin.readline())

    # N개의 정수를 저장할 리스트 변수를 선언합니다.
    numbers = []

    # N번 반복해봅니다.
    for number_idx in range(N):
        # 정수를 하나 입력합니다.
        # 정수의 절댓값은 9223372036854775807보다 작거나 같습니다.
        # 정수형으로 변환해줍니다.
        number = int(stdin.readline())
        # 입력한 정수를 numbers 리스트 변수에 넣어줍니다.
        numbers.append(number)

    # numbers 리스트 변수에 있는 정수들을 모두 합한 값을 저장하는 변수를 선언합니다.
    numbers_sum = sum(numbers)

    # numbers_sum이 0이라면
    if numbers_sum == 0:
        # 0을 출력합니다.
        print("0")
    # numbers_sum이 0보다 크다면
    elif numbers_sum > 0:
        # +를 출력합니다.
        print("+")
    # numbers_sum이 0보다 작다면
    elif numbers_sum < 0:
        # -를 출력합니다.
        print("-")