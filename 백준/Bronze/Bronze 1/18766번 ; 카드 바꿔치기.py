# https://www.acmicpc.net/problem/18766

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫 줄에는 테스트 케이스의 수 T를 입력합니다.
# 1 <= T <= 10
T = int(stdin.readline().rstrip())

# 테스트 케이스의 수 T만큼 반복합니다.
for test_case_idx in range(T):
    # 각 테스트 케이스의 첫째 줄에는 카드의 개수 n을 입력합니다.
    # 1 <= n <= 200
    n = int(stdin.readline().rstrip())
    # 둘째 줄에는 카드놀이를 하기 전 범고래가 기억하는 n장의 카드를 공백으로 구분해 입력합니다.
    # 리스트 변수로 만들어주고 정렬을 합니다.
    grampus_cards = sorted(list(stdin.readline().rstrip().split(' ')))
    # 둘째 줄에는 돌고래가 기억하는 n장의 카드를 공백으로 구분해 입력합니다.
    # 리스트 변수로 만들어주고 정렬을 합니다.
    dolphin_cards = sorted(list(stdin.readline().rstrip().split(' ')))

    # 범고래의 카드와 돌고래의 카드가 같다면
    if grampus_cards == dolphin_cards:
        # NOT CHEATER를 출력합니다.
        print("NOT CHEATER")
    # 범고래의 카드와 돌고래의 카드가 같지 않다면
    else:
        # CHEATER를 출력합니다.
        print("CHEATER")