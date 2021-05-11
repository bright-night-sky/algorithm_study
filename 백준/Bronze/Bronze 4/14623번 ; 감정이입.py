# https://www.acmicpc.net/problem/14623

# 첫 번째 줄에 이진수 B1 입력
B1 = '0b' + input()
# 두 번째 줄에 이진수 B2 입력
B2 = '0b' + input()
# 두 이진수의 길이는 1 이상 30 이하의 자연수
# 두 이진수들이 1로 시작하는 것이 보장됨

# 두 이진수를 십진수로 변경
ten_B1 = int(B1, 2)
ten_B2 = int(B2, 2)

# 두 수의 곱을 저장하는 변수
multiple = ten_B1 * ten_B2

# 두 수의 곱의 결과를 이진수로 변환하고 앞의 '0b'를 떼서 변수에 저장
result = bin(multiple)[2:]

# 결과를 출력
print(result)