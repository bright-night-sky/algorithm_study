# https://www.acmicpc.net/problem/5176

# 첫째 줄에 테스트 케이스의 개수 K를 입력합니다.
K = int(input())

# 테스트 케이스의 개수 K만큼 반복합니다.
for i in range(K):
    # 첫째 줄에 참가자의 수 P, 자리의 수 M을 입력합니다.
    # 1 <= P, M <= 500
    P, M = map(int, input().split(' '))

    # 자리의 수 M만큼 True의 값을 가진 자리 리스트 변수를 선언합니다.
    # True이면 참가자가 앉을 수 있는 자리입니다.
    positions = [True for position in range(M)]

    # 원하는 자리에 이미 다른 참가자가 앉아버려 참가하지 못하는 인원의 수를 저장하는 변수를 선언합니다.
    cant_participants = 0

    # 참가자의 수 P만큼 반복합니다.
    for j in range(P):
        # 이번 참가자가 원하는 자리를 입력합니다.
        participant_want_position = int(input())

        # 이번 참가자가 원하는 자리에 아직 아무도 앉지 않았다면
        if positions[participant_want_position - 1] == True:
            # 그 자리에는 이번 참가자가 앉았으니 다른 참가자는 못 앉으므로 False로 값을 변경해줍니다.
            positions[participant_want_position - 1] = False
        # 이번 참가자가 원하는 자리에 이미 누가 앉았다면
        else:
            # 참가하지 못하는 인원의 수에 1을 더해줍니다.
            cant_participants += 1

    # 대회에 참가하지 못하는 사람의 수를 출력합니다.
    print(cant_participants)