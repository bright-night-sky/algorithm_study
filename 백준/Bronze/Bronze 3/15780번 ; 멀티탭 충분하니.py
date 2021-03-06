# https://www.acmicpc.net/problem/15780

# 첫째 줄에 스터디에 온 학생의 수 N명, 멀티탭의 수 K를 입력합니다.
# 1 <= N <= 100
# 1 <= K <= 100
N, K = map(int, input().split(' '))

# 두 번째 줄에 각 멀티탭 구의 수 A[i]들을 입력합니다.
# 3 <= A[i] <= 8
multitap_gu = list(map(int, input().split(' ')))

# 멀티탭에 2개 이상 연속으로 코드를 꽂으면 안되므로
# 한 멀티탭에 코드를 최대한 반 정도 꽂을 수 있습니다.

# 모든 멀티탭에서 최대한 사용 가능한 구의 개수를 저장하는 변수입니다.
total_can_gu = 0

# 각 멀티탭마다 최대한으로 사용 가능한 멀티탭 구의 개수를 구해봅니다.
for gu in multitap_gu:
    # 현재 멀티탭에서 최대한 사용 가능한 구의 개수를 구합니다.
    # 현재 멀티탭에서 구의 수가 짝수이면
    if gu % 2 == 0:
        # 최대한 사용 가능한 구의 수는 구의 수의 반입니다.
        cur_can_gu = gu // 2
    # 현재 멀티탭에서 구의 수가 홀수이면
    else:
        # 최대한 사용 가능한 구의 수는 구의 수의 반에 1을 더한 수입니다.
        cur_can_gu = gu // 2 + 1
    # 그 최대한 사용 가능한 구를 total_can_gu에 더해줍니다.
    total_can_gu += cur_can_gu

# 모든 멀티탭에서 최대한 사용 가능한 구의 개수가 학생의 수보다 많거나 같다면
if total_can_gu >= N:
    # 모든 학생이 멀티탭을 사용할 수 있으므로 YES를 출력합니다.
    print("YES")
# 그렇지 않다면
else:
    # 멀티탭을 사용하지 못하는 학생이 있으므로 NO를 출력합니다.
    print("NO")