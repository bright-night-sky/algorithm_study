# https://www.acmicpc.net/problem/2947

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 조각에 쓰여 있는 수를 공백으로 구분해 순서대로 입력합니다.
# 숫자는 1보다 크거나 같고, 5보다 작거나 같으며 중복되지 않습니다.
# 처음 순서는 1, 2, 3, 4, 5가 아닙니다.
piece_num = list(map(int, stdin.readline().rstrip().split(' ')))

# 순서가 1, 2, 3, 4, 5가 될 때까지 반복합니다.
while True:
    # 순서가 1, 2, 3, 4, 5라면
    if piece_num == [1, 2, 3, 4, 5]:
        # 반복문을 탈출합니다.
        break
    # 순서가 1, 2, 3, 4, 5가 아니라면
    else:
        # 1번 과정의 조건인 첫 번째 조각의 수가 두 번째 수보다 크다면
        if piece_num[0] > piece_num[1]:
            # 둘의 위치를 서로 바꿉니다.
            piece_num[0], piece_num[1] = piece_num[1], piece_num[0]
            # 위치가 바뀌었으므로 조각의 순서를 출력 형식에 맞게 출력합니다.
            print(" ".join(list(map(str, piece_num))))

        # 2번 과정의 조건인 두 번째 조각의 수가 세 번째 수보다 크다면
        if piece_num[1] > piece_num[2]:
            # 둘의 위치를 서로 바꿉니다.
            piece_num[1], piece_num[2] = piece_num[2], piece_num[1]
            # 위치가 바뀌었으므로 조각의 순서를 출력 형식에 맞게 출력합니다.
            print(" ".join(list(map(str, piece_num))))

        # 3번 과정의 조건인 세 번째 조각의 수가 네 번째 수보다 크다면
        if piece_num[2] > piece_num[3]:
            # 둘의 위치를 서로 바꿉니다.
            piece_num[2], piece_num[3] = piece_num[3], piece_num[2]
            # 위치가 바뀌었으므로 조각의 순서를 출력 형식에 맞게 출력합니다.
            print(" ".join(list(map(str, piece_num))))

        # 4번 과정의 조건인 네 번째 조각의 수가 다섯 번째 수보다 크다면
        if piece_num[3] > piece_num[4]:
            # 둘의 위치를 서로 바꿉니다.
            piece_num[3], piece_num[4] = piece_num[4], piece_num[3]
            # 위치가 바뀌었으므로 조각의 순서를 출력 형식에 맞게 출력합니다.
            print(" ".join(list(map(str, piece_num))))
