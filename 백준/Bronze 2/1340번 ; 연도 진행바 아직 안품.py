# https://www.acmicpc.net/problem/1340

# 각 달의 일수
month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 오늘 날짜, 시간 입력
# 항상 올바른 날짜와 시간만 입력으로 주어진다.
today = input()

# 입력 변수를 파싱해준다.
# Month DD, YYYY HH:MM 입력
# Month : 현재 월 영문
# YYYY : 현재 연도 숫자 네 자리 : 1800 <= YYYY <= 2600
# DD, HH, MM : 모두 2자리 숫자, 현재 일, 시, 분
Month = today.split(' ')[0]
day = int(today.split(' ')[:-1])
YYYY = int(today.split(' ')[2])
HH = today.split(' ')[3].split(':')[0]
MM = today.split(' ')[3].split(':')[1]

# 현재 날짜까지의 일수를 저장하는 변수
# 입력받은 일수 - 1로 초기화한다.
# 왜냐하면 해당 일수의 24시간이 지나가야 입력받은 날짜까지 일수가 포함되기 때문이다.
days_count = day - 1
# 해당 년도의 전체 일수에 대한 현재 날짜까지 비율을 저장하는 변수
days_ration = 0
# 하루 시간의 비율을 저장하는 변수
time_ration = 0
# 날짜의 비율과 시간의 비율을 곱하면 이번 해의 진행율을 알 수 있다.

# 입력한 연도의 총 일수를 저장하는 변수
cur_year_days = 365
# 윤년이 아니면 365일, 윤년이면 366일이다.
# 윤년은 그 해가 400으로 나누어 떨어지는 해 이거나, 4로 나누어 떨어지면서, 100으로 나누어 떨어지지 않는 해 일때이다.
if YYYY % 400 == 0 or (YYYY % 4 == 0 and YYYY % 100 != 0):
    # 조건문을 만족하면 윤년이므로 총 일수를 366으로 저장
    cur_year_days = 366

for day in month_day:
