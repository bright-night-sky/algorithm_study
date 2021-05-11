# https://www.acmicpc.net/problem/19572

# 3개의 양의 정수 d1, d2, d3를 입력합니다.
# 1 <= d1, d2, d3 <= 10^6
d1, d2, d3 = map(int, input().split(' '))

# 조건에 맞게 비를 내릴 수 있는지 저장하는 변수입니다.
# 초기화를 일단 -1로 해줍니다.
possible = -1

