# https://www.acmicpc.net/problem/1252

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 두 개의 이진수를 공백으로 구분해 입력합니다.
bin_1, bin_2 = stdin.readline().rstrip().split(' ')

# 위에서 입력한 두 개의 이진수를 십진수로 각각 변경해줍니다.
dec_1 = int(bin_1, 2)
dec_2 = int(bin_2, 2)

# 변경된 십진수를 더해서 저장하는 변수를 선언합니다.
dec_sum = dec_1 + dec_2

# 더한 결과의 십진수를 이진수로 변환하고 출력 형식에 맞게 앞의 0b를 떼어줍니다.
bin_sum = bin(dec_sum)[2:]

# 더한 결과의 이진수를 출력합니다.
print(bin_sum)