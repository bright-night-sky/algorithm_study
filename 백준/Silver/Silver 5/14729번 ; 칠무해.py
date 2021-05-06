# https://www.acmicpc.net/problem/14729

# 첫째 줄에 학생의 수 N을 입력합니다.
# 8 <= N <= 10,000,000
N = int(input())

scores = []

for score_index in range(N):
    score = float(input())

    scores.append(score)

scores.sort()

for score_index in range(7):
    print("{:.3f}".format(scores[score_index]))