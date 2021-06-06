# https://www.acmicpc.net/problem/1205

from sys import stdin

N, new_score, P = map(int, stdin.readline().split(' '))
scores = list(map(int, stdin.readline().split(' ')))

scores.append(new_score)
scores.sort(reverse=True)

new_score_idx = scores.index(new_score)

if new_score_idx > P:
    print(-1)
else:
    new_score_rank = 1

    for score_idx in range(len(scores[:new_score_idx])):
        if scores[score_idx] > new_score:
            new_score_rank += 1

    print(new_score_rank)