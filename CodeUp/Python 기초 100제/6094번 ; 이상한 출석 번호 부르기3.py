# https://codeup.kr/problem.php?id=6094

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 줄에 번호를 부른 횟수 n을 입력합니다.
# 정수형으로 변환합니다.
n = int(stdin.readline())
# 두 번째 줄에 n개의 랜덤 번호들을 공백을 사이에 두고 순서대로 입력합니다.
# 각각 정수형으로 변환하고 리스트 변수에 넣어줍니다.
nums = list(map(int, stdin.readline().split()))

# 출석을 부른 번호 중에 가장 빠른 번호, 즉 가장 작은 번호를 구하고 출력합니다.
print(min(nums))