# https://www.acmicpc.net/problem/2605

# 첫째 줄에는 학생의 수를 입력합니다.
# 100 이하입니다.
student_num = int(input())

# 둘째 줄에는 줄을 선 차례대로 학생들이 뽑은 번호를 입력합니다.
# 0 또는 자연수입니다.
# 뽑은 번호 사이에는 빈 칸이 하나씩 있습니다.
nums = list(map(int, input().split(' ')))

# 최종적으로 줄을 선 결과를 저장하는 변수입니다.
result = ''

for student in range(1, student_num+1):
    result = result[0:] + student + ' ' + result[]