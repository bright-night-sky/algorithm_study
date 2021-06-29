# https://www.acmicpc.net/problem/11050

# readline을 사용하기 위해 import합니다.
from sys import stdin
# factorial을 사용하기 위해 import합니다.
from math import factorial


# 첫째 줄에 자연수 N, 정수 K를 공백으로 구분해 입력합니다.
# 1 <= N <= 10
# 0 <= K <= N
# 각각 정수형으로 변환합니다.
N, K = map(int, stdin.readline().split(' '))

# 이항 계수의 정의에 맞게 식을 세우고 계산한 뒤 출력합니다.
# nCk = n! / ((n-k)!k!)
print(factorial(N) // (factorial(N - K) * factorial(K)))