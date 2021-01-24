# https://www.acmicpc.net/problem/19946

# 양의 정수 N 입력
# N은 태영이가 2^64를 계산했을 때 나올 수 있는 수
# 2 <= N <= 2^64 - 1
N = int(input())

for i in range(0, 64):
    if N % 2 == 1:
        print(64 - i)
        break
    else:
        N = N / 2
