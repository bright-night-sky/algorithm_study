# https://www.acmicpc.net/problem/1268

from sys import stdin

students_cnt = int(stdin.readline().rstrip())

each_students_class_num = []

for student_idx in range(students_cnt):
    student_class_num = list(stdin.readline().rstrip().split(' '))
    each_students_class_num.append(student_class_num)

each_students_same_class_cnt = []

for student1 in each_students_class_num:
    same_cnt = 0
    for student2 in each_students_class_num:
        same_grade = [class1 for class1, class2 in zip(student1, student2) if class1 == class2]
        same_cnt += len(same_grade)
    each_students_same_class_cnt.append(same_cnt)

print(each_students_same_class_cnt)

max_same_student = max(each_students_same_class_cnt)
max_same_student_num = each_students_same_class_cnt.index(max_same_student) + 1

print(max_same_student_num)