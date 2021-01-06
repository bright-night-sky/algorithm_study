# https://www.acmicpc.net/problem/1284

while True:
    num_str = input()

    if num_str == '0':
        break

    width = 1 # 맨 왼쪽의 1cm는 무조건 들어가므로 미리 넣어놓음
    for num in num_str:
        if num == '1':
            width += 3
        elif num == '0':
            width += 5
        else:
            width += 4
    print(width)