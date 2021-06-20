# https://www.acmicpc.net/problem/10871

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 수열의 개수 N, 비교할 수 X를 공백으로 구분해 입력합니다.
# 1 <= N, X <= 10,000
# 각각 정수형으로 변환합니다.
N, X = map(int, stdin.readline().split(' '))
# 둘째 줄에 수열 A를 이루는 정수 N개들을 공백으로 구분해 입력합니다.
# 모두 1보다 크거나 같고, 10,000보다 작거나 같습니다.
# 각각 정수형으로 변환하고 리스트 변수에 넣어줍니다.
A = list(map(int, stdin.readline().split(' ')))

# 수열 A의 정수들 중에서 X보다 작은 정수들만 필터링합니다.
small_than_X = filter(lambda number: number < X, A)

# X보다 작은 수들을 출력 형식에 맞게 출력합니다.
for number in small_than_X:
    print(number, end=' ')