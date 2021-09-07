# https://codeup.kr/problem.php?id=1271

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 정수의 개수 n을 입력합니다.
# n <= 1,000
n = stdin.readline()
# 둘째 줄의 n개의 정수를 공백으로 구분해 입력합니다.
# 0 <= 각 정수 <= 1,000,000
# 각각 int형으로 변환합니다.
nums = map(int, stdin.readline().split())

# nums 중에서 최댓값을 출력합니다.
print(max(nums))