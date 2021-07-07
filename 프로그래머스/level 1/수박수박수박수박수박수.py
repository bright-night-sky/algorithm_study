# https://programmers.co.kr/learn/courses/30/lessons/12922

# 길이 n이 매개변수로 주어집니다.
def solution(n):
    # 정답을 저장할 변수를 선언합니다.
    answer = ''

    # 길이 n만큼 반복합니다.
    for idx in range(n):
        # answer에 넣을 글자가 홀수 번째 글자라면
        if idx % 2 == 0:
            # answer에 수를 넣어줍니다.
            answer += '수'
        # answer에 넣을 글자가 짝수 번째 글자라면
        else:
            # answer에 박을 넣어줍니다.
            answer += '박'

    # answer에 저장된 수박수박... 패턴 문자열을 반환합니다.
    return answer