# https://www.acmicpc.net/problem/10886

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 번째 줄에 설문조사를 한 사람의 수 N을 입력합니다.
# 1 <= N <= 101, 홀수입니다.
# 정수형으로 변환합니다.
N = int(stdin.readline())
# 준희가 귀엽다고 말한 사람의 수를 저장하는 변수를 선언합니다.
cute = 0
# 준희가 귀엽지 않다고 말한 사람의 수를 저장하는 변수를 선언합니다.
not_cute = 0

# 설문조사를 한 사람의 수 N만큼 반복합니다.
for opinion_idx in range(N):
    # 설문 조사에 어떤 의견을 표명했는지를 입력합니다.
    # 0은 준희가 귀엽지 않다는 뜻입니다.
    # 1은 준희가 귀엽다는 뜻입니다.
    # 맨 끝의 \n은 떼어줍니다.
    opinion = stdin.readline().rstrip()

    # 의견이 0이라면
    if opinion == '0':
        # not_cute에 1을 더해줍니다.
        not_cute += 1
    # 의견이 1이라면
    else:
        # cute에 1을 더해줍니다.
        cute += 1

# not_cute가 cute보다 크다면
if not_cute > cute:
    # Junhee is not cute!를 출력합니다.
    print('Junhee is not cute!')
# not_cute가 cute보다 작다면
elif not_cute < cute:
    # Junhee is cute!를 출력합니다.
    print('Junhee is cute!')