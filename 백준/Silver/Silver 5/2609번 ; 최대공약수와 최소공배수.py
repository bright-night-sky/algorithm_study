# https://www.acmicpc.net/problem/2609

# readline을 사용하기 위해 import합니다.
from sys import stdin
# gcd, lcm 함수를 사용하기 위해 import합니다.
from math import gcd, lcm

# 첫째 줄에 두 개의 자연수를 공백으로 구분해 입력합니다.
# 10,000 이하의 자연수입니다.
# 각각 정수형으로 변환합니다.
number1, number2 = map(int, stdin.readline().split(' '))

# gcd, lcm 함수를 이용해 최대공약수와 최소공배수를 출력 형식에 맞게 출력합니다.
print(gcd(number1, number2))
print(lcm(number1, number2))