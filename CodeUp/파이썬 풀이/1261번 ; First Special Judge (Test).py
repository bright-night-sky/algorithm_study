# https://codeup.kr/problem.php?id=1261

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 10개의 자연수들을 공백으로 구분해 입력합니다.
# 각각 int형으로 변환하고, 리스트 변수에 넣어줍니다.
ten_nums = list(map(int, stdin.readline().split()))

# ten_nums에 있는 숫자들을 하나씩 반복해봅니다.
for num in ten_nums:
    # 현재 숫자가 5의 배수라면, 즉, 현재 숫자를 5로 나누었을 때 나머지가 0이라면
    if num % 5 == 0:
        # 현재 숫자를 출력합니다.
        print(num)
        # 5의 배수인 숫자를 하나 출력했으므로 반복문을 탈출합니다.
        break
# 반복문을 끝까지 순회했다면
else:
    # 10개의 자연수들 중 5의 배수가 없었으므로, 0을 출력합니다.
    print(0)