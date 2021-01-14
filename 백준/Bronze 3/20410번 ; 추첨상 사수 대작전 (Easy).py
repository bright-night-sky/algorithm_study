# https://www.acmicpc.net/problem/20410

# 한 줄에 걸쳐 준표가 좋아하는 소수 m, 참가자들이 정한 Seed, 시연으로 공개된 X1, X2 입력
# 항상 가능한 상황만 입력으로 주어진다.
# m <= 100 (m은 소수)
# 0 < Seed, X1, X2 < m
m, Seed, X1, X2 = map(int, input().split(' '))

# a와 c를 저장할 변수
a_result = -1
c_result = -1

# a와 c를 0부터 돌려보면서 부합하는 경우를 찾는다.
for a in range(0, m):
    for c in range(0, m):
        # 현재의 a와 c가 계산식에 부합한다면
        if (a * Seed + c) % m == X1 and (a * X1 + c) % m == X2:
            # 최총 결과를 저장하는 변수에 저장
            a_result = a
            c_result = c
            break

    # 최종 결과를 찾은 경우에는 반복문 탈출
    if a_result != -1 and c_result != -1:
        break

# 최종 결과를 출력한다.
print(a_result, c_result)