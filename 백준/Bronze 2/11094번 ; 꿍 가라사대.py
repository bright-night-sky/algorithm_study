# https://www.acmicpc.net/problem/11094

# 첫째 줄에는 N을 입력합니다.
# 1 <= N <= 1,000
N = int(input())

# N개만큼의 명령을 반복해봅니다.
for order in range(N):
    # 한 개의 명령을 입력합니다.
    # 길이는 100이 넘지 않습니다.
    # 대소문자가 적절히 쓰여져 있으며 각 단어는 공백으로 구분되고 끝은 마침표로 끝납니다.
    order = input()

    # 명령문에서 Simon says가 시작되는 인덱스를 저장하는 변수를 선언합니다.
    Simon_says_index = order.find("Simon says")

    # 명령문에서 Simon says가 없다면
    if Simon_says_index == -1:
        # 다음 명령으로 넘어갑니다.
        continue
    # 명령문에서 Simon says가 있다면
    else:
        # 이후에 나오는 나머지 부분을 출력합니다.
        print(order[Simon_says_index+10:])
