# https://www.acmicpc.net/problem/14912

# 자연수 n, 한 자리 숫자 d를 입력합니다.
# 1 <= n <= 100,000
# 0 <= d <= 9
n, d = map(int, input().split(' '))

# d의 빈도수를 저장하는 변수를 선언합니다.
d_count = 0

# 1부터 n까지 반복해봅니다.
for number in range(1, n + 1):
    # 현재 숫자를 문자열 형태로 변환합니다.
    number = str(number)

    # 현재 숫자에서 d의 개수를 세어 d_count에 더해줍니다.
    d_count += number.count(str(d))

# d의 개수를 출력합니다.
print(d_count)