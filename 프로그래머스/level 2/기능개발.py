# https://programmers.co.kr/learn/courses/30/lessons/42586

# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 리스트 pregresses,
# 각 작업의 개발 속도가 적힌 정수 리스트 speeds가 매개변수로 주어집니다.
def solution(progresses, speeds):
    # 각 배포마다 배포되는 기능의 개수를 저장할 리스트 변수를 선언합니다.
    answer = []
    # 기능의 개수를 저장하는 변수를 선언합니다.
    progresses_len = len(progresses)
    # 가장 최근에 배포되었을 때까지 걸린 작업 일수를 저장할 변수를 선언합니다.
    prev_work_day = None

    # 기능 하나마다 반복해봅니다.
    for idx in range(progresses_len):
        # 현재 기능의 작업의 진도를 저장하는 변수를 선언합니다.
        progress = progresses[idx]
        # 현재 기능의 개발 속도를 저장하는 변수를 선언합니다.
        speed = speeds[idx]
        # 현재 기능을 개발하는데 걸리는 작업 일수를 저장하는 변수를 선언합니다.
        work_day = (100 - progress) // speed

        # 만약 남은 진도를 개발 속도로 나누었을 때 나머지가 0이 아니라면
        if (100 - progress) % speed != 0:
            # 작업 일수에 1을 더해줍니다.
            work_day += 1

        # 아직 배포된 기능이 없다면
        if prev_work_day == None:
            # prev_work_day에 work_day의 값을 넣어줍니다.
            prev_work_day = work_day
            # answer에 1을 넣어줍니다.
            answer.append(1)
        # 현재 기능의 작업 일수가 prev_work_day보다 작거나 같다면
        elif work_day <= prev_work_day:
            # 현재 기능은 가장 최근에 배포한 기능을 배포할 때 같이 배포하므로
            # answer의 가장 끝 값에 1을 더해줍니다.
            answer[-1] += 1
        # 현재 기능의 작업 일수가 prev_work_day보다 크다면
        elif work_day > prev_work_day:
            # 가장 최근에 배포한 기능을 배포한 이후에 배포할 수 있으므로
            # answer에 1을 넣어줍니다.
            answer.append(1)
            # prev_work_day에 work_day의 값을 넣어줍니다.
            prev_work_day = work_day

    # 각 배포마다 배포된 기능의 개수를 저장한 리스트를 반환합니다.
    return answer