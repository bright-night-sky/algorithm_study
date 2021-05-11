# https://www.acmicpc.net/problem/5032

# 첫째 줄에 준민이가 가지고 있는 빈 병의 수 e,
# 그날 발견한 빈 병의 수 f,
# 새 병으로 바꾸는데 필요한 빈 병의 개수 c를 입력합니다.
# e < 1000,
# f < 1000,
# 1 < c < 2000
# e, f, c는 모두 음이 아닌 정수입니다.
e, f, c = map(int, input().split(' '))

soda_drink = int((e + f) / c)

while True:
    new_soda_drink = int((e + f) / c)
    soda_drink +=