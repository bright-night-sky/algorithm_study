# https://www.acmicpc.net/problem/11931

# 첫째 줄에 수의 개수 N을 입력합니다.
# 1 <= N <= 1,000,000
N = int(input())

nums = []

for num_index in range(N):
    num = int(input())

    nums.append(num)

nums.sort(reverse=True)

for num in nums:
    print(num)