# https://programmers.co.kr/learn/courses/30/lessons/12910

# 자연수를 담은 배열 arr, 자연수인 divisor를 매개변수로 받습니다.
def solution(arr, divisor):
    # 정답들을 저장할 리스트 변수를 선언합니다.
    answer = []

    # arr에 있는 자연수들을 하나씩 반복합니다.
    for num in arr:
        # 현재 숫자가 divisor로 나누어 떨어진다면
        if num % divisor == 0:
            # answer에 현재 숫자를 넣어줍니다.
            answer.append(num)

    # answer가 빈 리스트라면
    if answer == []:
        # answer를 -1 하나가 담긴 리스트로 만들어줍니다.
        answer = [-1]
    # answer가 빈 리스트가 아니라면
    else:
        # answer의 값들을 오름차순으로 정렬합니다.
        answer.sort()

    # answer를 반환합니다.
    return answer