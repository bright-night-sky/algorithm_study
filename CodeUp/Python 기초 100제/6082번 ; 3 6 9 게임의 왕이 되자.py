# https://codeup.kr/problem.php?id=6082

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 1 ~ 29 중 3 6 9 게임의 마지막 숫자 1개를 입력합니다.
# 정수형으로 변환합니다.
end_num = int(stdin.readline())

# 1부터 end_num의 값까지 반복합니다.
for num in range(1, end_num + 1):
    # 3 6 9 게임을 최대 29까지만 진행하므로
    # 일의 자리 숫자가 3, 6, 9인지만 생각하면 됩니다.
    # 현재 숫자의 1의 자리 숫자를 저장하는 변수를 선언합니다.
    remainder = num % 10

    # 1의 자리 숫자가 3, 6, 9 중 하나라도 속한다면
    if remainder in [3, 6, 9]:
        # X를 출력하고 한 칸 띄어줍니다.
        print('X', end=' ')
    # 그 외의 숫자라면
    else:
        # 현재 숫자를 출력하고 한 칸 띄어줍니다.
        print(num, end=' ')