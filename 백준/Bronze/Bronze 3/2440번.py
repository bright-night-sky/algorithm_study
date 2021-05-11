# https://www.acmicpc.net/problem/2440

# 첫째 줄에 N(1 <= N <= 100) 입력
num = int(input())

# 한 줄당 별을 한 개씩 차감하면서 출력
for i in range(num, 0, -1):
    print('*' * i)