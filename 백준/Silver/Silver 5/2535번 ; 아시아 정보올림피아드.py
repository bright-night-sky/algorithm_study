# https://www.acmicpc.net/problem/2535

# 첫 번째 줄에는 대회참가 학생 수 N을 입력합니다.
# 3 <= N <= 100
N = int(input())

# 입력한 학생들의 정보를 저장하는 리스트 변수를 선언합니다.
students = []

# 대회참가 학생 수 N만큼 반복합니다.
for student_index in range(N):
    # 한 학생의 소속 국가 번호, 학생 번호, 성적을 공백으로 구분하고 입력합니다.
    # 소속 국가 번호, 학생 번호, 성적은 정수형으로 변환하고 하나의 리스트 형태로 넣어줍니다.
    student_info = list(map(int, input().split(' ')))

    # 한 학생의 정보 리스트 변수를 students 리스트에 넣어줍니다.
    students.append(student_info)

# students 내부의 학생 정보들을 성적을 기준으로 내림차순으로 정렬합니다.
students.sort(key=lambda student: student[2], reverse=True)

# 금메달은 성적이 제일 높은 학생입니다.
gold = students[0]
# 은메달은 성적이 두 번째로 높은 학생입니다.
silver = students[1]
# 동메달을 수여받는 사람은 금메달과 은메달을 받은 사람이 같은 나라 사람이라면
# 무조건 세 번째 사람이 아닐수도 있으니 일단 None으로 초기화해줍니다.
bronze = None

# students 리스트 변수에서 세 번째로 높은 점수를 가진 사람부터 끝까지 반복해봅니다.
for student_index in range(2, len(students)):
    # 금메달을 받은 학생과 은메달을 받은 학생과 동메달을 받을 자격이 있을 것 같은 이번 학생이
    # 같은 소속 국가 번호를 가지고 있다면
    if gold[0] == silver[0] == students[student_index][0]:
        # 이번 학생은 동메달을 못 받으므로 다음 학생의 여부로 넘어갑니다.
        continue
    # 이번 학생이 동메달을 받을 수 있는 자격이 된다면
    else:
        # 동메달은 이번 학생이 받습니다.
        bronze = students[student_index]
        # 반복문을 탈출합니다.
        break

# 금, 은, 동메달을 받은 학생들의 소속 국가 번호와 학생 번호를 출력 형식에 맞게 출력합니다.
print(gold[0], gold[1])
print(silver[0], silver[1])
print(bronze[0], bronze[1])
