# https://www.acmicpc.net/problem/2774

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 테스트 케이스의 개수 T를 입력합니다.
# 정수형으로 변환합니다.
T = int(stdin.readline())
# 0 ~ 9의 문자 형태를 저장하는 리스트 변수를 선언합니다.
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# 테스트 케이스의 개수 T만큼 반복합니다.
for test_case_idx in range(T):
    # 아름다운 정도를 알고 싶은 수 X를 입력합니다.
    # 1 <= X <= 1,000,000,000
    # 맨 끝의 \n은 떼어줍니다.
    X = stdin.readline().rstrip()
    # 입력한 X의 아름다운 정도를 저장할 변수를 선언합니다.
    beauty = 0

    # 0 ~ 9를 하나씩 반복해봅니다.
    for number in numbers:
        # X에서 현재 숫자가 있다면
        if X.find(number) != -1:
            # 아름다운 정도에 1을 더해줍니다.
            beauty += 1

    # X의 아름다운 정도를 출력합니다.
    print(beauty)