# https://www.acmicpc.net/problem/2884

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 알람 시간 H시, M분인 두 정수를 공백으로 구분해 입력합니다.
# 0 <= H <= 23
# 0 <= M <= 59
# 각각 정수형으로 변환합니다.
H, M = map(int, stdin.readline().split(' '))
# 분에서 45분을 뺍니다.
M -= 45

# 분이 0보다 작다면
if M < 0:
    # 시에서 1을 뺍니다.
    H -= 1
    # 분에 60을 더합니다.
    M += 60

# 시가 0보다 작다면
if H < 0:
    # 시에 24를 더합니다.
    H += 24

# 45분 앞선 알람 시간을 출력 형식에 맞게 출력합니다.
print(H, M)