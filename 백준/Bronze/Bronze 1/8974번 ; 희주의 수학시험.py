# https://www.acmicpc.net/problem/8974

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 한 줄에 양의 정수 A, B를 공백으로 구분해 입력합니다.
# 1 <= A <= B <= 1000
# 각각 정수형으로 변환합니다.
A, B = map(int, stdin.readline().split(' '))
# B번째까지의 숫자를 포함한 수열들을 저장할 리스트 변수를 선언합니다.
series = []

# 수열은 1부터 시작하므로 1로 초기화된 숫자 변수를 하나 선언합니다.
number = 1
# 수열에 숫자 넣기를 계속 반복해봅니다.
while True:
    # 현재 수열의 길이가 B보다 크거나 같다면
    if len(series) >= B:
        # 반복문을 탈출합니다.
        break

    # 현재 숫자만큼 반복합니다.
    for _ in range(number):
        # 수열에 현재 숫자를 그 숫자만큼 넣습니다.
        series.append(number)

    # number에 1을 더해줍니다.
    number += 1

# 수열에서 A번째부터 B번째까지의 합을 출력합니다.
print(sum(series[A-1:B]))