# https://codeup.kr/problem.php?id=1259

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 자연수 n을 입력합니다.
# int형으로 변환합니다.
n = int(stdin.readline())
# 1부터 n까지의 짝수의 합을 저장할 변수를 선언합니다.
# 0으로 초기화합니다.
even_sum = 0

# 1부터 n까지 반복해봅니다.
for num in range(1, n + 1):
    # 현재 숫자가 짝수라면, 즉, 현재 숫자를 2로 나누었을 때 나머지가 0이라면
    if num % 2 == 0:
        # even_sum에 현재 숫자를 더해줍니다.
        even_sum += num

# 1부터 n까지의 짝수의 합인 even_sum의 값을 출력합니다.
print(even_sum)