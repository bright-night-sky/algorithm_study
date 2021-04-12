# https://www.acmicpc.net/problem/17389

# 첫 번째 줄에는 OX표의 길이인 자연수 N을 입력합니다.
# 1 <= N <= 10,000
N = int(input())

# 두 번째 줄에는 OX표를 의미하는 문자열 S를 입력합니다.
# 길이는 N입니다.
S = input()

# 최종 점수를 저장할 변수를 선언합니다.
score = 0
# 보너스 점수를 저장할 변수를 선언합니다.
bonus = 0

# 문자열 S의 한 문제마다 반복해봅니다.
for index in range(len(S)):
    # 현재 문제를 맞췄다면
    if S[index] == 'O':
        # 최종 점수에 문제의 인덱스 + 1과 현재 저장 중인 보너스 점수를 더해줍니다.
        score += index + 1 + bonus
        # 보너스 점수 변수에도 1을 더해줍니다.
        bonus += 1
    # 현재 문제를 틀렸다면
    else:
        # 보너스 점수를 0점으로 초기화합니다.
        bonus = 0

# 최종 점수를 출력합니다.
print(score)