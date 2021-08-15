# https://codeup.kr/problem.php?id=1120

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 세 정수를 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
num1, num2, num3 = map(int, stdin.readline().split())
# 세 수의 평균을 저장하는 변수를 선언합니다.
avg = (num1 + num2 + num3) / 3

# 평균인 avg의 값을 소수 둘째 자리까지 출력합니다.
print('%.2f' % avg)