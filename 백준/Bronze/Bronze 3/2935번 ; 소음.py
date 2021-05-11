# https://www.acmicpc.net/problem/2935

# 첫째 줄에 양의 정수 A를 입력합니다.
A = input()

# 둘째 줄에 연산자 + 또는 *를 입력합니다.
operator = input()

# 셋째 줄에 양의 정수 B를 입력합니다.
B = input()

# 입력받은대로의 A+B 또는 A*B를 저장하는 변수입니다.
result = eval(A + operator + B)

# 결과를 출력합니다.
print(result)
