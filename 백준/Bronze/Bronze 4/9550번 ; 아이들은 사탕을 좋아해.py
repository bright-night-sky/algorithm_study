# https://www.acmicpc.net/problem/9550

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 줄에 테스트 케이스의 수 T를 입력합니다.
# 1 <= T <= 100
# 정수형으로 변환합니다.
T = int(stdin.readline())

# 테스트 케이스의 수 T만큼 반복합니다.
for test_case_idx in range(T):
    # 승택이가 갖고 있는 사탕의 종류의 수 N,
    # 아이들이 행복해지는 최소 사탕의 개수 K를 공백으로 구분해 입력합니다.
    # 1 <= N, K <= 100
    # 각각 정수형으로 변환합니다.
    N, K = map(int, stdin.readline().split(' '))
    # 승택이가 가지고 있는 N개 종류의 각 사탕의 개수를 공백으로 구분해 입력합니다.
    # 모든 종류의 사탕의 개수는 최소 1개 최대 100개입니다.
    # 각각 정수형으로 변환하고 리스트 변수에 넣어줍니다.
    kind_of_candies = list(map(int, stdin.readline().split(' ')))
    # 생일 파티에 올 수 있는 아이들의 최댓값을 저장할 변수를 선언합니다.
    kids = 0

    # 모든 종류의 사탕에서 각 종류의 사탕씩 반복해봅니다.
    for candies in kind_of_candies:
        # 이번 사탕의 개수에 아이들이 행복해지는 최소 사탕의 개수 K를 나눈 몫을
        # 생일 파티에 올 수 있는 아이들의 최댓값 kids에 더해줍니다.
        kids += candies // K

    # 생일 파티에 올 수 있는 아이들의 최댓값인 kids의 값을 출력합니다.
    print(kids)