# https://codeup.kr/problem.php?id=6043

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 2개의 실수를 공백으로 구분해 입력합니다.
# 각각 실수형으로 변환합니다.
f1, f2 = map(float, stdin.readline().split(' '))

# 먼저 f1을 f2로 나눈 값을 소숫점 셋째 자리에서 반올림합니다.
# 출력 형식에 맞게 소숫점 셋째 자리까지 출력합니다.
print(format(round(f1 / f2, 3), '.3f'))