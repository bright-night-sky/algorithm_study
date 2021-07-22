# https://codeup.kr/problem.php?id=6045

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 정수 3개를 공백으로 구분해 입력합니다.
# 각각 정수형으로 만들어줍니다.
nums = map(int, stdin.readline().split(' '))
# 정수 3개의 합을 저장하는 변수를 선언합니다.
num_sum = sum(nums)
# 정수 3개의 평균을 저장하는 변수를 선언합니다.
# 소수점 셋째 자리에서 반올림하고 소수점 둘째 자리까지 있는 실수로 만들어줍니다.
num_avg = format(round(num_sum / 3, 2), '.2f')

# 합과 평균을 공백을 두고 출력합니다.
print(num_sum, num_avg)