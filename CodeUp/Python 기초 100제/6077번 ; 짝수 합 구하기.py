# https://codeup.kr/problem.php?id=6077

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 1 ~ 100 중 정수 1개를 입력합니다.
num = int(stdin.readline())
# 1부터 입력한 정수까지 짝수만 합한 값을 저장할 변수를 선언합니다.
# 0으로 초기화합니다.
even_sum = 0

# 1부터 num의 값까지 반복해봅니다.
for cur_num in range(1, num + 1):
    # 현재 수가 짝수라면
    if cur_num % 2 == 0:
        # even_sum에 현재 수를 더해줍니다.
        even_sum += cur_num

# 짝수만 합한 값인 even_sum의 값을 출력합니다.
print(even_sum)