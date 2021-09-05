# https://codeup.kr/problem.php?id=1266

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 수의 개수인 자연수 n을 입력합니다.
# n <= 1,000
# int형으로 변환합니다.
n = int(stdin.readline())
# n개의 정수들을 공백으로 구분해 입력합니다.
# 각 수는 0 ~ 100입니다.
# 각각 int형으로 변환하고, 리스트에 넣어줍니다.
nums = list(map(int, stdin.readline().split()))

# 정수 리스트 nums의 값들의 합을 구하고 출력합니다.
print(sum(nums))