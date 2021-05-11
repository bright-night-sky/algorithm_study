# https://www.acmicpc.net/problem/5533

# 첫째 줄에 참가자의 수 N을 입력합니다.
# 2 <= N <= 200
N = int(input())

players_cards = []

for player_index in range(N):
    one_player_cards = input().split(' ')

    players_cards.append(one_player_cards)

