# https://programmers.co.kr/learn/courses/30/lessons/12932

# 자연수 n이 매개변수로 주어집니다.
def solution(n):
    # n을 문자열로 바꾸고 각 문자들을 원소로 가지는 리스트로 만들어줍니다.
    # 각 원소를 정수형으로 변환하고 리스트로 만들어준 뒤 뒤집어줍니다.
    # 최종적으로 다시 리스트로 만들어줍니다.
    answer = list(reversed(list(map(int, list(str(n))))))

    # 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 리스트 answer를 반환합니다.
    return answer