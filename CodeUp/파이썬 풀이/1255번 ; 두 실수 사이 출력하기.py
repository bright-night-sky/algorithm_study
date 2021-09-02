# https://codeup.kr/problem.php?id=1255

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 두 실수 a, b를 공백으로 구분해 입력합니다.
# a <= b
# 각각 float형으로 변환합니다.
a, b = map(float, stdin.readline().split())

# a가 b 이하면 계속 반복하는 반복문을 만듭니다.
while a <= b:
    # a를 소수점 둘째 자리까지 출력합니다.
    print('%.2f' % a)

    # a에 0.01을 더해줍니다.
    a += 0.01