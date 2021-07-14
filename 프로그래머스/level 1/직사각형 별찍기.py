# https://programmers.co.kr/learn/courses/30/lessons/12969

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 두 개의 정수 n, m을 공백으로 구분해 입력합니다.
# n, m은 각각 1,000 이하인 자연수입니다.
# 각각 정수형으로 변환합니다.
n, m = map(int, stdin.readline().split(' '))

# 행의 개수인 m만큼 반복합니다.
for _ in range(m):
    # 한 행에 *을 n개만큼 출력합니다.
    print('*' * n)