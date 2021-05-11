# https://www.acmicpc.net/problem/8595

from sys import stdin

n = int(stdin.readline().rstrip())

word = stdin.readline()

hidden_num_sum = 0

hidden_num = ''

for character in word:
    if ord('0') <= ord(character) <= ord('9'):
        hidden_num += character
    elif hidden_num != '' and ord(character) > ord('9'):
        hidden_num_sum += int(hidden_num)
        hidden_num = ''

print(hidden_num_sum)