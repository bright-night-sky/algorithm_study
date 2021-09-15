# https://codeup.kr/problem.php?id=1279

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 두 자연수 a, b를 공백으로 구분해 입력합니다.
# 반드시 a는 b보다 같거나 작습니다.
# 각각 int형으로 변환합니다.
a, b = map(int, stdin.readline().split())
# 홀수는 더하고 짝수는 뺀 값을 저장할 변수를 선언합니다.
# 0으로 초기화합니다.
result = 0

# a부터 b까지 반복해봅니다.
for num in range(a, b + 1):
    # 현재 숫자가 홀수라면, 즉 현재 숫자를 2로 나누었을 때 나머지가 1이라면
    if num % 2 == 1:
        # result에 현재 숫자를 더해줍니다.
        result += num
    # 그 외의 경우인 현재 숫자가 짝수라면, 즉 현재 숫자를 2로 나누었을 때 나머지가 0이라면
    else:
        # result에 현재 숫자를 빼줍니다.
        result -= num

# 홀수는 더하고 짝수는 뺀 값인 result의 값을 출력합니다.
print(result)