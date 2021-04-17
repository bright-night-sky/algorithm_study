# https://www.acmicpc.net/problem/5691

# 0 두 개를 입력할 때까지 반복합니다.
while True:
    # A, B를 공백으로 구분해 한 줄로 입력합니다.
    # 1 <= A <= B <= 10^9
    A, B = map(int, input().split(' '))

    # 입력값이 0 0이라면
    if A == 0 and B == 0:
        # 반복문을 탈출하고 종료시킵니다.
        break
    # 입력값이 다른 숫자들이라면
    else:
        # A, B, C의 평균과 중앙값이 같을 때 가장 작은 정수 C를 찾아야 하므로
        # C는 A보다 작으면서
        # B와 A의 차이값을 구해서 C도 A보다 그 차이값만큼 작으면 됩니다.
        # 그러면 A, B, C의 평균값은 A가 되고, 중앙값도 A가 됩니다.
        print(A - (B - A))