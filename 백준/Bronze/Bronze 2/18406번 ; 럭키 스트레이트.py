# https://www.acmicpc.net/problem/18406

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 점수 N을 정수로 입력합니다.
# 10 <= N <- 99,999,999
# 맨 끝의 \n은 떼어주고 각 자릿수들을 정수형으로 변환한 튜플 변수로 만들어줍니다.
N = tuple(map(int, tuple(stdin.readline().rstrip())))
# N의 길이를 저장하는 변수를 선언합니다.
N_len = len(N)
# 자릿수를 기준으로 반으로 나눈 뒤, 왼쪽 부분의 합을 저장하는 변수를 선언합니다.
left_sum = sum(N[:N_len // 2])
# 자릿수를 기준으로 반으로 나눈 뒤, 오른쪽 부분의 합을 저장하는 변수를 선언합니다.
right_sum = sum(N[N_len // 2:])

# 왼쪽 부분과 오른쪽 부분이 같다면
if left_sum == right_sum:
    # 럭키 스트레이트를 사용할 수 있으므로 LUCKY를 출력합니다.
    print("LUCKY")
# 왼쪽 부분과 오른쪽 부분이 다르다면
else:
    # 럭키 스트레이트를 사용할 수 없으므로 READY를 출력합니다.
    print("READY")