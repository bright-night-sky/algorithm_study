# https://codeup.kr/problem.php?id=6039

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 2개의 실수 f1, f2를 공백으로 구분해 입력합니다.
# 각각 실수형으로 변환합니다.
f1, f2 = map(float, stdin.readline().split(' '))

# f1을 f2번 거듭제곱한 값을 출력합니다.
print(f1 ** f2)