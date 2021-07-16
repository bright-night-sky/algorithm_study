# https://programmers.co.kr/learn/courses/30/lessons/42889

# 전체 스테이지의 개수 N,
# 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 리스트 stages가 매개변수로 주어집니다.
def solution(N, stages):
    # 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호들을 저장할 리스트 변수를 선언합니다.
    answer = [None] * N
    # (스테이지 번호, 실패율) 튜플 정보를 저장할 리스트 변수를 선언합니다.
    all_stage_and_fail = [None] * N

    # 스테이지 번호 1부터 N까지 반복합니다.
    for stage_num in range(1, N + 1):
        # 현재 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수를 저장하는 변수를 선언합니다.
        on_stage_not_clear = len([i for i in stages if i == stage_num])
        # 현재 스테이지에 도달한 플레이어 수를 저장하는 변수를 선언합니다.
        on_stage = len([i for i in stages if i >= stage_num])

        # 현재 스테이지에 도달한 유저가 없는 경우
        if on_stage == 0:
            # 현재 스테이지의 실패율은 0입니다.
            fail = 0
        # 현재 스테이지에 도달한 유저가 있는 경우
        else:
            # 실패율의 정의에 따라 계산하고 저장한 변수를 선언합니다.
            # 실패율의 정의 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
            fail = on_stage_not_clear / on_stage

        # 현재 스테이지의 번호와 실패율 짝을 저장하는 튜플 변수를 선언합니다.
        stage_and_fail = (stage_num, fail)
        # all_stage_and_fail에 현재 스테이지의 번호, 실패율 짝 튜플을 넣어줍니다.
        all_stage_and_fail[stage_num - 1] = stage_and_fail

    # all_stage_and_fail의 값들을 실패율을 기준으로 내림차순 정렬합니다.
    all_stage_and_fail.sort(key=lambda stage: -stage[1])

    # 각 스테이지마다 반복합니다.
    for stage_num in range(N):
        # all_stage_and_fail에 있는 스테이지 정보의 순서대로 스테이지 번호를 answer에 넣어줍니다.
        answer[stage_num] = all_stage_and_fail[stage_num][0]

    # 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 리스트 answer의 값을 반환합니다.
    return answer