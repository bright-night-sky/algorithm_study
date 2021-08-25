# https://codeup.kr/problem.php?id=1173

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 시와 분을 공백으로 구분해 입력합니다.
# 시의 범위 : 0 ~ 23
# 분의 범위 : 0 ~ 59
# 각각 정수형으로 변환합니다.
hour, minute = map(int, stdin.readline().split())
# 입력한 시에 60을 곱하고 분에 더해 분 단위의 시간으로 변경하고 변수에 저장합니다.
time_sum = hour * 60 + minute
# 분 단위 시간에서 30분을 빼서 30분전의 시간을 구하고 변수에 저장합니다.
before_30_time = time_sum - 30
# 30분전의 시간에 60을 나눈 후의 몫인 30분전 시간의 시 부분을 구하고 변수에 저장합니다.
before_30_hour = before_30_time // 60
# 30분전의 시간에 60을 나눈 후의 나머지인 30분전 시간의 분 부분을 구하고 변수에 저장합니다.
before_30_minute = before_30_time % 60

# 30분전 시간의 시가 음수라면
if before_30_hour < 0:
    # 음수인 시 부분에 24를 더해 24시간 기준으로 맞춰줍니다.
    before_30_hour += 24

# 30분 전의 시간의 시와 분을 공백으로 구분해 출력합니다.
print(before_30_hour, before_30_minute)