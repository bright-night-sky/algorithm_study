# https://www.acmicpc.net/problem/18247

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 번째 줄에 테스트 케이스의 개수 T를 입력합니다.
# 1 <= T <= 20
# 정수형으로 변환합니다.
T = int(stdin.readline())

# 테스트 케이스의 개수 T만큼 반복합니다.
for test_case_idx in range(T):
    # 영화관 자리의 열 개수 N, 영화관 한 열에 속한 좌석 개수 M 두 자연수를 공백으로 구분해 입력합니다.
    # 1 <= N <= 26
    # 1 <= M <= 9
    # 각각 정수형으로 변환합니다.
    N, M = map(int, stdin.readline().split(' '))

    # 열 개수가 12개보다 적거나, 한 열에 속한 좌석 개수가 4개보다 적다면
    if N < 12 or M < 4:
        # L4 좌석이 없으므로 -1을 출력합니다.
        print(-1)
        # 다음 테스트 케이스로 넘어갑니다.
        continue

    # L4가 있다면 L4의 좌석 번호를 출력합니다.
    print(11 * M + 4)