# https://programmers.co.kr/learn/courses/30/lessons/12911

# 자연수 n이 매개변수로 주어집니다.
# n은 1,000,000 이하의 자연수입니다.
def solution(n):
    # n을 2진수로 바꿨을 때, 1의 개수를 저장하는 변수를 선언합니다.
    bin_n_one_cnt = bin(n).count('1')

    # 다음 큰 숫자를 찾을 때까지 반복합니다.
    while True:
        # n에 1을 더합니다.
        n += 1

        # 현재 n을 2진수로 바꿨을 때의 1의 개수가
        # 처음 n을 2진수로 바꿨을 때의 1의 개수와 같다면
        if bin(n).count('1') == bin_n_one_cnt:
            # 현재 n을 반환합니다.
            return n