# https://www.acmicpc.net/problem/1268

# 첫째 줄에는 반의 학생 수를 나타내는 정수 입력
# 3 <= 학생 수 <= 1000
student_num = int(input())

# 각 학생이 몇 반에 속했었는지를 저장할 변수
student_class_history = []

# 각 학생의 같은 반이었던 사람 수를 저장할 변수
same_class_count = []

# 학생 수만큼 몇 반에 속했는지 입력
for i in range(0, student_num):
    # 입력받은 한 학생의 반 이력을 student_class_history에 저장
    # 각 반은 1 이상 9 이하의 정수이다.
    student_class_history = list(map(int, input().split(' ')))

for i in student_class_history:


