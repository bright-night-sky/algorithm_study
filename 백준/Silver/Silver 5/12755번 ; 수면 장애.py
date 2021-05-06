# https://www.acmicpc.net/problem/12755

# 첫째 줄에 N번째 숫자를 나타내는 N을 입력합니다.
# 1 <= N <= 100,000,000
N = int(input())

num_string = ''

number = 1

while True:
    num_string += str(number)

    num_string_length = len(num_string)

    if num_string_length >= N:
        print(num_string[N - 1])
        break

    number += 1