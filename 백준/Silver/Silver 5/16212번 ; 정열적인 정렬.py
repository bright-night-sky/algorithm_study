# https://www.acmicpc.net/problem/16212

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에는 수열의 길이 N을 입력합니다.
# 1 <= N <= 500,000
# 정수형으로 변환합니다.
N = int(stdin.readline())
# 둘째 줄에는 수열의 각 원소 ai들을 공백을 사이에 두고 입력합니다.
# ai의 절댓값은 200만 이하입니다.
# 각각 정수형으로 변환하고 리스트 변수에 넣어줍니다.
ais = list(map(int, stdin.readline().split(' ')))

# ais의 값들을 오름차순으로 정렬합니다.
ais.sort()

# 오름차순으로 정렬된 원소들을 출력 형식에 맞게 출력합니다.
for ai in ais:
    print(ai, end=' ')