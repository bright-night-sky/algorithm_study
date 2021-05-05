# https://www.acmicpc.net/problem/11292

# 학생의 수 N에 0을 입력할 때까지 반복합니다.
while True:
    # 학생의 수 N을 입력합니다.
    # 0 <= N <= 50
    N = int(input())

    # 입력한 N이 0이라면
    if N == 0:
        # 반복문을 탈출하고 종료합니다.
        break
    # 입력한 N이 0이 아니라면
    else:
        # 학생들의 이름과 키의 정보를 저장하는 리스트 변수를 선언합니다.
        students = []

        # 학생의 수 N만큼 반복합니다.
        for student_index in range(N):
            # 한 학생의 이름과 키를 공백으로 구분해 입력합니다.
            student = input().split(' ')

            # 학생의 키는 실수형으로 변환해줍니다.
            student[1] = float(student[1])

            # 학생의 이름, 키 정보를 students 리스트 변수에 넣어줍니다.
            students.append(student)

        # 학생의 키를 기준으로 가장 큰 키의 값을 저장하는 변수를 선언합니다.
        max_height = max(students, key=lambda student: student[1])[1]

        # 학생 한 명마다 반복해봅니다.
        for student in students:
            # 현재 학생의 키가 가장 큰 키의 값과 같다면
            if student[1] == max_height:
                # 학생의 이름을 출력 형식에 맞게 출력합니다.
                print(student[0], end=' ')

        # 한 테스트 케이스가 끝났으면 한 줄 내려줍니다.
        print()