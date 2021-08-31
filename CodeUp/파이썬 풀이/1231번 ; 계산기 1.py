# https://codeup.kr/problem.php?id=1231

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 더하기, 빼기, 곱하기, 나누기 연산자들 +, -, *, /가 들어있는 리스트 변수를 선언합니다.
operators = ['+', '-', '*', '/']
# 연산식 한 줄을 입력합니다.
# 맨 끝의 \n은 떼어줍니다.
operation_expression = stdin.readline().rstrip()
# 정수 2개와 연산자를 연산식에서 분리해 저장할 변수들 선언합니다.
# 각각 None으로 초기화합니다.
num1, num2, operator = None, None, None

# operators에서 연산자 하나씩 반복해봅니다.
for oper in operators:
    # 현재 연산자가 입력한 연산식에 들어있다면
    if oper in operation_expression:
        # operator에 현재 연산자를 저장합니다.
        operator = oper
        # 입력한 연산식에서 현재 연산자를 기준으로 분리해 각 피연산자들을
        # 각각 int형으로 변환하고 변수에 저장합니다.
        num1, num2 = map(int, operation_expression.split(operator))

# 연산식의 연산자가 +라면
if operator == '+':
    # 두 피연산자들의 덧셈 결과를 출력합니다.
    print(num1 + num2)
# 연산식의 연산자가 +라면
elif operator == '-':
    # 두 피연산자들의 뺄셈 결과를 출력합니다.
    print(num1 - num2)
# 연산식의 연산자가 +라면
elif operator == '*':
    # 두 피연산자들의 곱셈 결과를 출력합니다.
    print(num1 * num2)
# 그 외의 경우인 연산식의 연산자가 /라면
else:
    # 두 피연산자들의 나눗셈 결과를 출력합니다.
    # 나눗셈 결과는 소수 둘째 자리까지 출력합니다.
    print('%.2f' % (num1 / num2))