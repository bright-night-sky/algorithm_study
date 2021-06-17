# https://www.acmicpc.net/problem/9437

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 0 하나만 입력할 때까지 반복합니다.
while True:
    # 두 정수를 입력하거나 0 하나를 입력합니다.
    # 맨 끝의 \n은 떼어줍니다.
    numbers = stdin.readline().rstrip()

    # 0 하나만 입력했다면
    if numbers == '0':
        # 반복문을 탈출하고 종료합니다.
        break

    # 두 정수를 공백으로 구분해 입력했다면
    # 각각 정수형으로 변환합니다.
    # 4 <= N <= 1000
    # 1 <= P <= N
    N, P = map(int, numbers.split(' '))
    # 시험지 종이의 개수를 저장하는 변수를 선언합니다.
    paper_cnt = N // 4

    # 시험지 종이의 개수만큼 반복합니다.
    for idx in range(paper_cnt):
        # 현재의 종이에서 가장 작은 쪽의 번호를 저장하는 변수를 선언합니다.
        start_page = 2 * idx + 1
        # 현재 종이의 쪽의 번호들을 모두 저장하는 리스트 변수를 선언합니다.
        pages_num = [start_page, start_page + 1, N - start_page, N - start_page + 1]

        # P가 pages_num에 있다면
        if P in pages_num:
            # pages_num에서 P를 없앱니다.
            pages_num.remove(P)
            # 종이에서 번호 P를 뺀 나머지 번호들을 출력 형식에 맞게 출력합니다.
            print(pages_num[0], pages_num[1], pages_num[2])
            # 답을 찾았으니 반복문을 탈출합니다.
            break