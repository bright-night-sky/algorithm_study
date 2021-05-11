# https://www.acmicpc.net/problem/8974

# 양의 정수 A, B를 입력합니다.
# 1 <= A <= B <= 1000
A, B = map(int, input().split(' '))

series = []

for index in range(1, B + 1):
    for num in range(1, index + 1):
        series.append(index)

print(series)