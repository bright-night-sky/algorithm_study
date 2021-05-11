# https://www.acmicpc.net/problem/1453

# 첫째 줄에 손님의 수 N 입력
# 1 <= N <= 100
N = int(input())

# 둘째 줄에 순서대로 각 손님이 앉고 싶어하는 자리 입력
want_position = list(map(int, input().split(' ')))

# 피시방의 각 자리가 비어있는지 여부를 리스트로 표현
# 만약 누군가 어떤 자리에 앉으면 그 자리는 False로 표현
pc_possible = [True for i in range(100)]

# 거절당하는 사람의 수를 저장하는 변수
refusal = 0

# 들어온 손님 순서대로 원하는 각 자리를 탐색한다.
for i in want_position:
    # 원하는 자리에 앉을 수 없다면
    if pc_possible[i-1] == False:
        # 거절당한 사람의 수에 1을 더한다.
        refusal += 1
    # 원하는 자리에 앉을 수 있다면
    else:
        # 해당 자리에 더 이상 앉을 수 없다고 값을 바꾼다.
        pc_possible[i-1] = False

# 거절당한 사람의 수를 출력한다.
print(refusal)