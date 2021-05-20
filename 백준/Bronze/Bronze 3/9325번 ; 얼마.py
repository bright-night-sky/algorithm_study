# https://www.acmicpc.net/problem/9325

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 테스트 케이스의 개수를 입력합니다.
# 정수형으로 변환합니다.
test_case_cnt = int(stdin.readline())

# 테스트 케이스의 개수만큼 반복합니다.
for test_case_idx in range(test_case_cnt):
    # 자동차의 가격 s를 입력합니다.
    # 정수형으로 변환합니다.
    # 1 <= s <= 100,000
    s = int(stdin.readline())
    # 서로 다른 옵션의 개수 n을 입력합니다.
    # 정수형으로 변환합니다.
    # 0 <= n <- 1,000
    n = int(stdin.readline())

    # 최종적으로 구매하려는 자동차의 가격을 저장할 변수를 선언합니다.
    # 자동차의 가격 s로 초기화합니다.
    total_price = s

    # 서로 다른 옵션의 개수 n만큼 반복합니다.
    for option_idx in range(n):
        # 해빈이가 사려고 하는 특정 옵션의 개수 q, 해당 옵션의 가격 p를 공백으로 구분해 입력합니다.
        # 각각 정수형으로 변환합니다.
        # 1 <= q <= 100
        # 1 <= p <= 10,000
        q, p = map(int, stdin.readline().split(' '))

        # 이번 옵션의 가격을 저장하는 변수를 선언합니다.
        option_price = q * p
        # 이번 옵션의 가격을 자동차 최종 가격에 더해줍니다.
        total_price += option_price

    # 최종적인 자동차의 가격을 출력합니다.
    print(total_price)