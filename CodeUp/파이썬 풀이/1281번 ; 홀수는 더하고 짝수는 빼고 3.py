# https://codeup.kr/problem.php?id=1281

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 두 자연수 a, b를 공백으로 구분해 입력합니다.
# 각각 int형으로 변환합니다.
a, b = map(int, stdin.readline().split())
# 홀수는 더하고 짝수는 뺀 값을 저장할 변수를 선언합니다.
# 0으로 초기화합니다.
sum_result = 0
# 홀수는 더하고 짝수는 뺀 식을 저장할 변수를 선언합니다.
# 빈 문자열로 초기화합니다.
expression = ''

# a부터 b까지 반복해봅니다.
for num in range(a, b + 1):
    # 현재 숫자가 홀수라면 즉, 현재 숫자를 2로 나누었을 때 나머지가 1이라면
    if num % 2 == 1:
        # sum_result에 현재 숫자를 더해줍니다.
        sum_result += num
        # expression에 '+(현재 숫자)' 문자열을 넣어줍니다.
        expression += f'+{num}'
    # 그 외의 경우인 현재 숫자가 짝수라면 즉, 현재 숫자를 2로 나누었을 때 나머지가 0이라면
    else:
        # sum_result에 현재 숫자를 빼줍니다.
        sum_result -= num
        # expression에 '-(현재 숫자)' 문자열을 넣어줍니다.
        expression += f'-{num}'

# 맨 처음 연산하는 숫자인 a의 값이 홀수라면 즉, a의 값을 2로 나누었을 때 나머지가 1이라면
if a % 2 == 1:
    # 현재 expression 변수에 저장되어 있는 문자열 맨 앞에는 '+' 기호가 있습니다.
    # expression 맨 앞에 있는 '+'는 없애줍니다.
    expression = expression[1:]

# a부터 b값까지 홀수는 더하고 짝수는 뺀 식과 결과를 출력 형식에 맞게 출력합니다.
print(f'{expression}={sum_result}')