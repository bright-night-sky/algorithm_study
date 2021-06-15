# https://www.acmicpc.net/problem/17256

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 케이크 수 a를 구성하는 자연수 a.x, a.y, a.z를 공백으로 구분해 입력합니다.
# 1 <= a.x, a.y, a.z <= 100
# 각각 정수형으로 변환합니다.
ax, ay, az = map(int, stdin.readline().split(' '))
# 둘째 줄에 케이크 수 c를 구성하는 자연수 c.x, c.y, c.z를 공백으로 구분해 입력합니다.
# 1 <= c.x, c.y, c.z <= 100
# 각각 정수형으로 변환합니다.
cx, cy, cz = map(int, stdin.readline().split(' '))

# c.x에서 a.z를 빼 b.x를
# c.y에서 a.y를 나누어 b.y를
# c.z에서 a.x를 빼 b.z를 구해서 공백으로 구분해 출력합니다.
print(cx - az, cy // ay, cz - ax)