# https://www.acmicpc.net/problem/10569

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 번째 줄에 자연수 T를 입력합니다.
# 1 <= T <= 100
# 정수형으로 변환합니다.
T = int(stdin.readline())

# T만큼 반복합니다.
for _ in range(T):
    # 꼭짓점의 개수 V, 모서리의 개수 E를 공백으로 구분해 입력합니다.
    # 4 이상 100 이하의 자연수입니다.
    # 각각 정수형으로 변환합니다.
    V, E = map(int, stdin.readline().split(' '))

    # 2 - (꼭짓점의 개수) + (모서리의 개수)로 면의 수를 계산하고 출력합니다.
    print(2 - V + E)