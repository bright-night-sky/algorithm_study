# https://www.acmicpc.net/problem/2798

card_num, blackjack = input().split(' ')
cards = list(map(int, input().split(' ')))

result = 0

for i in range(0, len(cards)-2):
    for j in range(i+1, len(cards)-1):
        for k in range(j+1, len(cards)):
            sum = cards[i] + cards[j] + cards[k]

            if sum <= int(blackjack) and sum >= result:
                result = sum

print(result)