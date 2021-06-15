# https://www.acmicpc.net/problem/14652

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 관중석의 크기를 나타내는 N, M과 관중석 번호인 K를 공백으로 구분해 입력합니다.
# 1 <= N, M <= 30,000
# 0 <= K <= N*M-1
# 각각 정수형으로 변환합니다.
N, M, K = map(int, stdin.readline().split(' '))

# 잃어버린 좌표 n은 K를 M으로 나눈 몫입니다.
n = K // M
# 잃어버린 좌표 m은 n과 M을 곱한 값을 K에서 뺀 값입니다.
m = K - n * M

# n, m을 공백으로 구분해 출력합니다.
print(n, m)