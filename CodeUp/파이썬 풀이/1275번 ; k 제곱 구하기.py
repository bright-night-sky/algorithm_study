# https://codeup.kr/problem.php?id=1275

# readline을 사용하기 위해 import합니다.
from sys import stdin


# n, k를 공백으로 구분해 입력합니다.
# n은 0이 아닌 정수, k >= 0
# 각각 int형으로 변환합니다.
n, k = map(int, stdin.readline().split())

# n의 k승을 계산하고 그 값을 출력합니다.
print(n ** k)