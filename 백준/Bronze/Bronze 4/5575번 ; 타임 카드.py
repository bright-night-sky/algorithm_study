# https://www.acmicpc.net/problem/5575

# readline을 사용하기 위해 import합니다.
from sys import stdin


# A, B, C 세 사람이므로 3번 반복합니다.
for _ in range(3):
    # 이번 사람의 출근 시간과 퇴근 시간을 공백으로 구분해 입력합니다.
    # 7 <= h <= 22
    # 0 <= m <= 59
    # 0 <= s <= 59
    # 각각 정수형으로 변환하고 리스트 변수에 넣어줍니다.
    person_time = list(map(int, stdin.readline().split(' ')))

    # 퇴근 시간의 초에서 출근 시간의 초를 빼준 값을 저장하는 변수를 선언합니다.
    s = person_time[5] - person_time[2]
    # s가 0보다 작은 음수라면
    if s < 0:
        # s에 60을 더해줍니다.
        s += 60
        # 퇴근 시간의 분에 1을 빼줍니다.
        person_time[4] -= 1

    # 퇴근 시간의 분에서 출근 시간의 분을 빼준 값을 저장하는 변수를 선언합니다.
    m = person_time[4] - person_time[1]
    # m이 0보다 작은 음수라면
    if m < 0:
        # m에 60을 더해줍니다.
        m += 60
        # 퇴근 시간의 시에 1을 빼줍니다.
        person_time[3] -= 1

    # 퇴근 시간의 시에서 출근 시간의 시를 빼준 값을 저장하는 변수를 선언합니다.
    h = person_time[3] - person_time[0]

    # 근무 시간의 시, 분, 초를 공백으로 구분해 출력합니다.
    print(h, m, s)


