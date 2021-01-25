# https://www.acmicpc.net/problem/2953

# 최고 점수를 저장하는 변수입니다.
max_score = 0

# 최고 점수를 받은 참가자의 번호를 저장하는 변수입니다.
max_parti = 0

# 참가자가 다섯명이므로 반복문을 5번 돌립니다.
for i in range(1, 6):
    # 현재 참가자가 받은 점수 4개를 공백으로 구분해서 입력합니다.
    scores = list(map(int, input().split(' ')))

    # 받은 점수의 합계를 구합니다.
    cur_sum = sum(scores)

    # 이전까지의 최고 점수보다 현재 참가자의 점수가 더 높다면
    if cur_sum > max_score:
        # 최고 점수 변수에 현재 참가자의 점수를 저장해줍니다.
        max_score = cur_sum
        # 최고 점수를 받은 참가자의 번호를 저장해줍니다.
        max_parti = i

# 결과인 우승자의 번호와 그가 얻은 점수를 출력합니다.
print(max_parti, max_score)