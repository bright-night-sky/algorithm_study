# https://www.acmicpc.net/problem/14614

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 입력의 첫째 줄에 A, B, C를 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
A, B, C = map(int, stdin.readline().split(' '))

# A에 B를 C번 XOR했을 때
# A에 B로 한 번 XOR 연산한 뒤, 또 B로 XOR 연산하면 그대로 A가 나옵니다.
# 따라서 연산 횟수를 짝수일 때, 홀수일 때로 나누어 생각하면 됩니다.

# C가 짝수라면
if C % 2 == 0:
    # A 그대로 출력합니다.
    print(A)
# C가 홀수라면
else:
    # A에 B로 XOR 연산을 한 결과를 출력합니다.
    print(A ^ B)