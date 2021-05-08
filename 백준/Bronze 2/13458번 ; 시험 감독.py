# https://www.acmicpc.net/problem/13458

from math import ceil

# 첫째 줄에 시험장의 개수 N을 입력합니다.
# 1 <= N <= 1,000,000
N = int(input())

for test_site_index in range(N):
    Ai = int(input())
    B, C = map(int, input().split(' '))

    total_inspector_count = 1

    if Ai > B:
        assist_inspector_count = ceil((Ai - B) / C)
        total_inspector_count += assist_inspector_count

    print(total_inspector_count)