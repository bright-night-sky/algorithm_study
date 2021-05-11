# https://www.acmicpc.net/problem/1350

# 첫째 줄에는 파일의 개수 N을 입력합니다.
# 1 <= N <= 1,000 자연수입니다.
N = int(input())

# 파일마다의 크기를 넣을 리스트입니다.
file_sizes = []

# 둘째 줄에는 공백을 사이에 두고 파일의 크기를 입력합니다.
for i in range(1, N + 1):
    file_size = int(input())

    # file_sizes 리스트에 넣어줍니다.
    file_sizes.append(file_size)

# 셋째 줄에는 클러스터의 크기를 입력합니다.
cluster_size = int(input())

for file_size in file_sizes:
    