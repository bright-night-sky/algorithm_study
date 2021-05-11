# https://www.acmicpc.net/problem/20361

# 첫째 줄에 N, X, K를 공백으로 구분해서 입력합니다.
# 3 <= N <= 200,000
# 1 <= x <= N
# 1 <= K <= 100,000
N, X, K = map(int, input().split(' '))

# K개의 줄에 순서대로 바꾼 두 컵의 위치 Ai, Bi를 공백으로 구분해서 입력합니다.
for i in range(0, K):
    # Ai, Bi를 입력합니다.
    # 1 <= Ai, Bi <= N
    # Ai와 Bi는 다른 값입니다.
    Ai, Bi = map(int, input().split(' '))

    # 만약 공이 들어있는 컵의 위치를 옮기는 행동이라면,
    # 즉, Ai나 Bi의 값이 X라면
    # 공이 그 반대인 Bi나 Ai로 옮겨집니다.
    if Ai == X:
        X = Bi
    elif Bi == X:
        X = Ai
    # 만약 공이 들어있는 컵을 건드리지 않는다면,
    else:
        # 그냥 넘어갑니다.
        continue

# 최종적으로 공이 들어있는 컵을 출력합니다.
print(X)