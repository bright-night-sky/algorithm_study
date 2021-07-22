# https://codeup.kr/problem.php?id=6046

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 정수 1개를 입력합니다.
# 정수형으로 변환합니다.
num = int(stdin.readline())

# 왼쪽 비트시프트 연산자를 적용해서 입력한 정수의 2배를 계산해 출력합니다.
print(num << 1)