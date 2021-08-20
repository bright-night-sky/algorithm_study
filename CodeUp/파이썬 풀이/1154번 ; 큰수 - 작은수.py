# https://codeup.kr/problem.php?id=1154

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 두 정수를 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
num1, num2 = map(int, stdin.readline().split())

# num1의 값이 num2의 값보다 크다면
if num1 > num2:
    # 큰 수인 num1의 값에서 작은 수인 num2의 값을 뺀 결과를 출력합니다.
    print(num1 - num2)
# 그 외의 경우, 즉, num2의 값이 num1의 값보다 크거나 같다면
else:
    # 큰 수인 num2의 값에서 작은 수인 num1의 값을 뺀 결과를 출력합니다.
    print(num2 - num1)