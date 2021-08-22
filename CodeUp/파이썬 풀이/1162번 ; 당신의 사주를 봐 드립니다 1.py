# https://codeup.kr/problem.php?id=1162

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 년, 월, 일을 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
year, month, day = map(int, stdin.readline().split())
# (년 - 월 + 일)의 마지막 숫자를 저장하는 변수를 선언합니다.
fate = (year - month + day) % 10

# 사주의 마지막 숫자가 0이라면
if fate == 0:
    # 대박을 출력합니다.
    print('대박')
# 그렇지 않으면
else:
    # 그럭저럭을 출력합니다.
    print('그럭저럭')