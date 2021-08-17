# https://codeup.kr/problem.php?id=1137

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 두 정수 a, b를 공백을 두고 입력합니다.
# a, b는 int형 범위입니다.
# 각각 정수형으로 변환합니다.
a, b = map(int, stdin.readline().split())

# a와 b가 같지 않을 경우 1을, 그렇지 않은 경우 0을 출력합니다.
print(1 if a != b else 0)