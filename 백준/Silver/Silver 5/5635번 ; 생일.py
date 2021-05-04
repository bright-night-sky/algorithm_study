# https://www.acmicpc.net/problem/5635

# 첫째 줄에 반에 있는 학생의 수 n을 입력합니다.
# 1 <= n <= 100
n = int(input())

# 학생들의 이름과 생일 정보를 저장하는 리스트 변수를 저장합니다.
students = []

# 학생의 수 n만큼 반복합니다.
for student_index in range(n):
    # 한 학생의 이름, 생일 정보 일, 월, 연도를 dd mm yyyy 형식으로 공백으로 구분해 입력합니다.
    # 학생의 이름은 최대 15글자입니다.
    # 1990 <= yyyy <= 2010
    # 1 <= mm <= 12
    # 1 <= dd <= 31
    # 연, 월, 일은 0으로 시작하지 않습니다.
    student = input().split(' ')

    # 생일 정보인 dd mm yyyy를 정수형으로 변환해줍니다.
    student[1:] = map(int, student[1:])

    # 한 학생의 정보를 students 리스트 변수에 넣어줍니다.
    students.append(student)

# students 리스트 변수 내부의 값들을 연, 월, 일을 기준으로 오름차순 정렬해줍니다.
# 오름차순 정렬이므로 앞에 있을수록 연, 월, 일이 작으므로 나이가 더 많은 사람,
# 뒤에 있을수록 연, 월, 일이 크므로 나이가 더 적은 사람입니다.
students.sort(key=lambda student: (student[3], student[2], student[1]))

# 나이가 제일 적은 사람의 이름을 출력합니다.
print(students[-1][0])
# 나이가 제일 많은 사람의 이름을 출력합니다.
print(students[0][0])