# https://www.acmicpc.net/problem/2438

# 첫째 줄에 N(1 <= N <= 100) 입력
num = int(input())

# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력
for i in range(1, num+1):
    print('*' * i)