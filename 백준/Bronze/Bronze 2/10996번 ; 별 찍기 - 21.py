# https://www.acmicpc.net/problem/10996

# 첫째 줄에 N을 입력합니다.
# 1 <= N <= 100
N = int(input())

half = int(N / 2)

for i in range(N):
    if N == 1 or half % 2 == 1:
        for j in range(half + 1):
            print("* ", end='')
        print()
    else:
        for j in range(half):
            print("* ", end='')
        print()

    for k in range(half):
        print(" *", end='')
    print()