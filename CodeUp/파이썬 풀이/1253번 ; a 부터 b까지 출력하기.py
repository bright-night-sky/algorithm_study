# https://codeup.kr/problem.php?id=1253

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 두 정수 a, b를 공백으로 구분해 입력합니다.
# 각각 int형으로 변환합니다.
a, b = map(int, stdin.readline().split())
# 입력한 a, b 범위를 저장할 변수를 선언합니다.
num_range = None

# a가 b보다 크다면
if a > b:
    # num_range에 b부터 a까지 범위로 저장합니다.
    num_range = range(b, a + 1)
# 그 오의 경우인 a가 b 이하라면
else:
    # num_range에 a부터 b까지 범위로 저장합니다.
    num_range = range(a, b + 1)

# num_range의 범위의 숫자들을 하나씩 반복해봅니다.
for num in num_range:
    # 현재 숫자를 출력하고, 다음 줄로 내리지 않고 한 칸만 띄어줍니다.
    print(num, end=' ')