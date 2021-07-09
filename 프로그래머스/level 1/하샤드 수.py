# https://programmers.co.kr/learn/courses/30/lessons/12947

# 양의 정수 x가 매개변수로 주어집니다.
def solution(x):
    # 양의 정수 x가 하샤드 수인지 아닌지를 저장하는 변수를 선언합니다.
    # 처음에는 x가 하샤드 수가 맞다는 뜻인 True로 초기화합니다.
    answer = True
    # x의 자릿수의 합을 저장하는 변수를 선언합니다.
    position_sum = sum(map(int, list(str(x))))

    # x가 x의 자릿수의 합으로 나누어지지 않는다면
    if x % position_sum != 0:
        # x는 하샤드 수가 아니므로 answer에 False를 저장합니다.
        answer = False

    # x가 하샤드 수인지 아닌지가 저장되어 있는 answer의 값을 반환합니다.
    return answer