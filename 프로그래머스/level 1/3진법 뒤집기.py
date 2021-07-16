# https://programmers.co.kr/learn/courses/30/lessons/68935

# 자연수 n이 매개변수로 주어집니다.
# n은 1 이상 100,000,000 이하인 자연수입니다.
def solution(n):
    # 정답을 저장할 변수를 선언합니다.
    answer = ''

    # n이 3보다 크거나 같은 경우, 계속 반복합니다.
    while n >= 3:
        # n을 3으로 나누고 나온 나머지를 문자열로 변환하고 answer에 넣어줍니다.
        answer += str(n % 3)
        # n을 3으로 나눈 몫을 다시 n에 저장합니다.
        n //= 3

        # n이 3보다 작다면
        if n < 3:
            # n을 문자열로 변환하고 answer에 넣어줍니다.
            answer += str(n)
    # 이 반복문을 거치고 나면 answer에는 n을 3진수로 변환하고 뒤집은 상태의 값이 저장됩니다.

    # 매개변수로 주어진 n이 3보다 작아서 answer가 빈 문자열인 상태라면
    if answer == '':
        # answer에 n 그대로 문자열로 변환하고 저장합니다.
        answer = str(n)

    # 3진법 형태의 수를 문자열로 저장하고 있는 answer의 값을 3진법으로 10진법으로 변환합니다.
    answer = int(answer, base=3)

    # answer의 값을 반환합니다.
    return answer