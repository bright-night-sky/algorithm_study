# https://www.acmicpc.net/problem/15819

# 첫 줄에 핸들의 개수 N, 핸들 중 사전 순으로 찾을 I번째의 단어인 I를 입력합니다.
# 1 <= I, N <= 100
N, I = map(int, input().split(' '))

# 입력한 핸들들을 저장할 리스트 변수를 선언합니다.
handles = []

# 핸들의 개수 N만큼 반복합니다.
for i in range(N):
    # 핸들을 하나 입력합니다.
    # 영어 소문자, 숫자로만 이루어져 있으며 길이는 20보다 짧거나 같습니다.
    # 완전히 같은 핸들은 없습니다.
    handle = input()

    # 입력한 핸들을 handles 리스트 변수에 넣어줍니다.
    handles.append(handle)

# handles 내부의 값들을 사전 순으로 정렬시킵니다.
handles.sort()

# I번째 핸들을 출력합니다.
print(handles[I - 1])