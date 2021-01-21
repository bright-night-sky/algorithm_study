# https://www.acmicpc.net/problem/2755

# 반올림 모드 설정
import decimal
ctx = decimal.getcontext()
ctx.rounding = decimal.ROUND_UP

# 첫째 줄에 이번 학기에 들은 과목 수 입력
subjects = int(input())

# 성적과 성적 점수를 연결한 dictionary
scores_dict = {
    'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
    'F': 0.0
}

# 학점*성적을 모두 더한 총 점수를 저장할 변수
total_score = 0
# 총 학점을 저장할 변수
total_credits = 0

# 둘째 줄부터 N개의 줄에 각 과목의 성적 정보 입력
for i in range(0, subjects):
    # 과목의 과목명, 학점, 성적 입력
    subject, credit, score = input().split(' ')
    # 입력받은 학점을 숫자로 변환
    credit = int(credit)

    # 총 학점에 현재 과목의 학점을 더함
    total_credits += credit
    # 총 점수에 현재 과목의 학점*성적을 더함
    total_score += decimal.Decimal(credit * scores_dict[score])

# 평균 평점을 계산하고 소수점 셋째 자리에서 반올림해서 둘째 자리까지의 수로 만든다.
average = "%.2f" % round(decimal.Decimal(total_score / total_credits), 2)

# 평균 평점을 출력한다.
print(average)
