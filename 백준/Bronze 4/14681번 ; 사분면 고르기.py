# https://www.acmicpc.net/problem/14681

# 첫 줄에는 정수 x 입력
# -1000 <= x <= 1000; x는 0이 아니다.
x = int(input())

# 둘째 줄에는 정수 y 입력
# -1000 <= y <= 1000; y는 0이 아니다.
y = int(input())

# x, y가 모두 양수이면
if x > 0 and y > 0:
    # 1사분면이므로 1 출력
    print(1)
# x는 음수, y는 양수이면
elif x < 0 and y > 0:
    # 2사분면이므로 2 출력
    print(2)
# x, y가 모두 음수이면
elif x < 0 and y < 0:
    # 3사분면이므로 3 출력
    print(3)
# x는 양수, y는 음수이면
else:
    # 4사분면이므로 4 출력
    print(4)