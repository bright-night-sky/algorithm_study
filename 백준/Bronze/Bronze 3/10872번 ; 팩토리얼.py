# https://www.acmicpc.net/problem/10872

# readline을 사용하기 위해 import합니다.
from sys import stdin
# factorial을 사용하기 위해 import합니다.
from math import factorial


# 첫째 줄에 정수 N을 입력합니다.
# 0 <= N <= 12
# 정수형으로 변환합니다.
N = int(stdin.readline())

# N!을 출력합니다.
print(factorial(N))