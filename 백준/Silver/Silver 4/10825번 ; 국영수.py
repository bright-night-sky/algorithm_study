# https://www.acmicpc.net/problem/10825

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 도현이네 반의 학생의 수 N을 입력합니다.
# 1 <= N <= 100,000
# 정수형으로 변환합니다.
N = int(stdin.readline())
# 학생들의 이름, 점수 정보 리스트들을 저장할 리스트 변수를 선언합니다.
# N개의 None으로 초기화합니다.
students_inform = [None] * N

# 학생의 수 N만큼 반복합니다.
for student_idx in range(N):
    # 각 학생의 이름, 국어, 영어, 수학 점수를 공백으로 구분해 입력합니다.
    # 점수는 1보다 크거나 같고, 100보다 작거나 같은 자연수입니다.
    # 이름은 알파벳 대소문자로 입력하고, 길이는 10자리를 넘지 않습니다.
    student_inform = stdin.readline().rstrip().split(' ')

    # 학생의 국어, 영어, 수학 점수는 정수형으로 변환합니다.
    student_inform[1:4] = map(int, student_inform[1:4])
    # 학생의 정보를 현재 인덱스 그대로 students_inform의 인덱스에 넣어줍니다.
    students_inform[student_idx] = student_inform

# students_inform의 값들을 문제의 조건인
# 1. 국어 점수가 감소하는 순서
# 2. 영어 점수가 증가하는 순서
# 3. 수학 점수가 감소하는 순서
# 4. 이름이 사전 순으로 증가하는 순서(대소문자에서는 대문자가 더 앞)
# 로 정렬해줍니다.
students_inform.sort(key=lambda student: (-student[1], student[2], -student[3], student[0]))

# 정렬된 students_inform의 값에서 학생의 이름을 하나씩 출력합니다.
for student_inform in students_inform:
    print(student_inform[0])