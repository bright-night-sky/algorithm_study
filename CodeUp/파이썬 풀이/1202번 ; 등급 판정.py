# https://codeup.kr/problem.php?id=1202

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 점수를 입력합니다.
# 0 ~ 100의 정수입니다.
# 정수형으로 변환합니다.
score = int(stdin.readline())

# 입력한 점수가 90 이상이라면
if score >= 90:
    # 문자 'A'를 출력합니다.
    print('A')
# 입력한 점수가 위의 조건문은 만족하지 않고 80 이상이라면
elif score >= 80:
    # 문자 'B'를 출력합니다.
    print('B')
# 입력한 점수가 위의 조건문들은 만족하지 않고 70 이상이라면
elif score >= 70:
    # 문자 'C'를 출력합니다.
    print('C')
# 입력한 점수가 위의 조건문들은 만족하지 않고 70 이상이라면
elif score >= 60:
    # 문자 'D'를 출력합니다.
    print('D')
# 입력한 점수가 위의 조건문들은 모두 만족하지 않으면, 즉, 70점 미만이라면
else:
    # 문자 'F'를 출력합니다.
    print('F')