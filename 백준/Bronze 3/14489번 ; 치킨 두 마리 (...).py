# https://www.acmicpc.net/problem/14489

# 첫째 줄에 두 통장의 잔고 A, B를 입력합니다.
# 0 <= A, B <= 1,000,000,000
A, B = map(int, input().split(' '))

# 둘째 줄에 치킨 한 마리의 가격 C를 입력합니다.
# 0 <= C <= 1,000,000,001
C = int(input())

# 두 통장 잔고의 합계를 저장하는 변수입니다.
total = A + B

# 만약 치킨 두 마리를 살 수 있다면
if total >= C * 2:
    # 치킨 두 마리를 사고 남은 두 통장 잔고의 합을 출력합니다.
    print(total - C * 2)
# 만약 살 수 없다면
else:
    # 두 통장의 잔고의 합을 출력합니다.
    print(total)