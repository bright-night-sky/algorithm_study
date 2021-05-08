# https://www.acmicpc.net/problem/10864

# 첫째 줄에 도현이네 반 학생의 수 N과
# 친구 관계의 수 M을 입력합니다.
# 1 <= N <= 1,000
# 0 <= M <= 1,000
N, M = map(int, input().split(' '))

# 각 학생들의 친구들을 저장할 리스트 변수를 선언합니다.
friendships = [[] for student in range(N)]

#
for friendship_index in range(M):
    A, B = map(int, input().split(' '))

    friendships[A - 1].append(B)
    friendships[B - 1].append(A)

for student in friendships:
    print(len(student))