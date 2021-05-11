# https://www.acmicpc.net/problem/1526

# 첫째 줄에 N을 입력합니다.
# 4보다 크거나 같고 1,000,000보다 작거나 같은 자연수입니다.
N = int(input())

while True:
    N = str(N)

    not_4_7 = ['0', '1', '2', '3', '5', '6', '8', '9']

    for number in N:
        if number in not_4_7:
            N = int(N) - 1
            break

