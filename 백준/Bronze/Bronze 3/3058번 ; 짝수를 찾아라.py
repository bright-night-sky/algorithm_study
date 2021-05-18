# https://www.acmicpc.net/problem/3058

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 테스트 데이터의 개수 T를 입력합니다.
# 정수형으로 변환해줍니다.
T = int(stdin.readline())

# 테스트 데이터의 개수 T만큼 반복해봅니다.
for _ in range(T):
    # 7개의 자연수를 공백으로 구분해 입력합니다.
    # 각 자연수를 정수형으로 변환하고 리스트 변수에 넣어줍니다.
    # 각 자연수는 1보다 크거나 같고, 100보다 작거나 같습니다.
    # 적어도 하나는 짝수입니다.
    numbers = list(map(int, stdin.readline().split(' ')))

    # 7개의 자연수들 중에서 짝수인 자연수들을 필터링해 저장하는 리스트 변수를 선언합니다.
    even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
    # even_numbers에 있는 짝수 자연수들의 합을 저장하는 변수를 선언합니다.
    even_number_sum = sum(even_numbers)
    # even_numbers에서 가장 작은 짝수 자연수를 저장하는 변수를 선언합니다.
    min_even_number = min(even_numbers)

    # 짝수의 합과 최소 짝수값을 공백으로 구분해 출력합니다.
    print(even_number_sum, min_even_number)