# https://www.acmicpc.net/problem/14606

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫 번째 줄에 피자판의 개수인 양의 정수 N을 입력합니다.
# 1 <= N <= 10
# 정수로 변환합니다.
N = int(stdin.readline())
# 즐거움의 총합을 구하면서 생기는 피자탑들을 저장하는 리스트 변수를 선언합니다.
pizza_towers = []
# 즐거움의 총합의 최댓값을 저장할 변수를 선언합니다.
joy = 0

# 처음 피자판의 개수가 1 이상이면
if N > 1:
    # 피자탑 리스트 변수에 N을 넣어줍니다.
    pizza_towers = [N]

# 피자탑 리스트 변수가 비어질 때까지 반복합니다.
while True:
    # 피자탑 리스트 변수가 비어있다면
    if pizza_towers == []:
        # 즐거움의 총합을 출력합니다.
        print(joy)
        # 반복문을 탈출합니다.
        break
    # 피자탑 리스트 변수가 비어있지 않다면
    else:
        # 피자탑 리스트 변수의 맨 끝에서 피자탑을 하나 빼내어 변수에 저장합니다.
        pizza_tower = pizza_towers.pop()
        # 빼낸 피자탑의 절반을 한 부분으로 변수에 저장합니다.
        pizza_tower_part1 = pizza_tower // 2
        # 나머지 절반을 변수에 저장합니다.
        pizza_tower_part2 = pizza_tower - pizza_tower_part1
        # 두 절반의 곱을 즐거움의 총합에 더해줍니다.
        joy += pizza_tower_part1 * pizza_tower_part2

        # 빼낸 피자탑에서 구한 처음의 절반의 결과가 1이 아니라면
        if pizza_tower_part1 != 1:
            # 피자탑 리스트 변수에 그 절반의 값을 넣어줍니다.
            pizza_towers.append(pizza_tower_part1)

        # 빼낸 피자탑에서 구한 두 번째 절반의 결과가 1이 아니라면
        if pizza_tower_part2 != 1:
            # 피자탑 리스트 변수에 그 절반의 값을 넣어줍니다.
            pizza_towers.append(pizza_tower_part2)