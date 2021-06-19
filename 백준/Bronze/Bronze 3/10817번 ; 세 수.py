# https://www.acmicpc.net/problem/10817

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 세 정수 A, B, C를 공백으로 구분해 입력합니다.
# 1 <= A, B, C <= 100
# 각각 정수형으로 변환하고 리스트 변수에 넣어줍니다.
numbers = list(map(int, stdin.readline().split(' ')))

# numbers를 오름차순으로 정렬합니다.
numbers.sort()

# 두 번째로 큰 정수를 출력합니다.
print(numbers[1])