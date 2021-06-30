# https://www.acmicpc.net/problem/21964

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 번째 줄에 문자열의 길이 N을 입력합니다.
# 정수형으로 변환합니다.
N = int(stdin.readline())
# 두 번째 줄에 N글자로 이루어진 문자열 S를 입력합니다.
# 맨 끝의 \n은 떼어줍니다.
S = stdin.readline().rstrip()

# 문자열 S의 마지막 5글자를 출력합니다.
print(S[-5:])