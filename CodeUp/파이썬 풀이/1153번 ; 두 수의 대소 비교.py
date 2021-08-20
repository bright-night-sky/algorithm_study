# https://codeup.kr/problem.php?id=1153

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 두 정수 a, b를 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
a, b = map(int, stdin.readline().split())

# a의 값이 b의 값보다 크면
if a > b:
    # >를 출력합니다.
    print('>')
# b의 값이 a의 값보다 크면
elif a < b:
    # <를 출력합니다.
    print('<')
# 그 외의 경우, 즉, a의 값과 b의 값이 같으면
else:
    # =를 출력합니다.
    print('=')