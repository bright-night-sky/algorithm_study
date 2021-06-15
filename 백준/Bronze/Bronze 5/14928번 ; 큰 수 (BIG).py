# https://www.acmicpc.net/problem/14928

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 제연이가 가장 좋아하는 수 N을 입력합니다.
# N <= 10^1,000,000
# 정수형으로 변환합니다.
N = int(stdin.readline())

# N을 20000303으로 나눈 나머지를 출력합니다.
print(N % 20000303)