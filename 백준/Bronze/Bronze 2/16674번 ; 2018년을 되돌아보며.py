# https://www.acmicpc.net/problem/16674

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 번째 줄에 양의 정수 N을 입력합니다.
# 1 <= N <= 1,000,000,000
# 맨 끝의 \n은 떼어줍니다.
N = stdin.readline().rstrip()
# N의 길이를 저장하는 변수를 선언합니다.
N_len = len(N)

# N에서 2의 개수를 저장하는 변수를 선언합니다.
two_cnt = N.count('2')
# N에서 0의 개수를 저장하는 변수를 선언합니다.
zero_cnt = N.count('0')
# N에서 1의 개수를 저장하는 변수를 선언합니다.
one_cnt = N.count('1')
# N에서 8의 개수를 저장하는 변수를 선언합니다.
eight_cnt = N.count('8')

# N이 2, 0, 1, 8로만 이루어져 있다면
# 즉, N의 길이와 2, 0, 1, 8의 개수의 합이 같은 경우
if two_cnt + zero_cnt + one_cnt + eight_cnt == N_len:
    # 일단 N은 관련 있는 수에 속합니다.
    # 관련 있는 수 중에서 2, 0, 1, 8을 모두 포함하는 경우
    # 즉 2, 0, 1, 8의 개수가 각각 1개 이상인 경우
    if two_cnt >= 1 and zero_cnt >= 1 and one_cnt >= 1 and eight_cnt >= 1:
        # 일단 N은 밀접한 수에 속합니다.
        # 밀접한 수 중 2, 0, 1, 8의 개수가 모두 똑같은 경우
        if two_cnt == zero_cnt and zero_cnt == one_cnt and one_cnt == eight_cnt:
            # N은 묶여있는 수이므로 8을 출력합니다.
            print(8)
        # 묶여있는 수까지는 안되는 경우
        else:
            # 밀접한 수이므로 2를 출력합니다.
            print(2)
    # 밀접한 수까지는 안되는 경우
    else:
        # 관련 있는 수이므로 1을 출력합니다.
        print(1)
# 관련없는 수도 아니라면
else:
    # 관련 없는 수이므로 0을 출력합니다.
    print(0)