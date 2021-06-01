# https://www.acmicpc.net/problem/8595

from sys import stdin

n = int(stdin.readline().rstrip())
word = stdin.readline().rstrip()
hidden_num_sum = 0
hidden_num = ''

for character in word:
    if character in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        hidden_num += character
    else:
        if hidden_num != '':
            hidden_num_sum += int(hidden_num)
            hidden_num = ''

print(hidden_num_sum)