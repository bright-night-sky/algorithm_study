# https://codeup.kr/problem.php?id=6064

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 정수 3개를 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
num1, num2, num3 = map(int, stdin.readline().split(' '))

# 정수 3개 중 가장 작은 값을 출력합니다.
# 먼저 num1과 num2의 값을 비교해서 작은 값을 찾아 낸 뒤,
# num1과 num2 중 더 작은 값을 num3과 비교하여 제일 작은 값을 찾아서 출력하는 것입니다.
print((num1 if num1 < num2 else num2) if ((num1 if num1 < num2 else num2) < num3) else num3)