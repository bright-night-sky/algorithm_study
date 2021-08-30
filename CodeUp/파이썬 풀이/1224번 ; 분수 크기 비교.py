# https://codeup.kr/problem.php?id=1224

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 네 자연수 a, b, c, d를 공백으로 구분해 입력합니다.
# 각각 int형으로 변환합니다.
a, b, c, d = map(int, stdin.readline().split())
# 분수 a/b의 값을 변수에 저장합니다.
ab = a / b
# 분수 c/d의 값을 변수에 저장합니다.
cd = c / d

# a/b의 값이 c/d의 값보다 크다면
if ab > cd:
    # 문자 '>'를 출력합니다.
    print('>')
# a/b의 값이 c/d의 값과 같다면
elif ab == cd:
    # 문자 '='를 출력합니다.
    print('=')
# 그 외의 경우, 즉, a/b의 값이 c/d의 값보다 작다면
else:
    # 문자 '<'를 출력합니다.
    print('<')