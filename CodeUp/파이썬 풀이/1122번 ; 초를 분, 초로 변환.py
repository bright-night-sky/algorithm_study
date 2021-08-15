# https://codeup.kr/problem.php?id=1122

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 초를 입력합니다.
# 정수형으로 변환합니다.
second = int(stdin.readline())
# 입력한 초를 60으로 나누고 나온 몫인 분을 저장하는 변수를 선언합니다.
minute = second // 60
# 입력한 초를 60으로 나누고 나온 나머지인 초를 다시 second 변수에 저장합니다.
second %= 60

# 분, 초 순서로 공백으로 구분해 출력합니다.
print(minute, second)