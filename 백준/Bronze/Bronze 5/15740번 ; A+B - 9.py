# https://www.acmicpc.net/problem/15740

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 두 정수 A, B를 공백으로 구분해 입력합니다.
# -10^10000 <= A, B <= 10^10000
# 각각 정수형으로 변환합니다.
A, B = map(int, stdin.readline().split(' '))

# A, B의 합을 출력합니다.
print(A + B)