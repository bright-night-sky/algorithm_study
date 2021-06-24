# https://www.acmicpc.net/problem/17362

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 번째 줄에 자연수 n을 입력합니다.
# 1 <= n <= 10^9
# 정수형으로 변환합니다.
n = int(stdin.readline())

# 1, 9, 17, ...마다 엄지에 있으므로 이를 기준으로 잡아봅니다.
# 입력한 n에서 1을 뺀 뒤 8로 나눈 나머지를 저장하는 변수를 선언합니다.
remain = (n - 1) % 8

# 나머지가 0이라면
if remain == 0:
    # 엄지에 있는 숫자이므로 1을 출력합니다.
    print(1)
# 나머지가 1 혹은 7이라면
elif remain == 1 or remain == 7:
    # 검지에 있는 숫자이므로 2를 출력합니다.
    print(2)
# 나머지가 2 혹은 6이라면
elif remain == 2 or remain == 6:
    # 중지에 있는 숫자이므로 3을 출력합니다.
    print(3)
# 나머지가 3 혹은 5이라면
elif remain == 3 or remain == 5:
    # 약지에 있는 숫자이므로 4를 출력합니다.
    print(4)
# 나머지가 4라면
elif remain == 4:
    # 새끼손가락에 있는 숫자이므로 5를 출력합니다.
    print(5)