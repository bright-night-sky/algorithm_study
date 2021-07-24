# https://programmers.co.kr/learn/courses/30/lessons/49994

# 명령어 dir이 매개변수로 주어집니다.
def solution(dirs):
    # 캐릭터가 처음 걸어본 길들의 정보들을 저장할 set 변수를 선언합니다.
    first_load = set()
    # 현재 캐릭터의 위치를 저장하는 리스트 변수를 선언합니다.
    # 처음에는 0, 0에서 시작합니다.
    point = [0, 0]

    # 명령어에서 한 글자씩 반복해봅니다.
    for dir in dirs:
        # 현재 캐릭터가 있는 위치와 현재 명령어 글자를 저장할 변수를 선언합니다.
        point_dir = None
        # point_dir과 반대 방향의 정보를 저장할 변수를 선언합니다.
        reverse_point_dir = None

        # 명령어의 현재 글자가 U이고, 캐릭터의 y좌표에 1을 더했을 때 5보다 작거나 같다면
        if dir == 'U' and point[1] + 1 <= 5:
            # (현재 위치 x좌표, 현재 위치 y좌표, 현재 명령어 글자) 튜플을 point_dir에 저장합니다.
            point_dir = (point[0], point[1], dir)
            # 위로 이동하므로 현재 위치의 y좌표에 1을 더합니다.
            point[1] += 1
            # (다음 위치 x좌표, 다음 위치 y좌표, 현재 명령어 글자의 반대 방향) 튜플을 reverse_point_dir에 저장합니다.
            reverse_point_dir = (point[0], point[1], 'D')
        # 명령어의 현재 글자가 D이고, 캐릭터의 y좌표에 1을 뺐을 때 -5보다 크거나 같다면
        elif dir == 'D' and point[1] - 1 >= -5:
            # (현재 위치 x좌표, 현재 위치 y좌표, 현재 명령어 글자) 튜플을 point_dir에 저장합니다.
            point_dir = (point[0], point[1], dir)
            # 아래로 이동하므로 현재 위치의 y좌표에 1을 뺍니다.
            point[1] -= 1
            # (다음 위치 x좌표, 다음 위치 y좌표, 현재 명령어 글자의 반대 방향) 튜플을 reverse_point_dir에 저장합니다.
            reverse_point_dir = (point[0], point[1], 'U')
        # 명령어의 현재 글자가 R이고, 캐릭터의 x좌표에 1을 더했을 때 5보다 작거나 같다면
        elif dir == 'R' and point[0] + 1 <= 5:
            # (현재 위치 x좌표, 현재 위치 y좌표, 현재 명령어 글자) 튜플을 point_dir에 저장합니다.
            point_dir = (point[0], point[1], dir)
            # 오른쪽으로 이동하므로 현재 위치의 x좌표에 1을 더합니다.
            point[0] += 1
            # (다음 위치 x좌표, 다음 위치 y좌표, 현재 명령어 글자의 반대 방향) 튜플을 reverse_point_dir에 저장합니다.
            reverse_point_dir = (point[0], point[1], 'L')
        # 명령어의 현재 글자가 L이고, 캐릭터의 x좌표에 1을 뺐을 때 -5보다 크거나 같다면
        elif dir == 'L' and point[0] - 1 >= -5:
            # (현재 위치 x좌표, 현재 위치 y좌표, 현재 명령어 글자) 튜플을 point_dir에 저장합니다.
            point_dir = (point[0], point[1], dir)
            # 왼쪽으로 이동하므로 현재 위치의 x좌표에 1을 뺍니다.
            point[0] -= 1
            # (다음 위치 x좌표, 다음 위치 y좌표, 현재 명령어 글자의 반대 방향) 튜플을 reverse_point_dir에 저장합니다.
            reverse_point_dir = (point[0], point[1], 'R')

        # point_dir과 reverse_point_dir 튜플들을 first_load에 넣어줍니다.
        first_load.add(point_dir)
        first_load.add(reverse_point_dir)

    # 캐릭터가 한 번 이동할 때 first_load에 길의 정보를 2번 넣어주므로
    # 캐릭터가 처음 걸어본 길의 길이인 first_load의 길이의 절반을 반환합니다.
    return len(first_load) // 2