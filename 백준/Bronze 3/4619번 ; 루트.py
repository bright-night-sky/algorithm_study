# https://www.acmicpc.net/problem/4619

# 0 0을 입력하기 전까지 계속 테스트한다.
while True:
    # 양의 정수 B, N 입력
    # 1 <= B <= 1,000,000
    # 1 <= N <= 9
    B, N = map(int, input().split(' '))

    # 만약 0 0으로 입력한다면
    if B == N == 0:
        # 반복문 탈출
        break

    # A의 값을 저장할 변수
    A = 1

    # 조건을 만족할 때까지 반복
    while True:
        # 만약 B보다 A^N이 크거나 같으면
        if B <= A ** N:
            # 반복문 탈출
            break

        # 조건을 찾을 때까지 A에 1씩 더한다.
        A += 1

    # B와 A^N의 차이
    A_differ = abs(B - A ** N)
    # B와 (A-1)^N의 차이
    A_1_differ = abs(B - (A - 1) ** N)

    # 만약 B에서 A^N의 차이보다 (A-1)^N의 차이가 더 크다면
    if A_differ < A_1_differ:
        # A가 더 가까운 정수이다.
        print(A)
    # 만약 B에서 A^N의 차이가 (A-1)^N의 차이보다 더 크다면
    else:
        # (A-1)이 더 가까운 정수이다.
        print(A - 1)