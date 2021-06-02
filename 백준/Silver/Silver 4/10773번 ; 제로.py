# https://www.acmicpc.net/problem/10773

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫 번째 줄에 정수 K를 입력합니다.
# 1 <= K <= 100,000
# 정수형으로 변환합니다.
K = int(stdin.readline())
# 정수들을 저장할 리스트 변수를 선언합니다.
numbers = []

# K번 반복합니다.
for number_idx in range(K):
    # 정수를 1개 입력합니다.
    # 정수 0에서 1,000,000 사이의 값입니다.
    # 정수형으로 변환합니다.
    number = int(stdin.readline())

    # 입력한 숫자가 0이 아니라면
    if number != 0:
        # numbers 리스트 변수에 입력한 숫자를 넣어줍니다.
        numbers.append(number)
    # 입력한 숫자가 0이라면
    else:
        # numbers에 있는 숫자 중 맨 끝에 있는 숫자를 빼냅니다.
        numbers.pop()

# numbers에 있는 숫자의 합을 출력합니다.
print(sum(numbers))