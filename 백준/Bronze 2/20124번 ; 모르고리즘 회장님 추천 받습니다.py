# https://www.acmicpc.net/problem/20124

# 첫째 줄에 사람의 수 N을 입력합니다.
# 1 <= N <= 100,000
N = int(input())

pairs = {}

for i in range(N):
    person, score = input().split(' ')

    pairs[person] = score

