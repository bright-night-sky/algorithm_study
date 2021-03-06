# https://www.acmicpc.net/problem/16435

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫 번째 줄에 과일의 개수 N, 스네이크버드의 초기 길이 정수 L을 공백으로 구분해 입력합니다.
# 1 <= N <= 1,000
# 1 <= L <= 10,000
# 각각 정수형으로 변환합니다.
N, L = map(int, stdin.readline().split(' '))
# 두 번째 줄에는 과일의 높이 hi들을 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환하고 리스트 변수에 넣어줍니다.
his = list(map(int, stdin.readline().split(' ')))

# 스네이크버드가 과일을 가장 많이 먹는 방법을 구하면 되므로
# 높이가 가장 낮은 과일부터 하나씩 먹어가면 스네이크버드의 길이를 최대로 늘릴 수 있습니다.
# hi들을 오름차순으로 정렬합니다.
his.sort()

# 정렬된 hi들을 하나씩 반복해봅니다.
for hi in his:
    # 현재 스네이크버드의 길이가 현재 과일의 높이보다 길거나 같다면
    if L >= hi:
        # 과일을 먹을 수 있으므로 스네이크버드의 길이에 1을 더합니다.
        L += 1
    # 현재 스네이크버드의 길이가 현재 과일의 높이보다 작다면
    else:
        # 더 이상 과일을 먹지 못하므로 반복문을 탈출합니다.
        break

# 스네이크버드의 최대 길이를 출력합니다.
print(L)
