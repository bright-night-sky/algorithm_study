# https://www.acmicpc.net/problem/10808

word = input()

alphabets = 'abcdefghijklmnopqrstuvwxyz'

for alphabet in alphabets:
    print(word.count(alphabet), end=' ')