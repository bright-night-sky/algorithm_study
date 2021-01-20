# https://www.acmicpc.net/problem/14924

# 기차의 속도 S, 파리의 속도 T, 처음 두 기차 사이의 거리 D를 입력
# 각각 10,000보다 작거나 같은 양의 정수
# T > S
# D는 2*S의 배수
S, T, D = map(int, input().split(' '))

# 문제 설명에 있는 공식에 따라 두 기차가 만나는 시간을 저장하는 변수를 만듦
train_meet_time = D / (S * 2)
# 문제 설명에 있는 공식에 따라 파리의 이동거리를 저장하는 변수를 만듦
fly_travel_range = train_meet_time * T

# 파리의 이동거리를 출력
print(int(fly_travel_range))