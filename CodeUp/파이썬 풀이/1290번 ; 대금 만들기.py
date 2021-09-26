# https://codeup.kr/problem.php?id=1290

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 대나무의 원래 길이인 n을 입력합니다.
# int형으로 변환합니다.
n = int(stdin.readline())
# 좋은 소리를 내는 서로 다른 대나무 조각의 수를 저장할 변수를 선언합니다.
# 0으로 초기화합니다.
daegeum_cnt = 0
# n의 제곱근의 정수 부분에 1을 더한 값을 저장한 변수를 선언합니다.
limit = int(n ** 0.5) + 1

# 좋은 소리를 내는 서로 다른 대나무 조각의 수는 n의 약수 개수에서 n 자기 자신만 뺀 개수입니다.
# 1부터 limit - 1 값까지 반복해봅니다.
for divisor in range(1, limit):
    # 16의 약수 중 4처럼 n의 약수 중 제곱근인 약수인 경우입니다.
    # n을 현재 숫자로 나누었을 때 나머지가 0이며, 현재 숫자와 n을 현재 숫자로 나누었을 때 몫이 같다면
    if n % divisor == 0 and divisor == n // divisor:
        # daegeum_cnt에 1을 더합니다.
        daegeum_cnt += 1
    # n의 약수 중 제곱근이 아닌 약수인 경우입니다.
    # n을 현재 숫자로 나누었을 때 나머지가 0이라면
    elif n % divisor == 0:
        # daegeum_cnt에 2를 더합니다.
        daegeum_cnt += 2

# n의 약수 중 n 자기 자신은 개수에서 빼야하므로 daegeum_cnt에 1을 뺀 값을 출력합니다.
print(daegeum_cnt - 1)
