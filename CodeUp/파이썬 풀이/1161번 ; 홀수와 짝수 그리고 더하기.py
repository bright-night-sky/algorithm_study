# https://codeup.kr/problem.php?id=1161

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 정수 두 개를 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
num1, num2 = map(int, stdin.readline().split())
# 첫 번째 정수의 홀짝 여부, 두 번째 정수의 홀짝 여부, 두 정수의 합의 홀짝 여부를 저장할 변수를 선언합니다.
# 처음에는 모두 None으로 초기화합니다.
num1_type, num2_type, result_type = None, None, None

# 첫 번째 정수인 num1의 값이 홀수라면
if num1 % 2 == 1:
    # num1_type에 홀수를 저장합니다.
    num1_type = '홀수'
# 그 외의 경우, 즉, 첫 번째 정수인 num1의 값이 짝수라면
else:
    # num1_type에 짝수를 저장합니다.
    num1_type = '짝수'

# 두 번째 정수인 num2의 값이 홀수라면
if num2 % 2 == 1:
    # num2_type에 홀수를 저장합니다.
    num2_type = '홀수'
# 그 외의 경우, 즉, 두 번째 정수인 num2의 값이 짝수라면
else:
    # num2_type에 짝수를 저장합니다.
    num2_type = '짝수'

# 첫 번째 정수와 두 번째 정수의 홀짝 여부가 같다면
if num1_type == num2_type:
    # 두 정수의 합은 짝수이므로 result_type에 짝수를 저장합니다.
    result_type = '짝수'
# 그 외의 경우, 즉, 첫 번째 정수와 두 번째 정수의 홀짝 여부가 다르다면
else:
    # 두 정수의 합은 홀수이므로 result_type에 홀수를 저장합니다.
    result_type = '홀수'

# 출력 형식에 맞게 첫 번째 정수, 두 번째 정수, 두 정수의 합의 홀짝 여부를 출력합니다.
print(f'{num1_type}+{num2_type}={result_type}')