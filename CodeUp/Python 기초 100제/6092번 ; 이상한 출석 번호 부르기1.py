# https://codeup.kr/problem.php?id=6092

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 번째 줄에 출석 번호를 부른 횟수인 정수 n을 입력합니다.
# 정수형으로 변환합니다.
n = int(stdin.readline())
# 두 번째 줄에는 무작위로 부른 n개의 번호를 공백을 두고 순서대로 입력합니다.
# 각각 정수형으로 변환하고 리스트 변수에 넣어줍니다.
nums = list(map(int, stdin.readline().split()))

# 1부터 23까지 반복합니다.
for num in range(1, 24):
    # 현재 번호가 불린 횟수를 출력하고, 한 칸 띄어줍니다.
    print(nums.count(num), end=' ')