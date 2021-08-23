# https://codeup.kr/problem.php?id=1167

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 세 개의 정수를 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환하고, 리스트 변수에 넣어줍니다.
nums = list(map(int, stdin.readline().split()))

# nums 내부의 값들을 오름차순으로 정렬합니다.
nums.sort()

# nums의 값들 중 두 번째로 작은 수를 출력합니다.
print(nums[1])