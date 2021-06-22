# https://www.acmicpc.net/problem/1371

from sys import stdin


sentences = ''

while True:
    try:
        sentence = stdin.readline()
        sentences += sentence
    except EOFError:
        break

max_alphabet_cnt = 0
max_alphabet = ''

for alphabet in 'abcdefghijklmnopqrstuvwxyz':
    alphabet_cnt = sentences.count(alphabet)

    if alphabet_cnt > max_alphabet_cnt:
        max_alphabet_cnt = alphabet_cnt
        max_alphabet = alphabet
    elif alphabet_cnt == max_alphabet_cnt:
        max_alphabet += alphabet

print(max_alphabet)