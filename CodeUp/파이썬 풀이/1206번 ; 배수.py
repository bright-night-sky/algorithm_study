# https://codeup.kr/problem.php?id=1206

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 두 자연수 a, b를 공백으로 구분해 입력합니다.
# 각각 int형으로 변환합니다.
a, b = map(int, stdin.readline().split())

# b가 a의 배수이면, 즉 b를 a로 나누었을 때 나머지가 0이라면
if b % a == 0:
    # b를 a로 나눈 몫인 출력 형식의 x를 구하고
    # 출력 형식 'a*x=b'에 맞게 배수 관계를 출력합니다.
    print(f'{a}*{b // a}={b}')
# a가 b의 배수이면, 즉 a를 b로 나누었을 때 나머지가 0이라면
elif a % b == 0:
    # a를 b로 나눈 몫인 출력 형식의 x를 구하고
    # 출력 형식 'b*x=a'에 맞게 배수 관계를 출력합니다.
    print(f'{b}*{a // b}={a}')
# 그 외의 경우에는, 즉, a와 b가 서로 배수가 아니라면
else:
    # 문자열 'none'을 출력합니다.
    print('none')