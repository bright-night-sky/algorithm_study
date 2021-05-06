# https://www.acmicpc.net/problem/2751

# 첫째 줄에 수의 개수 N을 입력합니다.
# 1 <= N <= 1,000,000
N = int(input())

numbers = []

for number_index in range(N):
    number = int(input())

    numbers.append(number)

numbers.sort()

for number in numbers:
    print(number)