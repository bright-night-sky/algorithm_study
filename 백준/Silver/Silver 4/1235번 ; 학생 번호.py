# https://www.acmicpc.net/problem/1235

# 첫째 줄에는 학생의 수 N을 입력합니다.
# 2 <= N <= 1,000
N = int(input())

student_numbers = []

for student_index in range(N):
    student_number = input()

    student_numbers.append(student_number)

student_number_length = len(student_numbers[0])

for k in range(1, student_number_length + 1):
    student_k_numbers = []

    for student_number in student_numbers:
        student_k_number = student_number[-1:-(k+1)]

        student_k_numbers.append(student_k_number)