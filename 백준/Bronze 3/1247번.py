# https://www.acmicpc.net/problem/1247

for i in range(0, 3):
    N = int(input())
    sum = 0

    for j in range(0, N):
        num = int(input())
        sum += num

    if sum == 0:
        print('0')
    elif sum > 0:
        print('+')
    else:
        print('-')