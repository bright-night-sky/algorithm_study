# https://www.acmicpc.net/problem/21918

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 번째 줄에 전구의 개수 N, 입력되는 명령어의 개수 M을 공백으로 구분해 입력합니다.
# 1 <= N, M <= 4,000
# 각각 정수형으로 변환합니다.
N, M = map(int, stdin.readline().split(' '))
# 두 번째 줄에는 N개의 전구가 현재 어떤 상태인지들을 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환하고 리스트 변수로 만들어줍니다.
bulbs = list(map(int, stdin.readline().split(' ')))

# 명령어의 개수 M개만큼 반복합니다.
for M_idx in range(M):
    # a번 명령어 a, a에 따른 b, c 명령어들을 공백으로 구분해 입력합니다.
    # 1 <= a <= 4
    # 각각 정수형으로 변환합니다.
    a, b, c = map(int, stdin.readline().split(' '))

    # a가 1인 경우
    if a == 1:
        # b-1번째 전구의 상태를 c로 변경합니다.
        bulbs[b - 1] = c
    # a가 2인 경우
    elif a == 2:
        # b-1번째부터 c-1번째 전구의 상태를 반복해봅니다.
        for bulb_idx in range(b - 1, c):
            # 현재 전구의 상태가 꺼져있는 상태인 0이라면
            if bulbs[bulb_idx] == 0:
                # 1로 변경합니다.
                bulbs[bulb_idx] = 1
            # 현재 전구의 상태가 켜져있는 상태인 1이라면
            elif bulbs[bulb_idx] == 1:
                # 0으로 변경합니다.
                bulbs[bulb_idx] = 0
    # a가 3인 경우
    elif a == 3:
        # b-1번째 전구부터 c-1번째 전구를 모두 끈 상태인 0으로 만들어줍니다.
        bulbs[b - 1:c] = [0] * (c - b + 1)
    # a가 4인 경우
    elif a == 4:
        # b-1번째 전구부터 c-1번째 전구를 모두 켠 상태인 1로 만들어줍니다.
        bulbs[b - 1:c] = [1] * (c - b + 1)

# 모든 명령어를 수행한 후 각 전구의 상태를 출력 형식에 맞게 출력합니다.
for bulb in bulbs:
    print(bulb, end=' ')