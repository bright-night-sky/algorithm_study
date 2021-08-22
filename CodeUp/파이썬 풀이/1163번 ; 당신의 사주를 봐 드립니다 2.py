# https://codeup.kr/problem.php?id=1163

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 년도, 월, 일을 의미하는 세 정수를 공백으로 구분해 입력합니다.
year, month, day = map(int, stdin.readline().split())
# (년도 + 월 + 일)의 백의 자리 숫자를 저장하는 변수를 선언합니다.
fate = (year + month + day) % 1000 // 100

# (년도 + 월 + 일)의 백의 자리 숫자가 짝수이면
if fate % 2 == 0:
    # "대박"을 출력합니다.
    print('대박')
# 그렇지 않으면
else:
    # "그럭저럭"을 출력합니다.
    print('그럭저럭')