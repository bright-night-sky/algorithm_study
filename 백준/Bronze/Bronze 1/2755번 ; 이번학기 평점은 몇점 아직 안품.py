# https://www.acmicpc.net/problem/2755

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 파이썬의 오사오입 방식을 사용하는 round 함수대신
# 우리가 일반적으로 알고있는 사사오입 방식의 반올림을 문제에 맞게 구현합니다.
# 숫자 하나를 매개변수로 받습니다.
def normal_round(number):
    # 매개변수로 받은 숫자가 3.1, 3.28과 같이 딱 나누어 떨어져
    # 길이가 4보다 작거나 같다면
    if len(str(number)) <= 4:
        # 숫자 그대로 반환합니다.
        return number
    # 매개변수로 받은 숫자가 3.115, 3.284와 같이
    # 길이가 5라면
    elif len(str(number)) == 5:
        # 문자열 형태 숫자의 맨 뒤에 1을 붙여줍니다.
        number = str(number) + '1'
        # 1이 붙은 상태로 소수점 셋째 자리에서 반올림한 결과를 반환합니다.
        return round(float(number), 2)
    # 매개변수로 받은 숫자가 3.1152323..., 3.2842132...과 같이
    # 길이가 5보다 길다면
    elif len(str(number)) > 5:
        # 소수점 셋째 자리에서 반올림한 결과를 반환합니다.
        return round(float(number), 2)

# 첫째 줄에 이번 학기에 들은 과목 수를 입력합니다.
subjects_cnt = int(stdin.readline())

# 성적과 성적 점수를 연결한 dictionary를 선언합니다.
scores_dict = {
    'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
    'F': 0.0
}

# 학점*성적을 모두 더한 총 점수를 저장할 변수를 선언합니다.
total_score = 0
# 총 학점을 저장할 변수를 선언합니다.
total_credits = 0

# 이번 학기에 들은 과목 수만큼 반복해봅니다.
for _ in range(subjects_cnt):
    # 과목의 과목명, 학점, 성적을 공백으로 구분해 입력합니다.
    # 과목명은 알파벳 소문자, 숫자, _로만 이루어져 있고 최대 100글자입니다.
    # 학점은 1보다 크거나 같고, 3보다 작거나 같은 자연수입니다.
    subject, credit, score = stdin.readline().rstrip().split(' ')
    # 입력받은 학점을 숫자로 변환합니다.
    credit = int(credit)

    # 총 학점에 현재 과목의 학점을 더합니다.
    total_credits += credit
    # 총 점수에 현재 과목의 학점*성적을 더합니다.
    total_score += credit * scores_dict[score]

# 평균 평점을 계산하고 소수점 셋째 자리에서 반올림해서 둘째 자리까지의 수로 만듭니다.
average = "%.2f" % normal_round(total_score / total_credits)

# 평균 평점을 출력합니다.
print(average)
