# https://codeup.kr/problem.php?id=1166

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 해(year)를 입력합니다.
# 정수형으로 변환합니다.
year = int(stdin.readline())

# 윤년의 판단 조건을 조건문으로 만들어봅니다.
# 1. 해(year)가 4의 배수이면서 100의 배수가 아닌 경우
# 2. 400의 배수인 경우
# 위의 두 조건 중 하나라도 맞다면
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    # 입력한 해는 윤년이므로 'yes'를 출력합니다.
    print('yes')
# 그 외의 경우에는
else:
    # 윤년이 아니므로 'no'를 출력합니다.
    print('no')