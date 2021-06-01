# https://www.acmicpc.net/problem/13706

# readline을 사용하기 위해 import합니다.
from sys import stdin
# isqrt를 사용하기 위해 import합니다.
from math import isqrt

# 첫째 줄에 양의 정수 N을 입력합니다.
# 항상 정수이며 길이는 800자리를 넘지 않습니다.
# 정수형으로 변환합니다.
N = int(stdin.readline())

# 정수 N의 제곱근을 출력합니다.
print(isqrt(N))