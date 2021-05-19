# https://www.acmicpc.net/problem/9295

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 테스트 케이스의 개수 T를 입력합니다.
# 정수형으로 변환합니다.
T = int(stdin.readline())

# 테스트 케이스의 개수 T만큼 반복합니다.
for test_case_idx in range(T):
    # 주사위를 두 번 던져 나온 두 수를 공백으로 구분해 입력합니다.
    # 각각 정수형으로 변환합니다.
    dice1, dice2 = map(int, stdin.readline().split(' '))
    # 주사위를 던져 나온 두 수의 합을 저장하는 변수를 선언합니다.
    dice_sum = dice1 + dice2

    # 출력형식에 맞게 출력합니다.
    print(f"Case {test_case_idx + 1}: {dice_sum}")