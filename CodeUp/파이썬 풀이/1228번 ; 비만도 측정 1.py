# https://codeup.kr/problem.php?id=1228

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 희윤이의 키, 몸무게를 공백으로 구분해 입력합니다.
# 각각 float형으로 변환합니다.
height, weight = map(float, stdin.readline().split())
# 입력한 키에 따른 표준 몸무게를 계산하고 변수에 저장합니다.
standard_weight = (height - 100) * 0.9
# 입력한 몸무게와 계산한 표준 몸무게를 통해 비만도를 계산하고 변수에 저장합니다.
obesity_level = (weight - standard_weight) * 100 / standard_weight

# 비만도가 10 이하라면
if obesity_level <= 10:
    # 정상이므로 문자열 '정상'을 출력합니다.
    print('정상')
# 비만도가 10 이상 20 이하라면
elif 10 <= obesity_level <= 20:
    # 과체중이므로 문자열 '과체중'을 출력합니다.
    print('과체중')
# 그 외의 경우인 비만도가 20 초과라면
else:
    # 비만이므로 문자열 '비만'을 출력합니다.
    print('비만')