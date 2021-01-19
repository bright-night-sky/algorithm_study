# https://www.acmicpc.net/problem/16204

# N, M, K 입력
# 1 <= N M= 1,000,000
# 0 <= M, K <= N
N, M, K = map(int, input().split(' '))

# 앞면과 뒷면이 같은 모양이 적혀있는 카드의 개수는
# 앞면의 O와 뒷면의 O의 개수 중 더 적은 숫자와
# 앞면의 X와 뒷면의 X의 개수 중 더 적은 숫자를 더한 것이다.

# 앞면의 O 개수
front_O = M
# 앞면의 X 개수
front_X = N - M
# 뒷면의 O 개수
back_O = K
# 뒷면의 X 개수
back_X = N - K

# 결과 출력
print(min(front_O, back_O) + min(front_X, back_X))