# https://codeup.kr/problem.php?id=1289

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 3개 운동장의 가로, 세로의 정수 길이를 공백으로 구분해 입력합니다.
# 각 길이는 1000 이하의 양의 정수값입니다.
# 각각 int형으로 변환합니다.
width1, height1 = map(int, stdin.readline().split())
width2, height2 = map(int, stdin.readline().split())
width3, height3 = map(int, stdin.readline().split())
# 3개 운동장의 가로와 세로를 곱해 넓이를 계산하고 변수에 저장합니다.
schoolyard1 = width1 * height1
schoolyard2 = width2 * height2
schoolyard3 = width3 * height3

# 3개 운동장의 넓이 중 가장 넓은 운동장의 넓이를 출력합니다.
print(max(schoolyard1, schoolyard2, schoolyard3))
