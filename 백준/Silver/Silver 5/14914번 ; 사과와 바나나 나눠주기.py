# https://www.acmicpc.net/problem/14914

# readline을 사용하기 위해 import합니다.
from sys import stdin
# gcd를 사용하기 위해 import합니다.
from math import gcd

# 첫째 줄에 사과의 개수 a, 바나나의 개수 b를 공백으로 구분해 입력합니다.
# 1 <= a, b <= 1,000
# 각각 정수형으로 변환합니다.
a, b = map(int, stdin.readline().split(' '))
# a, b의 최대공약수를 저장하는 변수를 선언합니다.
ab_gcd = gcd(a, b)

# 친구의 수를 1부터 ab_gcd의 절반까지 반복합니다.
for friend in range(1, ab_gcd // 2 + 1):
    # ab_gcd를 현재 친구의 수로 나누었을 때 나머지가 0이라면
    if ab_gcd % friend == 0:
        # 친구의 수, 사과 개수, 바나나 개수를 차례대로 출력 형식에 맞게 출력합니다.
        print(friend, a // friend, b // friend)

# 친구의 수가 ab_gcd일 때의 친구의 수, 사과 개수, 바나나 개수를 차례대로 출력 형식에 맞게 출력합니다.
print(ab_gcd, a // ab_gcd, b // ab_gcd)