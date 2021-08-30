# https://codeup.kr/problem.php?id=1216

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 홍보를 하지 않을 경우 수입(not_promote_revenue),
# 홍보를 할 경우의 수입(after_prmote_revenue),
# 홍보 비용(promotion_expense)를 의미하는 세 정수를 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
not_promote_revenue, after_promote_revenue, promotion_expense = map(int, stdin.readline().split())
# 홍보를 할 경우의 수입에서 홍보 비용을 빼서 홍보를 할 경우의 순수익을 계산하고 변수 promote_net_gain에 저장합니다.
promote_net_gain = after_promote_revenue - promotion_expense

# 홍보를 할 경우의 순수익이 홍보를 하지 않을 경우 수입보다 커서 홍보를 하는 경우가 유리하면
if promote_net_gain > not_promote_revenue:
    # 문자열 'advertise'를 출력합니다.
    print('advertise')
# 홍보를 할 경우의 순수익이 홍보를 하지 않을 경우 수입보다 작아서 홍보를 하지 않는 경우가 유리하면
elif promote_net_gain < not_promote_revenue:
    # 문자열 'do not advertise'를 출력합니다.
    print('do not advertise')
# 그 외의 경우인, 홍보를 할 경우의 순수익과 홍보를 하지 않을 경우 수입이 같아서 홍보를 하든 안 하든 별 상관이 없으면
else:
    # 문자열 'does not matter'을 출력합니다.
    print('does not matter')