# https://www.acmicpc.net/problem/2742

# 첫째 줄에 자연수 N을 입력합니다.
# N은 100,000보다 작거나 같은 자연수입니다.
N = int(input())

# 첫째 줄부터 N번째 줄까지 N부터 1까지 출력합니다.
for i in range(N, 0, -1):
    print(i)