# https://codeup.kr/problem.php?id=6068

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 0 ~ 100인 점수를 의미하는 정수를 하나 입력합니다.
# 정수형으로 변환합니다.
score = int(stdin.readline())

# 점수가 90 ~ 100이라면
if 90 <= score <= 100:
    # A를 출력합니다.
    print("A")
# 점수가 70 ~ 89라면
elif 70 <= score <= 89:
    # B를 출력합니다.
    print("B")
# 점수가 40 ~ 69라면
elif 40 <= score <= 69:
    # C를 출력합니다.
    print("C")
# 점수가 0 ~ 39라면
elif 0 <= score <= 39:
    # D를 출력합니다.
    print("D")