# https://www.acmicpc.net/problem/2061

# 두 정수 K, L 입력
# 4 <= K <= 10^100
# 2 <= L <= 1,000,000
K, L = map(int, input().split(' '))

# 나쁜 암호일 경우 K의 가장 작은 (1 아닌) 인수를 저장할 변수
bad_min = 0

# K를 2부터 L보다 작은 정수로 나누어 보면서 만약 L보다 작은 값에서 나누어 지는 숫자가 있다면 나쁜 암호이다.
for i in range(2, L):
    if K % i == 0:
        bad_min = i
        break

# 좋은 암호라서 bad_min에 초기화했던 0이 그대로라면
if bad_min == 0:
    # GOOD 출력
    print("GOOD")
# 나쁜 암호라서 bad_min에 K의 가장 작은 (1 아닌) 인수가 저장되어 있다면
else:
    # BAD와 그 해당 인수를 출력
    print("BAD", bad_min)