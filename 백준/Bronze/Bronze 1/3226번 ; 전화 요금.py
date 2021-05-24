# https://www.acmicpc.net/problem/3226

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 상근이가 건 전화의 수 N을 입력합니다.
# 1 <= N <= 100
# 정수형으로 변환합니다.
N = int(stdin.readline())

# 총 전화 요금을 저장할 변수를 선언합니다.
call_cost = 0

# 전화의 수 N만큼 반복합니다.
for call_idx in range(N):
    # 전화를 건 시간 HH:MM, 통화 시간 DD를 공백으로 구분해 입력합니다.
    # DD는 최대 60입니다.
    start_time, DD = stdin.readline().rstrip().split(' ')
    # 통화 시간 DD는 정수형으로 변환합니다.
    DD = int(DD)
    # 통화 시간을 :로 구분해 시 HH, 분 MM으로 분리해줍니다.
    # 각각 정수형으로 변환합니다.
    HH, MM = map(int, start_time.split(':'))
    # 전화가 끝나는 시간의 시를 저장하는 변수를 선언합니다.
    # HH로 초기화해줍니다.
    end_hour = HH
    # 전화가 끝나는 시간의 분을 저장하는 변수를 선언합니다.
    # MM에 DD를 더한 값으로 초기화해줍니다.
    end_minute = MM + DD

    # 전화가 끝나는 시간의 분이 60분 이상이라면
    if end_minute >= 60:
        # 전화가 끝나는 시간의 시에 1을 더해줍니다.
        end_hour += 1
        # 전화가 끝나는 시간의 분에 60을 빼줍니다.
        end_minute -= 60

    # 전화가 끝나는 시간의 시가 24시 이상이라면
    if end_hour >= 24:
        # 전화가 끝나는 시간에 24를 빼줍니다.
        end_hour -= 24

    # 전화를 건 시간의 시 HH와 전화가 끝나는 시간의 시가 모두 7시에서 18시 이내라면
    if 7 <= HH <= 18 and 7 <= end_hour <= 18:
        # 1분에 10원을 곱한 값을 총 전화 요금에 더해줍니다.
        call_cost += DD * 10
    # 전화를 건 시간의 시 HH와 전화가 끝나는 시간의 시가 모두 19시에서 7시 이내라면
    elif (0 <= HH <= 6 or 19 <= HH <= 23) and (0 <= end_hour <= 6 or 19 <= end_hour <= 23):
        # 1분에 5원을 곱한 값을 총 전화 요금에 더해줍니다.
        call_cost += DD * 5
    # 전화를 건 시간의 시가 18시인데 전화가 끝나는 시간의 시가 19시라면
    elif HH == 18 and end_hour == 19:
        # 1분에 10원인 구간과 1분에 5원인 구간을 구분해서 총 전화 요금에 더해줍니다.
        call_cost += 10 * (60 - MM) + 5 * end_minute
    # 전화를 건 시간의 시가 6시인데 전화가 끝나는 시간의 시가 7시라면
    elif HH == 6 and end_hour == 7:
        # 1분에 10원인 구간과 1분에 5원인 구간을 구분해서 총 전화 요금에 더해줍니다.
        call_cost += 5 * (60 - MM) + 10 * end_minute

# 총 전화 요금을 출력합니다.
print(call_cost)