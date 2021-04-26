# https://www.acmicpc.net/problem/11383

# 첫 번째 줄에 N, M을 입력합니다.
# 1 <= N, M <= 10
N, M = map(int, input().split(' '))

origin_words = []
twice_words = []

for i in range(N):
    word = input()

    origin_words.append(word)

for i in range(N):
    twice_word = input()

    twice_words.append(twice_word)

