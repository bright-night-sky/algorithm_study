# https://www.acmicpc.net/problem/1356

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 수 N을 입력합니다.
# 2,147,483,647보다 작거나 같은 자연수입니다.
# 맨 끝의 \n은 떼어줍니다.
N = stdin.readline().rstrip()
# N의 길이를 저장하는 변수를 선언합니다.
N_len = len(N)
# N이 유진수인지 아닌지를 저장하는 변수를 선언합니다.
# 처음에는 유진수가 아니라는 뜻인 NO로 초기화합니다.
is_yujin = "NO"

# N을 두 부분으로 나누는 기준을 1부터 N의 길이까지 반복합니다.
for divide_idx in range(1, N_len):
    # 앞부분을 저장하는 변수를 선언합니다.
    # 각 숫자들을 정수형으로 변환합니다.
    front = map(int, N[:divide_idx])
    # 뒷부분을 저장하는 변수를 선언합니다.
    # 각 숫자들을 정수형으로 변환합니다.
    back = map(int, N[divide_idx:])
    # 앞부분의 곱을 저장할 변수를 선언합니다.
    # 1로 초기화합니다.
    front_multiple = 1
    # 뒷부분의 곱을 저장할 변수를 선언합니다.
    # 1로 초기화합니다.
    back_multiple = 1

    # 앞부분의 곱을 구해봅니다.
    for number in front:
        front_multiple *= number

    # 뒷부분의 곱을 구해봅니다.
    for number in back:
        back_multiple *= number

    # 앞부분의 곱과 뒷부분의 곱이 같다면
    if front_multiple == back_multiple:
        # N은 유진수이므로 is_yujin에 YES를 저장합니다.
        is_yujin = "YES"
        # 유진수가 확정되었으므로 반복문을 탈출합니다.
        break

# N이 유진수인지 아닌지를 출력합니다.
print(is_yujin)