# https://www.acmicpc.net/problem/2460

# 가장 많을 때의 사람 수를 저장하는 변수
max_men = 0
# 현재 기차에 타고 있는 사람 수를 저장하는 변수
current_men = 0

for i in range(0, 10):
    # 각 역에서 내린 사람 수와 탄 사람 수를 입력 : 역은 10개이므로 10번 반복
    drop_men, ride_men = map(int, input().split(' '))

    # 현재 기차에 타고 있는 사람 계산
    current_men = current_men - drop_men + ride_men

    # 현재 기차에 타고 있는 사람 수와 이전까지 가장 많을 때의 사람 수 비교
    # 현재 기차에 타고 있는 사람 수가 이전까지 가장 많을 때의 사람 수보다 많으면
    if max_men < current_men:
        # 가장 많을 때의 사람 수 변수에 저장
        max_men = current_men

# 가장 많을 때의 사람 수 출력
print(max_men)