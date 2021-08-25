# https://codeup.kr/problem.php?id=1172

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 세 정수를 입력합니다.
# 각각 정수형으로 변환하고, 리스트 변수에 넣어줍니다.
nums = list(map(int, stdin.readline().split()))

# nums 내의 값들을 오름차순으로 정렬합니다.
nums.sort()

# nums 내의 숫자들을 하나씩 반복합니다.
for num in nums:
    # 현재 숫자를 출력하고, 다음 줄로 넘어가지 않고 마지막에 한 칸 띄어줍니다.
    print(num, end=' ')