# https://www.acmicpc.net/problem/1268

from sys import stdin

# 첫째 줄에는 반의 학생 수를 나타내는 정수를 입력합니다.
students_count = int(stdin.readline().rstrip())

students_classes = []

for student_index in range(students_count):
    student_classes = list(map(int, stdin.readline().rstrip().split(' ')))

    students_classes.append(student_classes)

same_class_count = []

cur_student_num = 0

for grade in range(5):
    for student_index in range(students_count):


