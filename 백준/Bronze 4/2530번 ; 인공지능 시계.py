# https://www.acmicpc.net/problem/2530

# 현재 시각 시 A, 분 B, 초 C 입력
# 0 <= A <= 23
# 0 <= B <= 59
# 0 <= C <= 59
A, B, C = map(int, input().split(' '))

# 요리하는데 필요한 시간 D : 초 단위 입력
# 0 <= D <= 500,000
D = int(input())

# 요리하는 데 필요한 시간은 초 단위로 입력 받으므로 이것을 시, 분, 초 단위로 쪼개준다.
plus_hour = D // 3600
D = D - plus_hour * 3600
plus_minute = D // 60
plus_second = D % 60

# 결과를 표시할 시, 분, 초
result_hour = A + plus_hour
result_minute = B + plus_minute
result_second = C + plus_second

# 요리하는 데 필요한 시간을 더해주고 난 뒤 초가 60초를 넘은 경우
if result_second >= 60:
    # 결과의 분에 1분을 더해주고
    result_minute += 1
    # 결과의 초에는 60초를 빼준다.
    result_second -= 60

# 요리하는 데 필요한 시간을 더해주고 난 뒤 분이 60분을 넘은 경우
if result_minute >= 60:
    # 결과의 시에 1시간을 더해주고
    result_hour += 1
    # 결과의 분에는 60분을 빼준다.
    result_minute -= 60

# 요리하는 데 필요한 시간을 더해주고 난 뒤 시가 24시를 넘은 경우
if result_hour >= 24:
    # 23시 뒤에는 0시가 되므로 결과의 시에 24를 빼준다.
    result_hour -= 24

# 결과 출력
print(result_hour, result_minute, result_second)
