# https://codeup.kr/problem.php?id=1123

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 섭씨 온도를 입력합니다.
# 정수형으로 변환합니다.
celsius = int(stdin.readline())
# 섭씨 온도를 화씨 온도로 변환한 값을 저장한 변수를 선언합니다.
fahrenheit = 9 / 5 * celsius + 32

# 화씨 온도인 fahrenheit의 값을 소수 셋째 자리까지 출력합니다.
print('%.3f' % fahrenheit)