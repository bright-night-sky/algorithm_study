# https://codeup.kr/problem.php?id=6067

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 정수 1개를 입력합니다.
# 정수형으로 변환합니다.
num = int(stdin.readline())

# 입력한 정수가 음수이면서 짝수이면
if num < 0 and num % 2 == 0:
    # A를 출력합니다.
    print("A")
# 입력한 정수가 음수이면서 홀수이면
elif num < 0 and num % 2 != 0:
    # B를 출력합니다.
    print("B")
# 입력한 정수가 양수이면서 짝수이면
elif num > 0 and num % 2 == 0:
    # C를 출력합니다.
    print("C")
# 입력한 정수가 양수이면서 홀수이면
elif num > 0 and num % 2 != 0:
    # D를 출력합니다.
    print("D")