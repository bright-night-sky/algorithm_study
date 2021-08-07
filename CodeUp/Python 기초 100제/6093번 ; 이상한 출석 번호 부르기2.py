# https://codeup.kr/problem.php?id=6093

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 줄에 번호를 부른 횟수 n을 입력합니다.
# 정수형으로 변환합니다.
n = int(stdin.readline())
# 두 번째 줄에 n개의 랜덤 번호들을 공백을 사이에 두고 순서대로 입력합니다.
# 각각 정수형으로 변환하고 리스트 변수에 넣어줍니다.
nums = list(map(int, stdin.readline().split()))
# 랜덤 번호의 개수인 nums의 길이를 저장하는 변수를 선언합니다.
nums_len = len(nums)

# nums의 인덱스를 역순으로 반복합니다.
for idx in range(nums_len - 1, -1, -1):
    # nums에서 현재 인덱스의 값을 출력하고, 한 칸 띄어줍니다.
    print(nums[idx], end=' ')