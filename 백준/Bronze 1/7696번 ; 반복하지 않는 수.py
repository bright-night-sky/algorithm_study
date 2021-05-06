# https://www.acmicpc.net/problem/7696

# 0을 입력할 때까지 반복합니다.
while True:
    n = int(input())

    if n == 0:
        break
    else:
        repeat_num = ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99']

        number = 1

        while True:
            if str(number)