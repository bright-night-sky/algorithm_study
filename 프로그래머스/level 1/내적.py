# https://programmers.co.kr/learn/courses/30/lessons/70128

# 길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다.
def solution(a, b):
    # a, b의 내적의 결과를 저장할 변수를 선언합니다.
    answer = 0
    # a의 길이를 저장하는 변수를 선언합니다.
    length = len(a)

    # a의 길이만큼 반복합니다.
    for idx in range(length):
        # a, b에서 현재 인덱스의 값들을 곱하고 answer에 더해줍니다.
        answer += a[idx] * b[idx]

    # 내적의 결과인 answer를 반환합니다.
    return answer