# https://www.acmicpc.net/problem/3566

# 올림 함수 math.ceil을 사용하기 위해 math 모듈을 import 해둡니다.
import math

# 첫째 줄에 대형 모니터의 가로 세로 해상도, 가로 세로 크기 rh, rv, sh, sv를 입력합니다.
# r : resolution(해상도)
# s : size(크기)
# h : horizontal(가로)
# v : vertical(세로)
# 100 <= rh, rv, sh, sv <= 10,000
rh, rv, sh, sv = map(int, input().split(' '))

# 상근이가 가지고 있는 모니터 종류의 개수 n을 입력합니다.
# 1 <= n <= 100
n = int(input())

# 가장 저렴한 가격을 저장할 변수입니다.
# 일단 -1로 초기화해줍니다.
min_price = -1

# 각 모니터 종류의 정보를 입력하고 대형 모니터를 만들 때의 비용을 계산해봅니다.
for i in range(0, n):
    # 가로 세로 해상도, 가로 세로 크기, 가격인 rhi, rvi, shi, svi, pi를 입력합니다.
    # 100 <= rhi, rvi, shi, svi, pi <= 10,000
    rhi, rvi, shi, svi, pi = map(int, input().split(' '))

    # 현재 고른 모니터로 대형 모니터를 만들 때 가로로 필요한 개수를 저장하는 변수입니다.
    required_h = 0
    # 현재 고른 모니터로 대형 모니터를 만들 때 세로로 필요한 개수를 저장하는 변수입니다.
    required_v = 0
    # 현재 고른 모니터로 대형 모니터를 만들 때 총 필요한 모니터의 개수를 저장하는 변수입니다.
    required_total = 0

    # 문제에서 모니터를 회전시켜서 대형 모니터를 만들 수 있다고 했습니다.
    # 그래서 현재 고른 모니터를 가로로 더 긴 상태로 대형 모니터를 구성할 때와
    # 세로로 더 긴 상태로 대형 모니터를 구성할 때로 나누어서 계산해봅니다.

    # 처음에는 현재 모니터를 입력받은대로 대형 모니터를 구성하는데 필요한 모니터의 개수를 구해보고
    # 그 다음에는 현재 모니터의 가로와 세로의 정보를 반대로 해서 대형 모니터를 구성하는데 필요한 모니터의 개수를 구해봅니다.
    # 그리고 그 둘의 필요한 모니터의 개수 중 더 작은 개수로 가격을 계산하면
    # 현재 모니터로 대형 모니터를 만드는데 필요한 가장 저렴한 가격입니다.
    # 그리고 그 가격을 다른 모니터들과 비교해보면 됩니다.

    # 가로로 해상도를 고려할 때 필요한 모니터의 개수를 저장하는 변수입니다.
    required_rh = math.ceil(rh / rhi)
    # 가로로 크기를 고려할 때 필요한 모니터의 개수를 저장하는 변수입니다.
    required_sh = math.ceil(sh / shi)
    # 세로로 해상도를 고려할 때 필요한 모니터의 개수를 저장하는 변수입니다.
    required_rv = math.ceil(rv / rvi)
    # 세로로 크기를 고려할 때 필요한 모니터의 개수를 저장하는 변수입니다.
    required_sv = math.ceil(sv / svi)

    # 가로로 필요한 모니터의 개수에서 해상도와 크기를 고려할 때 필요한 개수가 더 많은 것을 선택해야 합니다.
    required_h = max(required_rh, required_sh)
    # 세로로 필요한 모니터의 개수에서 해상도와 크기를 고려할 때 필요한 개수가 더 많은 것을 선택해야 합니다.
    required_v = max(required_rv, required_sv)

    # 회전하기 전 필요한 모니터의 개수를 게산합니다.
    required_not_turn = required_h * required_v

    # 가로, 세로의 정보를 바꿔줍니다.
    # 회전시켜서 대형 모니터를 만드는 것을 계산하기 위해서입니다.
    rhi, rvi = rvi, rhi
    shi, svi = svi, shi

    # 가로로 해상도를 고려할 때 필요한 모니터의 개수를 저장하는 변수입니다.
    required_rh = math.ceil(rh / rhi)
    # 가로로 크기를 고려할 때 필요한 모니터의 개수를 저장하는 변수입니다.
    required_sh = math.ceil(sh / shi)
    # 세로로 해상도를 고려할 때 필요한 모니터의 개수를 저장하는 변수입니다.
    required_rv = math.ceil(rv / rvi)
    # 세로로 크기를 고려할 때 필요한 모니터의 개수를 저장하는 변수입니다.
    required_sv = math.ceil(sv / svi)

    # 가로로 필요한 모니터의 개수에서 해상도와 크기를 고려할 때 필요한 개수가 더 많은 것을 선택해야 합니다.
    required_h = max(required_rh, required_sh)
    # 세로로 필요한 모니터의 개수에서 해상도와 크기를 고려할 때 필요한 개수가 더 많은 것을 선택해야 합니다.
    required_v = max(required_rv, required_sv)

    # 회전한 후 필요한 모니터의 개수를 게산합니다.
    required_turn = required_h * required_v

    # 회전하기 전과 회전한 후 모니터로 대형 모니터를 만들 때 각각 필요한 개수 중 더 작은 개수를 고릅니다.
    min_monitor = min(required_not_turn, required_turn)

    # 필요한 가격을 계산합니다.
    current_price = min_monitor * pi

    # 이전까지 가장 저렴한 가격과 비교해봅니다.
    # 만약 지금 계산한 가격이 처음 계산하는 가격이거나 (min_price == -1)
    # 앞서 저장되어 있던 가장 저렴한 가격보다 지금 계산한 가격이 더 저렴하다면
    if min_price == -1 or min_price >= current_price:
        # 현재 계산한 가격을 가장 저렴한 가격 변수에 저장합니다.
        min_price = current_price

# 최종적으로 가장 저렴한 가격을 출력합니다.
print(min_price)
