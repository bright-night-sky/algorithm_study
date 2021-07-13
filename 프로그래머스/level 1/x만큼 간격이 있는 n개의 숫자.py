# https://programmers.co.kr/learn/courses/30/lessons/12954

# 정수 x, 자연수 n이 매개변수로 주어집니다.
# x는 -10,000,000 이상, 10,000,000 이하인 정수입니다.
# n은 1,000 이하인 자연수입니다.
def solution(x, n):
    # 정답을 저장할 리스트 변수를 선언합니다.
    # n개의 None으로 초기화합니다.
    answer = [None] * n

    # 0부터 n-1까지 반복해봅니다.
    for idx in range(n):
        # answer의 현재 인덱스에 x * (idx+1) 값을 저장해줍니다.
        answer[idx] = x * (idx + 1)

    # answer의 값을 반환합니다.
    return answer