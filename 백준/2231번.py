# https://www.acmicpc.net/problem/2231
# 실행 시간 줄여보자

num = int(input())
result = 0

for i in range(1, num):
    sum = 0

    string_i = str(i)
    sum += i
    for j in string_i:
        sum += int(j)

    if sum == num:
        result = i
        break

print(result)