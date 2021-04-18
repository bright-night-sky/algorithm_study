# https://www.acmicpc.net/problem/5533

# 첫째 줄에 참가자의 수 N을 입력합니다.
# 2 <= N <= 200
N = int(input())

player_scores = []

for i in range(N):
    one_player_score = input().split(' ')

    player_scores.append(one_player_score)

