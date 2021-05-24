# https://www.acmicpc.net/problem/2875

# readline을 사용하기 위해서 import합니다.
from sys import stdin

# 첫째 줄에 N, M, K를 공백으로 구분해 입력합니다.
# 0 <= N <= 100
# 0 <= M <= 100
# 0 <= K <= M+N
# 각각 정수형으로 변환해줍니다.
N, M, K = map(int, stdin.readline().split(' '))

# 여학생 중 인턴쉽 프로그램에 참가해야하는 수를 저장하는 변수를 선언합니다.
# 처음에는 K로 초기화해줍니다.
woman_internship = K
# 남학생 중 인턴쉽 프로그램에 참가해야하는 수를 저장하는 변수를 선언합니다.
# 처음에는 0으로 초기화해줍니다.
man_internship = 0
# 대회에 참가하기 위해 만들 수 있는 최대의 팀의 개수를 저장하는 변수를 선언합니다.
team_cnt = 0

# K만큼 반복해봅니다.
for _ in range(K + 1):
    # 여학생 중 대회에 참가할 수 있는 수를 저장하는 변수를 선언합니다.
    woman_competition = N - woman_internship
    # 남학생 중 대회에 참가할 수 있는 수를 저장하는 변수를 선언합니다.
    man_competition = M - man_internship

    # 여학생은 2명의 여학생이 묶여서 팀으로 구성되므로 2로 나누어 한 팀이 될 수 있는 수를 저장하는 변수를 선언합니다.
    woman_can_team = woman_competition // 2

    # 남학생 중 대회에 참가할 수 있는 수가
    # 여학생의 팀의 개수보다 작고, 현재 팀의 개수보다 크거나 같다면
    if woman_can_team > man_competition >= team_cnt:
        # 팀의 개수에 남학생 중 대회에 참가할 수 있는 수로 초기화해줍니다.
        team_cnt = man_competition
    # 여학생 중 대회에 참가할 수 있는 여학생 2명 묶음의 수가
    # 남학생 중 대회에 참가할 수 있는 수보다 작거나 같고, 현재 팀의 개수보다 크거나 같다면
    elif man_competition >= woman_can_team >= team_cnt:
        # 팀의 개수에 여학생 중 대회에 참가할 수 있는 여학생 2명 묶음의 수로 초기화해줍니다.
        team_cnt = woman_can_team

    # 여학생 중 인턴쉽 프로그램에 참가하는 학생의 수에 1을 뺍니다.
    woman_internship -= 1
    # 남학생 중 인턴쉽 프로그램에 참가하는 학생의 수에 1을 더합니다.
    man_internship += 1

# 대회에 참가할 수 있는 최대 팀의 개수를 출력합니다.
print(team_cnt)