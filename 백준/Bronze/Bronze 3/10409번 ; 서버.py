# https://www.acmicpc.net/problem/10409

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 줄은 일의 개수 n, 주어진 시간 T를 공백으로 구분해 입력합니다.
# 1 <= n <= 50
# 1 <= T <= 500
# 각각 정수형으로 변환합니다.
n, T = map(int, stdin.readline().split(' '))
# 두 번째 줄에는 n개의 100 이하인 각 일의 수행 시간을 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환하고 리스트 변수에 넣어줍니다.
perform_time = list(map(int, stdin.readline().split(' ')))

# 1부터 일의 개수 n만큼 반복합니다.
for idx in range(1, n + 1):
    # 일의 수행 시간의 현재 인덱스까지의 합이 주어진 시간 T보다 크다면
    if sum(perform_time[:idx]) > T:
        # 현재 인덱스에서 1을 빼준 값을 출력합니다.
        print(idx - 1)
        # 반복문을 탈출합니다.
        break
    # 주어진 시간 T 내에 모든 일을 완료할 수 있을 때,
    # 즉, 일의 수행 시간의 인덱스 끝까지의 합이 주어진 시간 T보다 작거나 같다면
    elif sum(perform_time[:idx]) <= T and idx == n:
        # 현재 인덱스를 출력합니다.
        print(idx)