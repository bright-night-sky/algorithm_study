# https://www.acmicpc.net/problem/2754

# 성적에 따른 평점을 dictionary 변수로 저장합니다.
grade_to_score = {
    'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
    'F': 0.0
}

# 첫째 줄에 C언어 성적을 입력합니다.
C_grade = input()

# 입력한 성적에 따른 평점을 출력합니다.
print(grade_to_score[C_grade])