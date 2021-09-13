# https://codeup.kr/problem.php?id=1274

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 2 이상의 자연수를 입력합니다.
# int형으로 변환합니다.
num = int(stdin.readline())
# 소수를 판별하기 위해 입력한 자연수를 2부터 입력한 자연수의 제곱근 이하의 자연수까지 나누어 봐야하므로
# 입력한 자연수의 제곱근을 구해 int형으로 변환하고 1을 더한 제한값을 구해 변수에 저장합니다.
limit = int(num ** 0.5) + 1

# 2부터 limit - 1 값인 입력한 자연수의 제곱근 이하의 자연수까지 반복해봅니다.
for divisor in range(2, limit):
    # 입력한 자연수를 현재 숫자로 나누었을 때 나머지가 0이라면
    if num % divisor == 0:
        # 입력한 자연수는 소수가 아니므로 문자열 not prime을 출력합니다.
        print('not prime')
        # 소수인지 아닌지 판별했으므로 반복문을 탈출합니다.
        break
# 입력한 자연수를 2부터 limit - 1까지 나누었을 때 나머지가 0인 경우가 없다면
else:
    # 입력한 자연수는 소수이므로 문자열 prime을 출력합니다.
    print('prime')