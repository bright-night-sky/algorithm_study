# https://www.acmicpc.net/problem/1712

A, B, C = map(int, input().split(' '))

total_cost = A
total_income = 0
num = 1

if B >= C:
    print(-1)
else:
    while True:
        total_cost = A + B * num
        total_income = C * num

        if total_cost < total_income:
            print(num)
            break

        num += 1
