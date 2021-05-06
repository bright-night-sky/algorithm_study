# https://www.acmicpc.net/problem/17176

# 첫 번째 줄에는 주어질 수열의 길이 N을 입력합니다.
# 1 <= N <= 100,000
N = int(input())

cipher_nums = list(map(int, input().split(' ')))

origin_string = list(input())

result = "y"

for cipher_num in cipher_nums:
    decipher_char = ''

    if cipher_num == 0:
        decipher_char = ' '
    elif 1 <= cipher_num <= 26:
        decipher_char = chr(cipher_num + 64)
    elif 27 <= cipher_num <= 52:
        decipher_char = chr(cipher_num + 70)

    if origin_string.count(decipher_char) >= 1:
        origin_string.remove(decipher_char)
    else:
        result = "n"
        break

print(result)