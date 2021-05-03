# https://www.acmicpc.net/problem/2018

# 첫 줄에 정수 N을 입력합니다.
# 1 <= N <= 10,000,000
N = int(input())

method = 0

for start in range(1, N + 1):
    case = 0
    i = 0

    while True:
        case += start + i

        if case >= N:
            if case == N:
                method += 1
            else:
                break

        i += 1

print(method)