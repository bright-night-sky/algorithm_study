# https://programmers.co.kr/learn/courses/30/lessons/12943

# 1 이상 8,000,000 미만인 정수 num이 매개변수로 주어집니다.
def solution(num):
    # 정답을 저장할 변수를 선언합니다.
    # 0으로 초기화합니다.
    answer = 0

    # 정답을 찾을 때까지 계속 반복해봅니다.
    while True:
        # num이 1이 된다면
        if num == 1:
            # 반복문을 탈출합니다.
            break
        # answer가 500이고 num이 1이 아니라면
        elif answer == 500 and num != 1:
            # answer에 -1을 저장합니다.
            answer = -1
            # 반복문을 탈출합니다.
            break

        # num이 짝수라면
        if num % 2 == 0:
            # num을 2로 나누고 그 값을 다시 num에 저장합니다.
            num //= 2
        # num이 홀수라면
        elif num % 2 == 1:
            # num에 3을 곱하고 1을 더한 값을 다시 num에 저장합니다.
            num = num * 3 + 1

        # 한 과정이 끝나면 answer에 1을 더합니다.
        answer += 1

    # -1 혹은 과정을 반복한 횟수가 들어있는 answer의 값을 반환합니다.
    return answer