# https://www.acmicpc.net/problem/5597

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 학생들의 출석번호 1부터 30까지를 리스트 변수에 저장합니다.
numbers = [number for number in range(1, 31)]

# 과제 제출자들은 28명이므로 28번 반복합니다.
for number in range(28):
    # 제출자의 출석번호를 하나씩 입력합니다.
    n = int(stdin.readline())

    # 제출자의 출석번호를 numbers에서 지웁니다.
    numbers.remove(n)

# 출력 형식에 맞게 과제를 제출하지 않은 학생의 출석번호를 작은 것부터 출력합니다.
print(numbers[0])
print(numbers[1])