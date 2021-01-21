# https://www.acmicpc.net/problem/2702

# 첫째 줄에 테스트 케이스의 개수 T 입력
# 1 <= T <= 1,000
T = int(input())

# 각 테스트 케이스마다 실행
for i in range(0, T):
    # 두 정수 a, b를 공백으로 구분해서 입력
    # 1 <= a, b <= 1,000
    a, b = map(int, input().split(' '))

    # a와 b 중 더 큰 수를 저장하는 변수
    max_num = max(a, b)
    # a와 b 중 더 작은 수를 저장하는 변수
    min_num = min(a, b)

    # 최소공배수를 저장하는 변수
    # least common multiple
    lcm = 0

    # 최대공약수를 저장하는 변수
    # greatest common divisor
    gcd = 0

    # 유클리드 호제법으로 최대공약수 구하기
    # 유클리드 호제법을 위해 사용할 임시 변수들
    gcd_a = max_num
    gcd_b = min_num

    # 나머지가 0이 될 때까지 반복
    while True:
        # 큰 숫자를 작은 숫자로 나누어본다.
        remainder = gcd_a % gcd_b

        # 그 나머지가 0이라면
        if remainder == 0:
            # 작은 숫자가 최대공약수이다.
            gcd = gcd_b
            # 최대공약수를 찾았으니 반복문 탈출
            break
        # 나머지가 0이 아니라면
        else:
            # 작은 숫자를 큰 숫자 변수에 넣고, 나머지를 작은 숫자 변수에 넣은 뒤 반복해본다.
            gcd_a = gcd_b
            gcd_b = remainder

    # 최소공배수 구하기
    # 최대공약수를 구했으면 최소공배수는 (두 자연수의 곱) / (최대공약수)으로 쉽게 구할 수 있다.
    lcm = int(a * b / gcd)

    # 결과 출력
    print(lcm, gcd)



