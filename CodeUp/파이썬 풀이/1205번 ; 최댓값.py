# https://codeup.kr/problem.php?id=1205

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 실수 a, b를 공백으로 구분해 입력합니다.
# 각각 float형으로 변환합니다.
a, b = map(float, stdin.readline().split())
# a+b, a-b, a*b, a/b, a^b, b-a, b/a, b^a를 계산하고 리스트 변수에 넣어줍니다.
# b+a, b*a는 각각 a+b, a*b와 같으므로 굳이 계산할 필요가 없습니다.
operations = [a + b, a - b, a * b, a / b, a ** b, b - a, b / a, b ** a]
# operations에서의 최댓값을 구하고, 소수점 이하 6자리로 만들어 변수에 저장합니다.
max_num = "%.6f" % max(operations)

# 소수점 이하 6자리인 최댓값을 출력합니다.
print(max_num)