# https://www.acmicpc.net/problem/5613

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 사칙연산을 계속 누적하면서 값을 저장할 변수를 선언합니다.
# 첫 번째 줄에 입력하는 수로 초기화합니다.
# 입력하는 숫자는 10^8 이하의 양의 정수입니다.
# 계산 중 결과는 0 또는 음수가 될 수 있지만
# -10^8 ~ 10^8 범위 이내입니다.
result = int(stdin.readline())

# 입력한 연산자를 저장하는 변수를 선언합니다.
operator = ''

# = 연산자를 입력할 때까지 반복합니다.
while True:
    # 숫자 혹은 연산자를 입력합니다.
    num_or_operator = stdin.readline().rstrip()

    # 입력한 값이 =이라면
    if num_or_operator == '=':
        # 계산 결과를 출력합니다.
        print(result)
        # 반복문을 탈출해 종료합니다.
        break
    # 입력한 값이 =이 아닐 때
    else:
        # 입력한 값이 +라면
        if num_or_operator == '+':
            # operator에 +를 저장합니다.
            operator = '+'
        # 입력한 값이 -라면
        elif num_or_operator == '-':
            # operator에 -를 저장합니다.
            operator = '-'
        # 입력한 값이 *라면
        elif num_or_operator == '*':
            # operator에 *를 저장합니다.
            operator = '*'
        # 입력한 값이 /라면
        elif num_or_operator == '/':
            # operator에 /를 저장합니다.
            operator = '/'
        # 입력한 값이 숫자라면
        else:
            # 정수형으로 변환해줍니다.
            num_or_operator = int(num_or_operator)

            # 이 숫자 이전에 입력한 연산자가 +라면
            if operator == '+':
                # result에 현재 숫자를 더해줍니다.
                result += num_or_operator
            # 이 숫자 이전에 입력한 연산자가 -라면
            elif operator == '-':
                # result에 현재 숫자를 빼줍니다.
                result -= num_or_operator
            # 이 숫자 이전에 입력한 연산자가 *라면
            elif operator == '*':
                # result에 현재 숫자를 곱해줍니다.
                result *= num_or_operator
            # 이 숫자 이전에 입력한 연산자가 /라면
            elif operator == '/':
                # result에 현재 숫자를 나눠줍니다.
                # 이 때 소수점 부분은 버립니다.
                result = int(result / num_or_operator)