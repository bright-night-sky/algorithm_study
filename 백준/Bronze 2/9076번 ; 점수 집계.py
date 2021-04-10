# https://www.acmicpc.net/problem/9076

# 첫 줄에는 테스트 케이스의 개수 T를 입력합니다.
# 1 <= T <= 10
T = int(input())

# 테스트 케이스의 개수만큼 반복합니다.
for i in range(T):
    # 다섯 심판이 준 점수 다섯 개의 정수 Ni를 하나의 공백을 사이에 두고 입력합니다.
    # 그 점수들을 리스트 변수 N에 넣습니다.
    N = list(map(int, input().split(' ')))

    # 입력한 점수들 중 최고점을 리스트에서 빼냅니다.
    N.pop(N.index(max(N)))
    # 입력한 점수들 중 최저점을 리스트에서 빼냅니다.
    N.pop(N.index(min(N)))

    # 남은 점수들 중에서 최고점과 최저점의 차이가 4점 이상인 경우
    if max(N) - min(N) >= 4:
        # KIN을 출력합니다.
        print("KIN")
    # 남은 점수들 중에서 최고점과 최저점의 차이가 4점 미만인 경우
    else:
        # 남은 점수들의 합을 출력합니다.
        print(sum(N))