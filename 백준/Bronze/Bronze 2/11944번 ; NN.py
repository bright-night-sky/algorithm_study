# https://www.acmicpc.net/problem/11944

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 번째 줄에 N, M을 공백으로 구분해 입력합니다.
# 1 <= N, M <= 2016
# 각각 정수형으로 변환합니다.
N, M = map(int, stdin.readline().split(' '))

# N을 N번 출력했을 때의 길이가 M보다 크다면
if len(str(N) * N) > M:
    # N을 N번 반복한 것의 앞 M자리까지만 출력합니다.
    print((str(N) * N)[:M])
# N을 N번 출력했을 때의 길이가 M보다 작거나 같다면
else:
    # N을 N번 출력합니다.
    print(str(N) * N)