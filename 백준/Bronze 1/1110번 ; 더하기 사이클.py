# https://www.acmicpc.net/problem/1110

# 첫째 줄에 N을 입력합니다.
# N은 0보다 크거나 같고, 99보다 작거나 같은 정수입니다.
N = input()

temp = N

cycle = 0

while True:
    if 0 <= int(temp) <= 9:
        temp = '0' + temp

    cycle += 1
    new_num = temp[1] + str(int(temp[0]) + int(temp[1]))[1]

    if N == new_num:
        print(cycle)
        break
    else:
        temp = new_num
