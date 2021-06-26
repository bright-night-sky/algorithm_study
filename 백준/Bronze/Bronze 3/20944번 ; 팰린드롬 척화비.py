# https://www.acmicpc.net/problem/20944

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 수미상관이면서 팰린드롬인 문자열의 길이 N을 입력합니다.
# 1 <= N <= 1,000,000
# 정수형으로 변환합니다.
N = int(stdin.readline())

# 수미상관이면서 팰린드롬이며 길이가 N인 문자열을 아무거나 찾으면 되므로
# 그냥 길이가 N인 a로만 이루어진 문자열이면 조건이 만족됩니다.
print('a' * N)