# https://www.acmicpc.net/problem/10813

# 첫째 줄에 N, M을 공백으로 구분해 입력합니다.
# 1 <= N <= 100
# 1 <= M <= 100
N, M = map(int, input().split(' '))

# 1번부터 N번 바구니에 있는 공의 번호를 저장하는 리스트 변수를 선언합니다.
basket = [str(i+1) for i in range(N)]

# M번 교환을 반복합니다.
for exchange in range(M):
    # 교환 방법인 i, j를 공백으로 구분해 입력합니다.
    # 1 <= i <= j <= N
    i, j = map(int, input().split(' '))

    # i번 바구니와 j번 바구니에 들어있는 공을 교환합니다.
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

# 최종적으로 바구니에 들어있는 공의 번호를 출력합니다.
print(' '.join(basket))