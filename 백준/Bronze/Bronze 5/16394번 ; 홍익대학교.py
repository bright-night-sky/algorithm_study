# https://www.acmicpc.net/problem/16394

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 줄에 특정 년도를 알리는 정수 N을 입력합니다.
# 1,946 <= N <= 1,000,000
# 정수형으로 변환합니다.
N = int(stdin.readline())

# N에서 1946을 빼 개교 주년을 출력합니다.
print(N - 1946)