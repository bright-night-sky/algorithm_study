# https://www.acmicpc.net/problem/9417

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 두 수의 최대공약수를 반환하는 함수를 구현합니다.
def gcd(num1, num2):
    # 유클리드 호제법을 사용해서 최대공약수를 구합니다.
    while num2 > 0:
        num1, num2 = num2, num1 % num2

    return num1


# 첫째 줄에 테스트 케이스의 개수 N을 입력합니다.
# 1 < N < 100
N = int(stdin.readline())

# 테스트 케이스의 개수 N만큼 반복합니다.
for test_case_idx in range(N):
    # 양의 정수 M개를 공백으로 구분해 입력합니다.
    # 각각 정수형으로 변환하고 리스트 변수에 넣어줍니다.
    # 모든 수는 -2^31보다 크거나 같고, 2^31 - 1보다 작거나 같습니다.
    numbers = list(map(int, stdin.readline().split(' ')))
    # 입력한 수의 개수를 저장하는 변수를 저장하는 변수를 선언합니다.
    numbers_len = len(numbers)
    # 모든 두 수의 쌍의 최대공약수 중 가장 큰 값을 저장할 변수를 선언합니다.
    max_gcd = 1

    # 양의 정수 리스트에서 두 개씩 묶어 최대공약수를 구해봅니다.
    for idx1 in range(numbers_len - 1):
        for idx2 in range(idx1 + 1, numbers_len):
            this_time_gcd = gcd(numbers[idx1], numbers[idx2])

            # 이번 두 수의 최대공약수가 이전까지의 최대공약수 중 가장 크다면
            if this_time_gcd > max_gcd:
                # max_gcd의 값을 이번 최대공약수로 변경합니다.
                max_gcd = this_time_gcd

    # max_gcd의 값을 출력합니다.
    print(max_gcd)
