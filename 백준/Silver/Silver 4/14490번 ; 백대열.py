# https://www.acmicpc.net/problem/14490

# readline을 사용하기 위해 import합니다.
from sys import stdin
# gcd를 사용하기 위해 import합니다.
from math import gcd

# n과 m을 :을 사이에 두고 입력합니다.
# 1 <= n, m <= 100,000,000
# 각각 정수형으로 변환합니다.
n, m = map(int, stdin.readline().split(':'))
# n과 m의 최대공약수를 저장하는 변수를 선언합니다.
gcd_num = gcd(n, m)

# n과 m을 gcd_num으로 나눈 몫들을 출력 형식에 맞게 출력합니다.
print(f"{n // gcd_num}:{m // gcd_num}")