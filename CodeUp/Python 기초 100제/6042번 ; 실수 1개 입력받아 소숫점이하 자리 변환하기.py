# https://codeup.kr/problem.php?id=6042

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 실수 1개를 입력합니다.
# 실수형으로 변환합니다.
num = float(stdin.readline())

# 입력한 실수를 소숫점 이하 두 번째 자리까지 정확도로 반올림한 값을 출력합니다.
print(format(num, '.2f'))