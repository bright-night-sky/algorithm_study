# https://www.acmicpc.net/problem/10995

# 첫째 줄에 N을 입력합니다.
# 1 <= N <= 100
N = int(input())

# 별을 출력 중일 때 현재 줄이 홀수 번째 줄인지 아닌지를 판별하는 변수를 선언합니다.
is_odd_line = True

# 별의 패턴을 입력한 N만큼의 줄로 반복합니다.
for line in range(N):
    # 별을 출력할 줄이 홀수 번째 줄이라면
    if is_odd_line == True:
        # 별 패턴을 반복합니다.
        for i in range(N):
            # 홀수 번째 줄에서는 '* ' 형태로 반복합니다.
            print('* ', end='')
        # 현재 줄에서 별 패턴을 다 출력했으면 다음 줄은 짝수 번째 줄이므로 is_odd_line의 값을 바꿉니다.
        is_odd_line = False
    # 별을 출력할 줄이 짝수 번째 줄이라면
    else:
        # 별 패턴을 반복합니다.
        for i in range(N):
            # 짝수 번째 줄에서는 ' *' 형태로 반복합니다.
            print(' *', end='')
        # 현재 줄에서 별 패턴을 다 출력했으면 다음 줄은 홀수 번째 줄이므로 is_odd_line의 값을 바꿉니다.
        is_odd_line = True

    # 다음 줄로 넘어갑니다.
    print()