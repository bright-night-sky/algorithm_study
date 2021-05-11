# https://www.acmicpc.net/problem/10039

# 모든 학생의 점수의 합계를 저장할 변수
total = 0

# 각 학생의 점수를 한 줄씩 입력
# 0 <= 점수 <= 100인 5의 배수
for i in range(0, 5):
    score = int(input())

    # 입력받은 점수가 40점 미만인 경우 40점으로 처리
    if score < 40:
        score = 40

    # 각 학생들의 점수를 total 변수에 더한다.
    total += score

# 평균 점수 출력
print(int(total / 5))