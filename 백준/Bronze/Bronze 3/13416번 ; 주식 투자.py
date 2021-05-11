# https://www.acmicpc.net/problem/13416

# 테스트 케이스의 개수 T를 입력합니다.
T = int(input())

# 테스트 케이스의 개수만큼 돌려봅니다.
for i in range(0, T):
    # 테스트 케이스의 첫째 줄에 환규가 정리한 주식 데이터의 일수 N을 입력합니다.
    # 자연수이며 1 <= N <= 1,000
    N = int(input())

    # 이번 테스트 케이스의 최대 이익을 저장하는 변수입니다.
    max_profit = 0

    # 일수만큼 돌려봅니다.
    for j in range(0, N):
        # 회사별 주식을 구매했을 때, 그날의 손익을 나타내는 3개의 정수 A, B, C를 입력합니다.
        # -1,000,000 <= A, B, C <= 1,000,000
        A, B, C = map(int, input().split(' '))

        # A, B, C 중 최대 이익을 구하는데,
        max_company = max(A, B, C)

        # 그 최대 이익이 양수인 경우에만
        if max_company > 0:
            # 최대 이익 변수에 더합니다.
            max_profit += max_company

    # 이번 테스트 케이스에서의 최대 이익을 출력합니다.
    print(max_profit)