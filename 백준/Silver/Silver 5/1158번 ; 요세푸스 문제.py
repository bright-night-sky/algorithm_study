# https://www.acmicpc.net/problem/1158

# 첫째 줄에 N, K를 빈 칸으로 구분해 입력합니다.
# 1 <= K <= N <= 5,000
N, K = map(int, input().split())

circle = [number for number in range(1, N + 1)]

poped_number = []

while True:
    circle_length = len(circle)

    if circle_length == 0:
        break