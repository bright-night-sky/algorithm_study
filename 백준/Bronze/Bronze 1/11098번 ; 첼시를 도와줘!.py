# https://www.acmicpc.net/problem/11098

# 첫 번째 줄에는 테스트 케이스의 개수 n을 입력합니다.
# n <= 100
n = int(input())

# 테스트 케이스의 개수 n만큼 반복합니다.
for test_case in range(n):
    # 고려해야될 선수의 수 p를 입력합니다.
    # 1 <= p <= 100
    p = int(input())

    # 가장 비싼 선수의 가격을 저장하는 변수를 선언합니다.
    max_price = 0
    # 가장 비싼 선수의 이름을 저장하는 변수를 선언합니다.
    max_price_player = ''

    # 고려해야될 선수의 수 p만큼 반복합니다.
    for player in range(p):
        # 현재 선수의 가격과 이름을 공백으로 구분해 입력합니다.
        # 모든 선수의 가격은 다릅니다.
        # 가격은 2*10^9보다 작습니다.
        # 이름은 20자 이하이며, 사이에 공백은 없습니다.
        price, player_name = input().split(' ')

        # 현재 가장 비싼 선수의 가격보다 반복문에서의 현재 선수의 가격이 더 비싸다면
        if max_price < int(price):
            # 가장 비싼 선수의 가격 변수에 현재 선수의 가격을 저장합니다.
            max_price = int(price)
            # 가장 비싼 선수의 이름 변수에 현재 선수의 이름을 저장합니다.
            max_price_player = player_name

    # 가장 비싼 선수의 이름을 출력합니다.
    print(max_price_player)