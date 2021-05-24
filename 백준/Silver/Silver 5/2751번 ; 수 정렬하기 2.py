# https://www.acmicpc.net/problem/2751

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 수의 개수 N을 입력합니다.
# 1 <= N <= 1,000,000
# 정수형으로 변환합니다.
N = int(stdin.readline())

# 숫자들을 저장할 리스트 변수를 선언합니다.
# N개의 None으로 초기화해줍니다.
numbers = [None] * N

# 수의 개수 N만큼 반복합니다.
for number_idx in range(N):
    # 숫자를 하나 입력하고 정수형으로 변환한 뒤 numbers에 넣어줍니다.
    numbers[number_idx] = int(stdin.readline())

# numbers에 있는 숫자들을 오름차순으로 정렬해줍니다.
numbers.sort()

# numbers에 있는 숫자들을 한 줄에 하나씩 출력합니다.
for number in numbers:
    print(number)