# https://codeup.kr/problem.php?id=1276

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 자연수 n을 입력합니다.
# n <= 12
# int형으로 변환합니다.
n = int(stdin.readline())
# 팩토리얼 n인 n! 값을 저장할 변수를 선언합니다.
# 곱셈 누적 값이므로 1로 초기화합니다.
n_factorial = 1

# 2부터 n까지 반복해봅니다.
for num in range(2, n + 1):
    # n_factorial에 현재 숫자를 곱해줍니다.
    n_factorial *= num

# n! 값인 n_factorial의 값을 출력합니다.
print(n_factorial)