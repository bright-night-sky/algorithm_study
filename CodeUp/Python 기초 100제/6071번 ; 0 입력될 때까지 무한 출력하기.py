# https://codeup.kr/problem.php?id=6071

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 입력한 숫자를 저장할 변수를 선언합니다.
# 처음에는 None으로 초기화합니다.
num = None

# num의 값이 0이 아니라면 계속 반복해봅니다.
while num != 0:
    # 임의의 정수를 하나 입력하고, 정수형으로 변환합니다.
    # 그 값을 num에 넣어줍니다.
    num = int(stdin.readline())

    # num의 값이 0이 아니라면
    if num != 0:
        # num의 값을 출력합니다.
        print(num)