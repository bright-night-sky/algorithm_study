# https://www.acmicpc.net/problem/2774

# 첫째 줄에는 테스트 케이스의 개수 T를 입력합니다.
T = int(input())

for test_case_index in range(T):
    X = input()

    beautiful = 0

    for number in range(1, 10):
        number_count = X.count(str(number))

        if number_count >= 1:
            beautiful += number_count

    print(beautiful)
