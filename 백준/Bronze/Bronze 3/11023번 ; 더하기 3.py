# https://www.acmicpc.net/problem/11023

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 N개의 수를 공백으로 구분해 입력합니다.
# 수들은 10,000보다 작거나 같은 자연수입니다.
# 각각 정수형으로 변환하고 리스트 변수에 넣어줍니다.
N = list(map(int, stdin.readline().split(' ')))

# N에 있는 자연수들의 합을 출력합니다.
print(sum(N))