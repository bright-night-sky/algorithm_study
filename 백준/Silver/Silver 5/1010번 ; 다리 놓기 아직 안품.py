# https://www.acmicpc.net/problem/1010

# 테스트 케이스 개수 T 입력
T = int(input())

# 각 테스트 케이스 실행
for i in range(0, T):
    # 강의 서쪽과 동쪽에 있는 사이트의 개수 N, M 입력
    # 정수, 0 < N <= M < 30
    N, M = map(int, input().split(' '))

    result = 1

    for i in range(1, N+1):
        result *= M
        M -= 1

    print(result)