# https://www.acmicpc.net/problem/13752

# 첫 번째 줄에는 테스트 케이스의 개수 n을 입력합니다.
# 1 <= n <= 100
n = int(input())

# 테스트 케이스의 개수만큼 돌려봅니다.
for i in range(0, n):
    # 히스토그램의 크기 k를 입력합니다.
    # 1 <= k <= 80
    k = int(input())

    # 히스토그램의 크기 k와 동일한 수의 '='를 출력합니다.
    # '=' 사이에 공백은 없습니다.
    print('=' * k)