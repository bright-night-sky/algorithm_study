# https://codeup.kr/problem.php?id=6078

# readline을 사용하기 위해 import합니다.
from sys import stdin


# q를 입력할 때까지 계속 반복합니다.
while True:
    # 문자 1개를 입력합니다.
    # 맨 끝의 \n은 떼어줍니다.
    char = stdin.readline().rstrip()

    # 입력한 문자를 출력합니다.
    print(char)

    # 입력한 문자가 q라면
    if char == 'q':
        # 반복문을 탈출합니다.
        break