# https://www.acmicpc.net/problem/14720

# 첫째 줄에 우유 가게의 수 N을 입력합니다.
# 1 <= N <= 1000
N = int(input())

# 둘째 줄에는 우유 가게 정보를 우유 거리의 시작부터 끝까지 순서대로 N개의 정수로 입력합니다.
# 0 : 딸기 우유만 파는 가게
# 1 : 초코 우유만 파는 가게
# 2 : 바나나 우유만 파는 가게
# 0, 1, 2 외의 정수는 입력하지 않습니다.
milk_store = list(map(int, input().split(' ')))

# 영학이가 다음 차례에 마실 우유를 저장하는 변수입니다.
# 딸기 우유(0) -> 초코 우유(1) -> 바나나 우유(2) -> 딸기 우유(0) 차례입니다.
# 그래서 초기화는 0으로 해줍니다.
cur_milk = 0

# 영학이가 마실 수 있는 우유의 최대 개수를 저장하는 변수입니다.
max_milk = 0

# 우유 가게에서 우유를 마실 수 있는지 확인해봅니다.
for milk in milk_store:
    # 현재 마실 수 있는 우유와 가게에서 파는 우유가 일치한다면
    if milk == cur_milk:
        # 우유를 마시고 마실 수 있는 우유의 최대 개수에 1을 더합니다.
        max_milk += 1

        # 현재 마실 수 있는 우유가 바나나 우유(2)였다면
        if cur_milk == 2:
            # 다음 번은 딸기 우유를 마실 수 있으므로 0으로 바꿉니다.
            cur_milk = 0
        # 그 외의 경우면
        else:
            # 그냥 1을 더해서 다음 번에 마실 수 있는 우유로 변경합니다.
            cur_milk += 1

# 마실 수 있는 우유의 최대 개수를 출력합니다.
print(max_milk)