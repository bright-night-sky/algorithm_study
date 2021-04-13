# https://www.acmicpc.net/problem/16462

# 첫째 줄에 학생의 수 N을 입력합니다.
# 1 <= N <= 1,000
N = int(input())

# 학생의 점수를 모두 더해서 저장하는 변수를 선언합니다.
total = 0

# 학생의 수 N만큼 반복합니다.
for i in range(N):
    Qi = input()

    Qi = Qi.replace('0', '9')
    Qi = Qi.replace('6', '9')
    Qi = int(Qi)

    if Qi >= 100:
        Qi = 100

    total += Qi

print(round(total / N))