# https://codeup.kr/problem.php?id=1268

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 자연수인 수의 개수 n을 입력합니다.
n = stdin.readline()
# 그 다음 줄에 n개의 자연수들을 공백으로 구분해 입력합니다.
# 각각 int형으로 변환합니다.
nums = map(int, stdin.readline().split())
# n개의 자연수들 중 짝수의 개수를 저장할 변수를 선언합니다.
# 0으로 초기화합니다.
even_cnt = 0

# nums에 들어 있는 자연수들을 하나씩 반복해봅니다.
for num in nums:
    # 현재 자연수가 짝수라면, 즉 현재 자연수를 2로 나누었을 때 나머지가 0이라면
    if num % 2 == 0:
        # even_cnt에 1을 더해줍니다.
        even_cnt += 1

# 짝수의 개수인 even_cnt의 값을 출력합니다.
print(even_cnt)