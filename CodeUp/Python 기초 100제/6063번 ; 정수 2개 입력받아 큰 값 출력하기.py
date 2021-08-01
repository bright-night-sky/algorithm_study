# https://codeup.kr/problem.php?id=6063

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 정수 2개를 공백을 두고 입력합니다.
# 각각 정수형으로 변환합니다.
num1, num2 = map(int, stdin.readline().split(' '))

# 3항 연산을 사용해봅니다.
# num1과 num2 중 num1이 num2보다 크거나 같다면 num1의 값을 출력하고,
# 그렇지 않다면 num2의 값을 출력합니다.
print(num1 if num1 >= num2 else num2)