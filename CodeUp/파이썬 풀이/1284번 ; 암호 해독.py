# https://codeup.kr/problem.php?id=1284

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 매개변수 num의 값이 소수인지를 판별하는 함수를 만들어봅니다.
def isPrime(num):
    # num의 값이 소수인지를 판별하기 위해 2부터 num의 제곱근까지의 값이 필요합니다.
    # 그래서 num의 제곱근의 정수 부분만 가져오고 그 값에 1을 더한 값을 변수 limit에 저장합니다.
    limit = int(num ** 0.5) + 1

    # 2부터 limit - 1 값까지 반복해봅니다.
    for i in range(2, limit):
        # num의 값이 현재 숫자로 나누어 떨어진다면, 즉 num의 값을 현재 숫자로 나누었을 때 나머지가 0이라면
        if num % i == 0:
            # num의 값은 소수가 아니므로 False를 반환합니다.
            return False
    # 2부터 limit - 1 값까지 반복했는데 나누어 떨어진 숫자가 하나도 없다면
    else:
        # num의 값은 소수이므로 True를 반환합니다.
        return True


# 어떤 수 n을 입력합니다.
# 1 <= n <= 10,000,000
# int형으로 변환합니다.
n = int(stdin.readline())

# 어떤 수 n이 두 소수의 곱으로 나타낼 수 있는지 여부는 2부터 n의 제곱근까지의 수로 나누어보고,
# 나눈 수와 나누고 나온 값이 둘 다 소수인지 판별하면 됩니다.

# 입력한 n의 제곱근에 1을 더한 값을 구해 변수 n_limit에 저장합니다.
n_limit = int(n ** 0.5) + 1

# 2부터 n_limit - 1 값까지 반복해봅니다.
for num in range(2, n_limit):
    # n의 값을 현재 숫자로 나누었을 때 나머지가 0이고,
    # 현재 숫자와 n을 현재 숫자로 나누었을 때 몫이 모두 소수라면
    if n % num == 0 and isPrime(num) and isPrime(n // num):
        # 입력한 n은 두 소수의 곱인 현재 숫자 num과 n // num으로 나타낼 수 있습니다.
        # 따라서 num과 n // num의 값을 공백으로 구분해 출력합니다.
        print(num, n // num)
        # n을 두 소수의 곱으로 나타냈으므로 반복문을 탈출합니다.
        break
# 2부터 n_limit - 1 값까지 반복해도 중간에 반복문을 탈출하지 않았다면
else:
    # n을 두 소수의 곱으로 나타낼 수 없으므로 문자열 'wrong number'을 출력합니다.
    print('wrong number')
