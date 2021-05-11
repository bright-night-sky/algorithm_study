# https://www.acmicpc.net/problem/10156

# 과자 한 개의 가격 K
# 사려고 하는 과자의 개수 N
# 현재 동수가 가진 돈 M
# 1 <= K, N <= 1,000
# 1 <= M <= 100,000
# 위의 세 변수를 각각 공백을 사이에 두고 입력
K, N, M = map(int, (input().split(' ')))

# 과자를 모두 사는데 필요한 돈을 저장하는 변수
total_money = K * N

# 과자를 모두 사는데 필요한 돈보다 동수가 가진 돈이 적다면
if total_money > M:
    # 부모님께 받아야 하는 돈의 액수를 출력
    print(total_money - M)
# 돈이 모자라지 않다면
else:
    # 부모님께 받아야 하는 돈은 0원이다.
    print(0)