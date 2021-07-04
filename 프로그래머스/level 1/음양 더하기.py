# https://programmers.co.kr/learn/courses/30/lessons/76501

# 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와
# 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다.
def solution(absolutes, signs):
    # 정답을 저장할 변수를 선언합니다.
    # 0으로 초기화합니다.
    answer = 0
    # 정수들의 개수를 저장하는 변수를 선언합니다.
    num_len = len(absolutes)

    # 정수 하나마다 반복해봅니다.
    for idx in range(num_len):
        # 현재 정수의 signs가 true라면
        if signs[idx]:
            # answer에 현재 정수를 더해줍니다.
            answer += absolutes[idx]
        # 현재 정수의 signs가 false라면
        else:
            # answer에 현재 정수를 빼줍니다.
            answer -= absolutes[idx]

    # 정답을 반환합니다.
    return answer