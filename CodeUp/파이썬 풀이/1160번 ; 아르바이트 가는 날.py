# https://codeup.kr/problem.php?id=1160

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 요일에 해당하는 번호를 입력합니다.
# 정수형으로 변환합니다.
weekday = int(stdin.readline())

# 입력한 요일의 번호가 월, 수, 금, 일인 홀수라면
if weekday % 2 == 1:
    # oh my god을 출력합니다.
    print('oh my god')
# 그 외에는
else:
    # enjoy를 출력합니다.
    print('enjoy')