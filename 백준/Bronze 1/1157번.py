# https://www.acmicpc.net/problem/1157

string = input().upper()

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
max_alpha = ''
max_count = 0

for alpha in alphabet:
    alpha_count = string.count(alpha)

    if alpha_count == max_count and alpha_count >= 1:
        max_alpha = '?'
        max_count = alpha_count
    elif alpha_count > max_count:
        max_alpha = alpha
        max_count = alpha_count
    else:
        continue

print(max_alpha)