# https://www.acmicpc.net/problem/2739

# 첫째 줄에 N을 입력합니다.
# 1 <= N <= 9
N = int(input())

# 출력 형식에 맞게 N*1부터 N*9까지 출력합니다.
for i in range(1, 10):
    print(f"{N} * {i} = {N * i}")