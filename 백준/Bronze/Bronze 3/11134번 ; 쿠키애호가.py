# https://www.acmicpc.net/problem/11134

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 번째 줄에는 테스트 케이스의 개수 T를 입력합니다.
# 0 < T < 100
# 정수형으로 변환합니다.
T = int(stdin.readline())

# 테스트 케이스의 개수 T만큼 반복합니다.
for test_case_idx in range(T):
    # 철수가 가진 쿠키의 개수 N, 날마다 먹는 쿠키의 개수 C를 공백으로 구분해 입력합니다.
    # 0 < N < 1,000,000,000
    # 0 < C < 5,000
    # 각각 정수형으로 변환합니다.
    N, C = map(int, stdin.readline().split(' '))

    # N을 C로 나누었을 때 나머지가 0이라면
    if N % C == 0:
        # 철수가 쿠키를 먹을 수 있는 날짜인 N을 C로 나누고 나온 몫을 출력합니다.
        print(N // C)
    # N을 C로 나누었을 때 나머지가 0이 아니라면
    else:
        # 철수가 쿠키를 먹을 수 있는 날짜인 N을 C로 나누고 나온 몫에 1을 더한 값을 출력합니다.
        print(N // C + 1)