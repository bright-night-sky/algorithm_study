# https://www.acmicpc.net/problem/2439

# 첫째 줄에 N(1 <= N <= 100) 입력
num = int(input())

# 첫째 줄부터 N번째 줄까지
for i in range(0, num):
    # 공백 입력
    for j in range(0, num-i-1):
        print(' ', end='')

    # 별 입력
    for k in range(0, i+1):
        print('*', end='')

    # 한 줄 입력을 끝냈으니 줄 바꾸기
    print()