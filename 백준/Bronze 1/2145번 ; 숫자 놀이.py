# https://www.acmicpc.net/problem/2145

# 0을 입력할 때까지 반복합니다.
while True:
    # N을 입력합니다.
    # 100,000보다 작은 양의 정수입니다.
    N = input()

    # 입력한 N이 0이라면
    if N == '0':
        # 반복문을 탈출해 종료합니다.
        break
    # 입력한 N이 0이 아니라면
    else:
        # 새로 값을 넣은 N의 길이가 1일 때까지 반복합니다.
        while True:
            # N의 길이가 1이라면
            if len(N) == 1:
                # N을 출력합니다.
                print(N)
                # 반복문을 탈출합니다.
                break
            # N의 길이가 1 초과라면
            else:
                # N의 각 자리 숫자를 모두 더하고 문자열 형태로 변환 후 다시 N에 넣어줍니다.
                N = str(sum(list(map(int, N))))
