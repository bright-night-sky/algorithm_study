# https://codeup.kr/problem.php?id=1109

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 이름을 입력합니다.
# 맨 끝의 \n은 떼어줍니다.
name = stdin.readline().rstrip()
# 다음 줄에 나이를 입력합니다.
# 정수형으로 변환합니다.
age = int(stdin.readline())
# 다음 줄에 부서코드 A, B, C 중 하나를 입력합니다.
# 맨 끝의 \n은 떼어줍니다.
department_code = stdin.readline().rstrip()
# 다음 줄에 보안키를 입력합니다.
# 실수형으로 변환합니다.
security_key = float(stdin.readline())

# 입력한 이름, 나이, 부서코드, 보안키를 한 줄에 하나씩 입력한 순서대로 출력합니다.
print(name)
print(age)
print(department_code)
print(security_key)