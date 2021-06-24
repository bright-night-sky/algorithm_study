# https://www.acmicpc.net/problem/1009

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 줄에는 테스트 케이스의 개수 T를 입력합니다.
# 정수형으로 변환합니다.
T = int(stdin.readline())

# 테스트 케이스의 개수 T만큼 반복합니다.
for test_case_idx in range(T):
    # 정수 a, b를 공백으로 구분해 입력합니다.
    # 1 <= a < 100
    # 1 <= b < 1,000,000
    # 각각 정수형으로 변환합니다.
    a, b = map(int, stdin.readline().split(' '))
    # a^b의 마지막 숫자를 저장하는 변수를 선언합니다.
    last_number = pow(a, b, 10)

    # 마지막 숫자가 0이라면
    if last_number == 0:
        # 10번 컴퓨터가 처리하므로 10을 출력합니다.
        print(10)
    # 마지막 숫자가 0외의 숫자라면
    else:
        # 그 번호에 해당하는 컴퓨터가 처리하므로 마지막 숫자를 그대로 출력합니다.
        print(last_number)