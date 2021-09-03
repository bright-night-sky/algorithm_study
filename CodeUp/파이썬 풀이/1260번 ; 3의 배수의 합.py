# https://codeup.kr/problem.php?id=1260

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 두 자연수 a, b를 공백으로 구분해 입력합니다.
# a <= b
# 각각 int형으로 변환합니다.
a, b = map(int, stdin.readline().split())
# a부터 b까지의 3의 배수의 합을 저장할 변수를 선언합니다.
# 0으로 초기화합니다.
three_multiple_sum = 0

# a부터 b까지 반복해봅니다.
for num in range(a, b + 1):
    # 현재 숫자가 3의 배수라면, 즉, 현재 숫자를 3으로 나누었을 때 나머지가 0이라면
    if num % 3 == 0:
        # three_multiple_sum에 현재 숫자를 더해줍니다.
        three_multiple_sum += num

# a부터 b까지의 3의 배수의 합인 three_multiple_sum의 값을 출력합니다.
print(three_multiple_sum)