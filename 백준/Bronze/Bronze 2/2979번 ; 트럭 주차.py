# https://www.acmicpc.net/problem/2979

# readline을 사용하기 위해서 import합니다.
from sys import stdin

# 첫째 줄에 주차 요금 A, B, C를 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
# 1 <= C <= B <= A <= 100
A, B, C = map(int, stdin.readline().split(' '))

# 각 트럭들이 주차장에 도착한 시간과 주차장에서 떠난 시간을 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환한 뒤, 리스트 변수에 넣어줍니다.
# 시간들은 1과 100 사이입니다.
truck1 = list(map(int, stdin.readline().split(' ')))
truck2 = list(map(int, stdin.readline().split(' ')))
truck3 = list(map(int, stdin.readline().split(' ')))

# 세 트럭 중 가장 마지막에 떠나는 시간을 저장하는 변수를 선언합니다.
last_time = max(truck1[1], truck2[1], truck3[1])

# 내야하는 주차 요금을 저장할 변수를 선언합니다.
parking_fee = 0

# 세 트럭 중 가장 마지막에 떠나는 시간만큼 1부터 반복합니다.
for time in range(1, last_time + 1):
    # 주차장에 있는 트럭의 개수를 저장할 변수를 선언합니다.
    truck_cnt = 0

    # 현재 시간에 첫 번째 트럭이 있다면
    if truck1[0] < time <= truck1[1]:
        # 트럭의 개수에 1을 더해줍니다.
        truck_cnt += 1
    # 현재 시간에 두 번째 트럭이 있다면
    if truck2[0] < time <= truck2[1]:
        # 트럭의 개수에 1을 더해줍니다.
        truck_cnt += 1
    # 현재 시간에 세 번째 트럭이 있다면
    if truck3[0] < time <= truck3[1]:
        # 트럭의 개수에 1을 더해줍니다.
        truck_cnt += 1

    # 주차장에 있는 트럭의 개수가 1대라면
    if truck_cnt == 1:
        # 최종 주차 요금에 A 요금 * 트럭 개수를 더해줍니다.
        parking_fee += A * truck_cnt
    # 주차장에 있는 트럭의 개수가 2대라면
    elif truck_cnt == 2:
        # 최종 주차 요금에 B 요금 * 트럭 개수를 더해줍니다.
        parking_fee += B * truck_cnt
    # 주차장에 있는 트럭의 개수가 3대라면
    elif truck_cnt == 3:
        # 최종 주차 요금에 C 요금 * 트럭 개수를 더해줍니다.
        parking_fee += C * truck_cnt

# 최종 주차 요금을 출력합니다.
print(parking_fee)