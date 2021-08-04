# https://programmers.co.kr/learn/courses/30/lessons/82612

# 놀이기구의 처음 이용료 price, 처음 가지고 있던 금액 money,
# 놀이기구의 이용 횟수 count가 매개변수로 주어집니다.
def solution(price, money, count):
    # 놀이기구를 count번 타는데 필요한 금액을 저장하는 변수를 선언합니다.
    # 등차수열의 합을 이용해서 계산합니다.
    # 등차수열의 합 : n{2a + (n-1)d} / 2
    cost = count * (2 * price + (count - 1) * price) // 2

    # 놀이기구를 count번 타는데 필요한 금액에서
    # 현재 자신이 가지고 있는 금액만큼 얼마가 모자라는지를 저장한 변수를 선언하니다.
    lack_money = cost - money

    # 모자라지 않다면
    if lack_money < 0:
        # lack_money에 0을 저장합니다.
        lack_money = 0

    # 모자란 금액을 반환합니다.
    return lack_money