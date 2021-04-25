# https://www.acmicpc.net/problem/20205

# 첫 번째 줄에는 정사각형 단색 비트맵의 가로/세로 길이 N,
# 이미지를 늘릴 배수 K를 입력합니다.
# 1 <= N <= 10
# 1 <= K <= 10
N, K = map(int, input().split(' '))

# 정사각형 단색 비트맵의 가로/세로 길이 N만큼 반복합니다.
for i in range(N):
    # N개의 픽셀 정보를 입력합니다.
    # 각 픽셀 정보는 공백으로 구분해 리스트 변수에 저장합니다.
    line = input().split(' ')

    # 입력받은 픽셀 정보 한 줄을 K 배수만큼 늘려야하므로 K만큼 반복합니다.
    for one_line in range(K):
        # 입력받은 픽셀 정보 한 줄 내에서도 한 픽셀을 K 배수만큼 늘려야하므로
        # 입력받은 픽셀 정보 리스트를 하나씩 반복해봅니다.
        for pixel in line:
            # 한 픽셀 정보를 K 배수만큼 늘려줍니다.
            print(f"{pixel} " * K, end="")
        # 한 줄을 K 배수만큼 다 늘려줬다면 다음 줄로 넘어갑니다.
        print()