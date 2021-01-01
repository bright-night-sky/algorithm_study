# https://www.acmicpc.net/problem/2475

nums = list(map(int, input().split(' ')))
sum = 0
result = 0

for num in nums:
    sum += num ** 2

result = sum % 10
print(result)