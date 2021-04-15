# https://www.acmicpc.net/problem/5176

# 첫째 줄에 테스트 케이스의 개수 K를 입력합니다.
K = int(input())

for i in range(K):
    # 첫째 줄에 참가자의 수 P, 자리의 수 M을 입력합니다.
    # 1 <= P, M <= 500
    P, M = map(int, input().split(' '))

    