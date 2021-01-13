# https://www.acmicpc.net/problem/9498

# 시험 점수 입력
# 0 <= 시험 점수 <= 100
test_score = int(input())

# 시험 점수가 90 ~ 100점이면
if 90 <= test_score <= 100:
    # A 출력
    print("A")
# 시험 점수가 80 ~ 89점이면
elif 80 <= test_score <= 89:
    # B 출력
    print("B")
# 시험 점수가 70 ~ 79점이면
elif 70 <= test_score <= 79:
    # C 출력
    print("C")
# 시험 점수가 60 ~ 69점이면
elif 60 <= test_score <= 69:
    # D 출력
    print("D")
# 나머지 점수는
else:
    # F 출력
    print("F")