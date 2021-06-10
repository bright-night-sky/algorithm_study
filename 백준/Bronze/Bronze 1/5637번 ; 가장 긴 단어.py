# https://www.acmicpc.net/problem/5637

from sys import stdin

longest_word = None
longest_word_len = 0

aa = 'ddd'
aa.

while True:
    line = stdin.readline().rstrip()
    words = line.split(' ')

    for word in words:

        word_len = len(word)

        if word_len > longest_word_len:
            longest_word = word
            longest_word_len = word_len

    if line[-5:] == 'E-N-D':
        break

print(longest_word.lower())