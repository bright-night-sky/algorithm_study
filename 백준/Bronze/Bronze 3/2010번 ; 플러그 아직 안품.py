# https://www.acmicpc.net/problem/2010

# 멀티탭의 개수 N 입력
# 1 <= N <= 500,000
N = int(input())

# 제일 많은 플러그를 가지고 있는 멀티탭의 플러그 개수를 저장할 변수
# 0으로 초기화
max_plug = 0

# 입력한 멀티탭의 개수만큼 반복
for i in range(0, N):
    # 각 멀티탭이 몇 개의 플러그를 꽂을 수 있도록 되어 있는지 자연수 입력
    # 1,000 미만의 자연수
    plug = int(input())

    # 저장되어 있는 최대 플러그의 개수보다 지금 입력된 멀티탭의 플러그가 많다면
    if max_plug < plug:
        # 최대 플러그를 갱신
        max_plug = plug

# 최대 플러그를 출력
print(max_plug)
