# https://www.acmicpc.net/problem/18228

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 얼음의 개수를 의미하는 N을 입력합니다.
# 3 <= N <= 200,000
N = int(stdin.readline())
# 각 얼음을 깨뜨리는 데에 드는 힘을 의미하는 Ai들을 공백으로 구분해 입력합니다.
# 1 <= Ai <= 1,000,000,000
# 각각 정수형으로 변환하고 튜플 변수에 넣어줍니다.
A = tuple(map(int, stdin.readline().split(' ')))
# 펭귄이 위치한 얼음의 인덱스를 저장하는 변수를 선언합니다.
penguin_idx = A.index(-1)
# 펭귄이 위치한 얼음에서 왼쪽편에 있는 얼음들 중 깨뜨리는데 가장 적게 드는 힘을 저장하는 변수를 선언합니다.
left_min = min(A[:penguin_idx])
# 펭귄이 위치한 얼음에서 오른쪽편에 있는 얼음들 중 깨뜨리는데 가장 적게 드는 힘을 저장하는 변수를 선언합니다.
right_min = min(A[penguin_idx+1:])

# 펭귄을 떨어뜨릴 수 있는 최소 힘인 left_min과 right_min의 합을 출력합니다.
print(left_min + right_min)