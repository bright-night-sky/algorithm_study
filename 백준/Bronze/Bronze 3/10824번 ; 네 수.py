# https://www.acmicpc.net/problem/10824

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 네 자연수 A, B, C, D를 공백으로 구분해 입력합니다.
# 1 <= A, B, C, D <= 1,000,000
A, B, C, D = stdin.readline().rstrip().split(' ')
# A의 뒤에 B를 붙이고 정수형으로 변환한 값을 저장하는 변수를 선언합니다.
num1 = int(A + B)
# C의 뒤에 D를 붙이고 정수형으로 변환한 값을 저장하는 변수를 선언합니다.
num2 = int(C + D)

# num1과 num2의 합을 출력합니다.
print(num1 + num2)