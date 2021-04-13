# https://www.acmicpc.net/problem/19563

# 세 정수 a, b, c를 공백을 사이에 두고 입력합니다.
# -10^9 <= a, b <= 10^9
# 0 <= c <= 2 X 10^9
a, b, c = map(int, input().split(' '))

# a와 b의 절댓값의 합을 저장하는 변수를 선언합니다.
ab_abs_sum = abs(a) + abs(b)

# a와 b 각각의 절댓값의 합이 c보다 작거나 같고
# a, b 절댓값의 합과 c가 동시에 홀수이거나 짝수인 경우에만
# 개구리가 문제의 조건대로 이동이 가능합니다.

# 위의 조건을 만족해 개구리가 해당 좌표로 이동하는 것이 가능하면
if (ab_abs_sum <= c) and ((ab_abs_sum % 2 == 0 and c % 2 == 0) or (ab_abs_sum % 2 == 1 and c % 2 == 1)):
    # YES를 출력합니다.
    print("YES")
# 위의 조건을 만족하지 못해 개구리가 해당 좌표로 이동하는 것이 불가능하다면
else:
    # NO를 출력합니다.
    print("NO")

