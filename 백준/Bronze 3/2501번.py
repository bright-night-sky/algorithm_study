# https://www.acmicpc.net/problem/2501

# N, K 입력
# 1 <= N <= 10000
# 1 <= K <= N
N, K = map(int, input().split(' '))
# K번째를 세기 위한 변수
count = 0

# 1부터 N까지 약수 찾기
for i in range(1, N+1):
    # 만약 N이 반복문 변수 i로 나누어진다면 i는 N의 약수이다.
    if N % i == 0:
        # 약수를 찾았으므로 count에 1 증가
        count += 1

    # 만약 count가 K와 같다면 K번째로 작은 수이다.
    if count == K:
        print(i)
        break

# 만약 K번째 약수가 존재하지 않을 경우
if count < K:
    # 0 출력
    print(0)