# https://programmers.co.kr/learn/courses/30/lessons/12934

# 양의 정수 n이 매개변수로 주어집니다.
# n은 1 이상, 50,000,000,000,000 이하인 양의 정수입니다.
def solution(n):
    # x+1의 제곱 혹은 -1을 저장할 변수를 선언합니다.
    answer = 0
    # 양의 정수 n의 제곱근을 저장하는 변수를 선언합니다.
    x = n ** 0.5

    # n의 제곱근 x가 .0으로 끝난다면
    if str(x)[-2:] == '.0':
        # x는 양의 정수이므로 x+1의 제곱을 answer에 저장합니다.
        answer = (x + 1) ** 2
    # n의 제곱근 x가 .0으로 끝나지 않는다면
    else:
        # x는 양의 정수가 아니므로 answer에 -1을 저장합니다.
        answer = -1

    # answer의 값을 반환합니다.
    return answer