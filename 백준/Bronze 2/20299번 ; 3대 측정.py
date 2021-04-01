# https://www.acmicpc.net/problem/20299

import timeit

start_time = timeit.default_timer()

# 첫째 줄에 정수 팀의 수 N,
# 팀원 3명의 레이팅 합에 대한 클럽 가입 조건 K,
# 개인 레이팅에 대한 클럽 가입 조건 L을 입력합니다.
# 1 <= N <= 500,000
# 0 <= K <= 12,000
# 0 <= L <= 4,000
N, K, L = map(int, input().split(' '))

# VIP 클럽에 가입 가능한 팀의 수를 저장할 변수 VIP_team_count를 만들고, 0으로 초기화해줍니다.
VIP_team_count = 0
# VIP 회원들의 레이팅을 저장할 변수 rating_of_VIP를 만들고, ''으로 초기화합니다.
rating_of_VIP = ''

# 팀의 수 N만큼 반복해봅니다.
for i in range(N):
    # 팀원들의 레이팅 정보인 x1, x2, x3를 입력합니다.
    # 0 <= x1, x2, x3 <= 4,000
    x1, x2, x3 = map(int, input().split(' '))

    # 입력받은 팀원들의 레이팅의 합을 team_rating_total 변수에 저장합니다.
    team_rating_total = x1 + x2 + x3

    if team_rating_total >= K and x1 >= L and x2 >= L and x3 >= L:
        VIP_team_count += 1
        rating_of_VIP += f'{x1} {x2} {x3} '

print(VIP_team_count)
print(rating_of_VIP)

terminate_time = timeit.default_timer()  # 종료 시간 체크

print("%f초 걸렸습니다." % (terminate_time - start_time))