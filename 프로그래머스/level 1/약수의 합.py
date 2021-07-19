# https://programmers.co.kr/learn/courses/30/lessons/12928

# 정수 n이 매개변수로 주어집니다.
# n은 0 이상 3,000 이하인 정수입니다.
def solution(n):
    # n의 약수를 모두 더한 값을 저장할 변수를 선언합니다.
    answer = 0
    # 1부터 n의 제곱근까지 반복할 것이므로
    # n의 제곱근보다 작거나 같은 정수를 저장하는 변수를 선언합니다.
    limit = int(n ** 0.5)

    # 1부터 limit까지 반복합니다.
    for divisor in range(1, limit + 1):
        # n이 현재 숫자로 나누어진다면
        if n % divisor == 0:
            # answer에 현재 숫자를 더해줍니다.
            answer += divisor
            # n을 현재 숫자로 나눈 몫을 answer에 더해줍니다.
            answer += n // divisor

    # 16의 제곱근은 4인 경우처럼
    # n의 제곱근이 정수 형태로 딱 맞게 나오는 경우에는
    if n ** 0.5 == float(limit):
        # 위의 반복문에서 제곱근인 약수를 중복해서 더해줬으므로
        # answer에서 limit를 빼줍니다.
        answer -= limit

    # n의 약수를 모두 더한 값을 반환합니다.
    return answer