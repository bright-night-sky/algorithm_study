# https://codeup.kr/problem.php?id=1203

# readline을 사용하기 위해 import합니다.
from sys import stdin


# BMI 수치를 정수로 입력합니다.
# int형으로 변환합니다.
bmi = int(stdin.readline())

# 입력한 BMI 수치가 10 이하라면
if bmi <= 10:
    # 문자열 '정상'을 출력합니다.
    print('정상')
# 입력한 BMI 수치가 20 이하라면
elif bmi <= 20:
    # 문자열 '과체중'을 출력합니다.
    print('과체중')
# 그 외의 경우, 즉, 입력한 BMI 수치가 20 초과라면
else:
    # 문자열 '비만'을 출력합니다.
    print('비만')