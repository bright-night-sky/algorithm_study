# https://codeup.kr/problem.php?id=1174

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 0 ~ 23인 시, 0 ~ 59인 분을 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
hour, minute = map(int, stdin.readline().split())
# 입력한 시에 24를 더하고 60을 곱한 뒤, 입력한 분을 더해 분 단위로 맞춘 시간을 계산하고 변수에 저장합니다.
# 입력한 시에 24를 더한 이유는 입력한 시가 0, 분이 30 미만일 경우, if문 같은 금지 키워드를 사용하지 않고
# 23시 몇 분으로 되돌아가야하기 때문입니다.
time_sum = (hour + 24) * 60 + minute
# 분 단위의 총 시간에 30을 빼 30분 전의 시간을 구하고 변수에 저장합니다.
before_30_time = time_sum - 30
# 30분 전의 총 시간에서 60으로 나눈 몫을 구하고 그 값에 24로 나눈 나머지를 계산해 30분 전의 시 부분을 구하고 변수에 저장합니다.
before_30_hour = before_30_time // 60 % 24
# 30분 전의 총 시간에서 60으로 나눈 나머지를 구해 30분 전의 분 부분을 구하고 변수에 저장합니다.
before_30_minute = before_30_time % 60

# 30분 전의 시, 분을 공백으로 구분해 출력합니다.
print(before_30_hour, before_30_minute)