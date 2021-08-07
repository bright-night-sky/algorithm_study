# https://codeup.kr/problem.php?id=6091

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 인원 3명의 방문 주기를 공백을 두고 입력합니다.
# 각각 정수형으로 변환합니다.
cycle1, cycle2, cycle3 = map(int, stdin.readline().split())
# 3명이 다시 모두 함께 방문해 문제를 풀어보는 날을 저장할 변수를 선언합니다.
# 1일부터 차례로 증가시킬 것이므로 1부터 시작합니다.
day = 1

# 계속 반복하는 반복문을 선언합니다.
while True:
    # day에 저장된 현재 날짜에 인원 3명이 모두 방문한 날이라면,
    # 즉, day의 값을 각 인원의 방문 주기로 나누었을 때 나머지가 모두 0이라면
    if day % cycle1 == 0 and day % cycle2 == 0 and day % cycle3 == 0:
        # 3명이 다시 모두 함께 방문하는 날이므로 day의 값을 출력합니다.
        print(day)
        # 반복문을 탈출합니다.
        break

    # 3명이 모두 함께 방문하는 날이 아니면 다음 날을 생각해야함로 day에 1을 더합니다.
    day += 1