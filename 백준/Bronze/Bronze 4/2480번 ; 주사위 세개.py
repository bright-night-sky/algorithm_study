# https://www.acmicpc.net/problem/2480

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 3개의 눈을 빈 칸을 사이에 두고 입력합니다.
# 주사위의 눈이므로 1부터 6까지입니다.
# 각각 정수형으로 변환하고 리스트 변수에 넣어줍니다.
spots = list(map(int, stdin.readline().split(' ')))

# 3개의 눈이 모두 같다면
if spots[0] == spots[1] == spots[2]:
    # 10000 + (같은 눈) * 1000을 출력합니다.
    print(10000 + spots[0] * 1000)
# 3개의 눈이 모두 다르다면
elif spots[0] != spots[1] and spots[0] != spots[2] and spots[1] != spots[2]:
    # (가장 큰 눈) * 100을 출력합니다.
    print(max(spots) * 100)
# 3개의 눈 중 2개만 같다면
elif len(set(spots)) == 2:
    # 같은 눈을 저장할 변수를 선언합니다.
    same = None

    # 첫 번째 눈과 두 번째 눈이 같은 경우
    if spots[0] == spots[1]:
        # same에 첫 번째 눈의 값을 저장합니다.
        same = spots[0]
    # 첫 번째 눈과 세 번째 눈이 같은 경우
    elif spots[0] == spots[2]:
        # same에 첫 번째 눈의 값을 저장합니다.
        same = spots[0]
    # 두 번째 눈과 세 번째 눈이 같은 경우
    elif spots[1] == spots[2]:
        # same에 두 번째 눈의 값을 저장합니다.
        same = spots[1]

    # 1000 + (같은 눈인 same의 값) * 100을 출력합니다.
    print(1000 + same * 100)