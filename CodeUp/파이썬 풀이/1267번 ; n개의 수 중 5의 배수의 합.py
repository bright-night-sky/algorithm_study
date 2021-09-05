# https://codeup.kr/problem.php?id=1267

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 수의 개수인 정수 n을 입력합니다.
# 1 <= n <= 1,000
n = stdin.readline()
# 둘째 줄에 n개의 자연수들을 공백으로 구분해 입력합니다.
# 각 정수는 1 ~ 1,000입니다.
# 각각 int형으로 변환합니다.
nums = map(int, stdin.readline().split())
# n개의 자연수들 중 5의 배수의 합을 저장할 변수를 선언합니다.
# 0으로 초기화합니다.
five_multiple_sum = 0

# nums에 있는 정수들을 하나씩 반복해봅니다.
for num in nums:
    # 현재 숫자가 5의 배수라면, 즉 5로 나누었을 때 나머지가 0이라면
    if num % 5 == 0:
        # five_multiple_sum에 현재 숫자를 더해줍니다.
        five_multiple_sum += num

# 5의 배수의 합인 five_multiple_sum의 값을 출력합니다.
print(five_multiple_sum)