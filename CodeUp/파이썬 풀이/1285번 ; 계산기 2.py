# https://codeup.kr/problem.php?id=1285

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 정수와 사칙연산 기호가 식을 입력합니다.
# 맨 끝의 \n은 떼어줍니다.
expression = stdin.readline().rstrip()
# 정수를 저장할 변수를 선언합니다.
operand = ''
# 사칙연산 기호와 '=' 기호가 있는 리스트 변수를 선언합니다.
operations = ['+', '-', '*', '/', '=']
# 사칙연산 기호를 저장할 변수를 선언합니다.
# None으로 초기화합니다.
operation = None
# 연산한 결과를 저장할 변수를 선언합니다.
# 0으로 초기화합니다.
result = 0

# 식을 한 글자씩 반복해봅니다.
for char in expression:
    # 현재 글자가 사칙연산 기호 혹은 '='이라면
    if char in operations:
        # operand에 저장되어 있는 숫자 형태의 문자열을 int형으로 변환해서 저장합니다.
        operand = int(operand)

        # operation에 어떠한 사칙연산 기호도 저장되어 있지 않다면
        # 한 글자씩 반복하면서 처음 만난 사칙연산 기호라면
        if operation is None:
            # 이전까지 아무 것도 연산할 것이 없었으므로 result에 operand의 값을 그대로 저장합니다.
            result = operand
        # operation에 '+'가 저장되어 있다면
        elif operation == '+':
            # result의 값에 operand의 값을 더해줍니다.
            result += operand
        # operation에 '-'가 저장되어 있다면
        elif operation == '-':
            # result의 값에 operand의 값을 빼줍니다.
            result -= operand
        # operation에 '*'가 저장되어 있다면
        elif operation == '*':
            # result의 값에 operand의 값을 곱해줍니다.
            result *= operand
        # operation에 '/'가 저장되어 있다면
        elif operation == '/':
            # result의 값에 operand의 값을 나눈 몫을 저장합니다.
            result //= operand

        # operand에는 다시 빈 문자열을 저장합니다.
        operand = ''
        # operation에 연산자인 현재 문자를 저장합니다.
        operation = char
    # 하나의 피연산자를 변수에 저장하기 위한 부분입니다.
    # 그 외의 경우인 현재 문자가 숫자 형태의 문자라면
    else:
        # operand에 현재 문자인 숫자 형태의 문자를 넣어줍니다.
        operand += char

# 맨 끝의 '='까지 반복문을 모두 돌고 나면
# 식을 연산한 결과인 result의 값을 출력합니다.
print(result)