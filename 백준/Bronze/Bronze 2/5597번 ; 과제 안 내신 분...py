# https://www.acmicpc.net/problem/5597

attendance = [None for student in range(30)]

for i in range(28):
    student = int(input())

    attendance[student-1] = True

