# https://www.acmicpc.net/problem/1145

# 첫째 줄에 다섯 개의 자연수를 입력합니다.
# 100보다 작거나 같은 자연수이고, 서로 다른 수입니다.
numbers = list(map(int, input().split(' ')))

least_most_multiple = max(numbers)

while True:
    multiple_count = 0

    for number in numbers:
        if least_most_multiple % number == 0:
            multiple_count += 1

    if multiple_count >= 3:
        print(least_most_multiple)
        break
    else:
        least_most_multiple += 1
