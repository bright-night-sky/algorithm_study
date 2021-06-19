# https://www.acmicpc.net/problem/10818

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 정수의 개수 N을 입력합니다.
# 1 <= N <= 1,000,000
# 정수형으로 변환합니다.
N = int(stdin.readline())
# 둘째 줄에는 N개의 정수를 공백으로 구분해 입력합니다.
# 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수입니다.
# 각각 정수형으로 변환하고 리스트 변수에 넣어줍니다.
numbers = list(map(int, stdin.readline().split(' ')))

# numbers에서 최댓값을 저장하는 변수를 선언합니다.
max_num = max(numbers)
# numbers에서 최솟값을 저장하는 변수를 선언합니다.
min_num = min(numbers)

# 최솟값과 최댓값을 공백으로 구분해 출력합니다.
print(min_num, max_num)