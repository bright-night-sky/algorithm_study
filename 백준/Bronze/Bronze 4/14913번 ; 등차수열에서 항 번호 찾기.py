# https://www.acmicpc.net/problem/14913

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 줄에 첫 항 a, 공차 d, 찾는 수 k를 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
a, d, k = map(int, stdin.readline().split(' '))
# 등차수열의 공식 a+(n-1)d = k을 dn = k - a + d로 계산하여 값을 저장한 변수를 선언합니다.
dn = k - a + d

# n을 구하기 위해 dn을 d로 나누었을 때 나머지가 0이고 그 n이 1보다 크거나 같다면
if dn % d == 0 and dn // d >= 1:
    # k는 등차수열의 수가 맞으므로 몇 번째 항인지 출력합니다.
    print(dn // d)
# 그 외의 경우에는
else:
    # k는 등차수열의 수가 아니므로 X를 출력합니다.
    print("X")