# https://www.acmicpc.net/problem/2720

# 첫째 줄에 테스트 케이스의 개수 T를 입력합니다.
T = int(input())

# 테스트 케이스의 개수만큼 실행합니다.
for i in range(0, T):
    # 거스름돈 C를 입력합니다.
    # 정수 하나이고, 단위는 센트입니다. (1달러 = 100센트)
    # 1 <= C <= 500
    C = int(input())

    # 쿼터의 개수, 다임의 개수, 니켈의 개수, 페니의 개수를 저장하는 변수입니다.
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0

    # 손님이 받는 동전의 개수를 최소로 하려면
    # 쿼터부터 페니까지 더 큰 동전으로 나누어 주면 된다.

    # 거스름돈에서 쿼터를 얼마나 줘야할지 계산합니다.
    quarter = C // 25
    # 쿼터로 주고난 나머지 거스름돈을 변수에 저장합니다.
    C = C - quarter * 25

    # 거스름돈에서 다임을 얼마나 줘야할지 계산합니다.
    dime = C // 10
    # 다임으로 주고난 나머지 거스름돈을 변수에 저장합니다.
    C = C - dime * 10

    # 거스름돈에서 니켈을 얼마나 줘야할지 계산합니다.
    nickel = C // 5
    # 니켈로 주고난 나머지 거스름돈을 변수에 저장합니다.
    C = C - nickel * 5

    # 나머지 거스름돈은 모두 페니로 줘야하므로 남은 거스름돈은 그대로 페니의 개수입니다.
    penny = C

    # 쿼터의 개수, 다임의 개수, 니켈의 개수, 페니의 개수를 공백으로 구분하여 출력합니다.
    print(quarter, dime, nickel, penny)