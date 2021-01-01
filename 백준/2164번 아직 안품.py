# https://www.acmicpc.net/problem/2164

num = int(input())
deck = [i for i in range(1, num+1)]


while True:
    if len(deck) == 1:
        print(deck[0])
        break

    del deck[0]
    deck.append(deck[0])
    del deck[0]
