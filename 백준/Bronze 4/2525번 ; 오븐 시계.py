# https://www.acmicpc.net/problem/2525

# 첫째 줄에는 현재 시각을 입력
# 시 A : 0 <= A <= 23
# 분 B : 0 <= B <= 50
A, B = map(int, input().split(' '))

# 두 번째 줄에는 요리하는데 필요한 시간 C 입력
# 분 단위이다.
# 0 <= C <= 1,000
C = int(input())

# 입력 받은 요리하는 데 필요한 시간 C 분이 1시간 이상인 경우도 있으므로 시와 분으로 나누어준다.
plus_hour = C // 60
plus_minute = C % 60

# 결과를 표시할 시와 분
result_hour = A + plus_hour
result_minute = B + plus_minute

# 요리하는 데 필요한 시간을 현재 시각에 더했을 때 분이 60분을 넘으면 시에 1시간을 더해주고, 분에는 60을 빼준다.
if result_minute >= 60:
    result_hour += 1
    result_minute -= 60

# 디지털 시계는 23시 59분에서 1분이 지나면 0시 0분이 되는 것을 처리
if result_hour >= 24:
    result_hour -= 24

# 결과 출력
print(result_hour, result_minute)