# https://codeup.kr/problem.php?id=1201

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 정수 하나를 입력합니다.
# 정수형으로 변환합니다.
num = int(stdin.readline())

# 입력한 정수가 0보다 크면, 즉, 양수이면
if num > 0:
    # 문자열 "양수"를 출력합니다.
    print("양수")
# 입력한 정수가 0보다 작으면, 즉, 음수이면
elif num < 0:
    # 문자열 "음수"를 출력합니다.
    print("음수")
# 그 외의 경우, 즉, 입력한 정수가 0이라면
else:
    # 0을 출력합니다.
    print(0)