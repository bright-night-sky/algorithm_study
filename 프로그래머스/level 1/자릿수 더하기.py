# https://programmers.co.kr/learn/courses/30/lessons/12931

# 자연수 n이 매개변수로 주어집니다.
def solution(n):
    # 자연수 n의 각 자릿수의 합을 저장하는 변수를 선언합니다.
    answer = sum(map(int, list(str(n))))

    # 자연수 n의 각 자릿수의 합을 반환합니다.
    return answer