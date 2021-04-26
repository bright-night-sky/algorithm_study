# https://www.acmicpc.net/problem/15720

# 첫째 줄에는 주문한 버거의 개수 B,
# 사이드 메뉴의 개수 C, 음료의 개수 D를
# 공백을 사이에 두고 순서대로 입력합니다.
# 1 <= B, C, D <= 1,000
B, C, D = map(int, input().split(' '))

# 둘째 줄에는 각 버거의 가격을 공백을 사이에 두고 입력합니다.
# 정수형으로 바꾸고 리스트 변수에 넣어줍니다.
burgers = list(map(int, input().split(' ')))

# 셋째 줄에는 각 사이드 메뉴의 가격을 공백을 사이에 두고 입력합니다.
# 정수형으로 바꾸고 리스트 변수에 넣어줍니다.
sides = list(map(int, input().split(' ')))

# 넷째 줄에는 각 음료의 가격을 공백을 사이에 두고 입력합니다.
# 정수형으로 바꾸고 리스트 변수에 넣어줍니다.
drinks = list(map(int, input().split(' ')))

# 입력한 버거, 사이드 메뉴, 음료 중 가장 적은 개수를 저장하는 변수를 선언합니다.
min_num = min(B, C, D)

# 세트 할인이 적용되기 전 가격을 저장하는 변수를 선언합니다.
# 모든 버거, 사이드 메뉴, 음료의 가격을 더한 값입니다.
before_set_dicount = sum(burgers) + sum(sides) + sum(drinks)
# 세트 할인이 적용된 후 가격을 저장하는 변수를 선언합니다.
# 0으로 초기화해줍니다.
after_set_discount = 0

# 버거, 사이드 메뉴, 음료 중 가장 적은 개수만큼 반복해봅니다.
for i in range(min_num):
    # 버거 중 가장 비싼 가격을 저장하는 변수를 선언합니다.
    max_price_burger = max(burgers)
    # 사이드 메뉴 중 가장 비싼 가격을 저장하는 변수를 선언합니다.
    max_price_side = max(sides)
    # 음료 중 가장 비싼 가격을 저장하는 변수를 선언합니다.
    max_price_drink = max(drinks)

    # 위의 세 변수를 더하고 10%를 할인한 가격을 저장하는 변수를 선언합니다.
    set_price = int((max_price_burger + max_price_side + max_price_drink) * 0.9)
    # 이번에 할인된 세트 메뉴의 가격을 after_set_discount에 저장합니다.
    after_set_discount += set_price

    # 가장 비싼 버거, 사이드 메뉴, 음료는 할인이 되었으니 각 리스트 변수에서 제거해줍니다.
    burgers.remove(max_price_burger)
    sides.remove(max_price_side)
    drinks.remove(max_price_drink)

# 할인이 되지 않은 남은 버거, 사이드 메뉴, 음료들의 가격을 after_set_discount에 저장해줍니다.
after_set_discount += sum(burgers) + sum(sides) + sum(drinks)

# 세트 할인이 적용되기 전 가격을 출력합니다.
print(before_set_dicount)
# 세트 할인이 적용된 후 가격을 출력합니다.
print(after_set_discount)