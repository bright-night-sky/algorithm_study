# https://www.acmicpc.net/problem/1009

test_case = int(input())

for i in range(0, test_case):
    a, b = map(int, input().split(' '))
    one_pattern = [] # 3, 9, 7, 1
    one_position = 1

    for i in range(0, 10):
        one_position = a * one_position

        if len(one_pattern) == 0 or one_pattern[0] != int(str(one_position)[-1]):
            one_pattern.append(int(str(one_position)[-1]))
        else:
            break

    # 이 밑부분을 못 풀고 있다.
    idx = int(len(one_pattern) / 10) - 1
    print(one_pattern[idx])