# https://www.acmicpc.net/problem/6359

# 첫 번째 줄에는 테스트 케이스의 개수 T를 입력합니다.
T = int(input())

for i in range(T):
    n = int(input())

    prison = ['open' for x in range(n)]

    for index in range(len(prison)):
