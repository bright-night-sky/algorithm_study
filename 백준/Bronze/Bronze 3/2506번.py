# https://www.acmicpc.net/problem/2506

# N : 문제의 개수 (1 <= N <= 100)
N = int(input())

# N개 문제의 채점 결과 입력
OX = list(map(int, input().split(' ')))

# 총 점수를 저장하는 변수
sum = 0

# 문제를 연속으로 맞힌 경우 쌓이는 점수를 저장하는 변수
stack_score = 0

# 문제를 맞았는지 틀렸는지 반복문으로 확인
for i in OX:
    # 맞은 문제인 경우
    if i == 1:
        # 총 점수에 일단 1점을 더하고
        # 앞의 문제를 맞은 경우 쌓이는 점수도 더해준다.
        sum += 1 + stack_score
        # 뒤의 문제를 또 맞았을 수도 있기 때문에 점수를 1점 쌓아준다.
        stack_score += 1
    # 틀린 문제인 경우
    else:
        # 연속으로 맞춘 경우 주는 점수를 0점으로 만든다.
        stack_score = 0

# 총점 출력
print(sum)
