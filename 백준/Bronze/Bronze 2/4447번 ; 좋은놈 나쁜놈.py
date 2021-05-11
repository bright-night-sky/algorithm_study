# https://www.acmicpc.net/problem/4447

# 첫 줄에는 테스트 케이스 n을 입력합니다.
# n > 0
n = int(input())

# 테스트 케이스의 수만큼 반복해봅니다.
for i in range(n):
    # 히어로의 이름을 입력합니다.
    hero_name = input()

    # 히어로의 이름에서 g와 G의 개수를 저장하는 변수를 선언합니다.
    gG_count = hero_name.count('g') + hero_name.count('G')
    # 히어로의 이름에서 b와 B의 개수를 저장하는 변수를 선언합니다.
    bB_count = hero_name.count('b') + hero_name.count('B')

    # g와 G의 개수가 b와 B의 개수보다 많다면
    if gG_count > bB_count:
        # 히어로 이름 is GOOD으로 출력합니다.
        print(f"{hero_name} is GOOD")
    # g와 G의 개수가 b와 B의 개수보다 적다면
    elif gG_count < bB_count:
        # 히어로 이름 is A BADDY로 출력합니다.
        print(f"{hero_name} is A BADDY")
    # g와 G의 개수가 b와 B의 개수와 같다면
    else:
        # 히어로 이름 is NEUTRAL로 출력합니다.
        print(f"{hero_name} is NEUTRAL")