# https://codeup.kr/problem.php?id=1257

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 시작 수, 마지막 수를 의미하는 a, b를 공백으로 구분해 입력합니다.
# a <= b
# 각각 int형으로 변환합니다.
a, b = map(int, stdin.readline().split())

# a부터 b까지 반복해봅니다.
for num in range(a, b + 1):
    # 현재 숫자가 홀수라면, 즉, 현재 숫자를 2로 나누었을 때 나머지가 1이라면
    if num % 2 == 1:
        # 현재 숫자를 출력한 뒤, 다음 줄로 내리지 않고 한 칸만 띄어줍니다.
        print(num, end=' ')