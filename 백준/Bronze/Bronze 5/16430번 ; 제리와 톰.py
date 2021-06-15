# https://www.acmicpc.net/problem/16430

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 번째 줄에 두 정수 A, B를 공백으로 구분해 입력합니다.
# 1 <= A < B <= 9
# A, B는 서로소임이 보장됩니다.
# 각각 정수형으로 변환합니다.
A, B = map(int, stdin.readline().split(' '))

# P는 B에서 A를 뺀 값입니다.
P = B - A

# A와 B는 서로소이므로 Q는 B와 같습니다.
# P와 B를 공백으로 구분해 출력합니다.
print(P, B)