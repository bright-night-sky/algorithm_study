# https://programmers.co.kr/learn/courses/30/lessons/77884

# 두 정수 left, right가 매개변수로 주어집니다.
# 1 <= left <= right <= 1,000
def solution(left, right):
    # 정답을 저장할 변수를 선언합니다.
    answer = 0

    # left부터 right까지 반복해봅니다.
    for num in range(left, right + 1):
        # 현재 숫자의 제곱근이 정수로 딱 나누어 떨어진다면
        if str(num ** 0.5)[-2:] == '.0':
            # 현재 숫자의 약수의 개수는 홀수이므로 answer에 현재 숫자를 빼줍니다.
            answer -= num
        # 현재 숫자의 제곱근이 정수로 딱 나누어 떨어지지 않는다면
        else:
            # 현재 숫자의 약수의 개수는 짝수이므로 answer에 현재 숫자를 더해줍니다.
            answer += num

    # answer의 값을 반환합니다.
    return answer