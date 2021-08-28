# https://codeup.kr/problem.php?id=1214

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 월별 마지지 막날을 저장한 리스트 변수 months_days를 선언합니다.
# 2월은 28일로 지정해줍니다.
months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 연도, 월을 공백으로 구분해 입력합니다.
# 각각 int형으로 변환합니다.
year, month = map(int, stdin.readline().split())

# 입력한 월이 2월이 아니라면
if month != 2:
    # 입력한 월에 해당하는 마지막 날을 months_days에서 찾아 출력합니다.
    print(months_days[month - 1])
# 입력한 월이 2월일 때
# 윤년에 해당하는 조건인
# 1. 400의 배수인 해이거나,
# 2. 4의 배수인 해들 중 100의 배수가 아닌 해라면
elif year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    # 윤년이므로 2월의 마지막 날인 28에 1을 더해 29를 출력합니다.
    print(months_days[1] + 1)
# 윤년이 아니라면
else:
    # 2월의 마지막 날을 출력합니다.
    print(months_days[1])