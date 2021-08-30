# https://codeup.kr/problem.php?id=1229

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 키 h, 몸무게 w를 공백으로 구분해 입력합니다.
# 1 <= w, h <= 200
# 각각 float형으로 변환합니다.
h, w = map(float, stdin.readline().split())
# 표준 몸무게를 저장할 변수를 선언합니다.
# 0으로 초기화합니다.
standard_weight = 0
# 비만도를 저장할 변수를 선언합니다.
# 0으로 초기화합니다.
obesity_level = 0

# 키에 따른 표준 몸무게를 구해봅니다.
# 키가 150 미만이라면
if h < 150:
    # 표준 몸무게는 (실제 키 - 100)로 계산하고 변수에 저장합니다.
    standard_weight = h - 100
# 키가 150 이상 160 미만이라면
elif 150 <= h < 160:
    # 표준 몸무게는 (실제 키 - 150) / 2 + 50으로 계산하고 변수에 저장합니다.
    standard_weight = (h - 150) / 2 + 50
# 그 외의 경우인 키가 160 이상이라면
else:
    # 표준 몸무게는 (실제 키 - 100) * 0.9로 계산하고 변수에 저장합니다.
    standard_weight = (h - 100) * 0.9

# 실제 몸무게, 표준 몸무게로 비만도를 계산하고 변수에 저장합니다.
obesity_level = (w - standard_weight) * 100 / standard_weight

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