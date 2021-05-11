# https://www.acmicpc.net/problem/5355

# 첫째 줄에 테스트 케이스의 개수 T를 입력합니다.
T = int(input())

# 테스트 케이스의 개수만큼 반복합니다.
for i in range(T):
    # 화성 수학식 한 줄을 입력하고 공백으로 구분해 리스트 변수로 만들어줍니다.
    mars_math = input().split(' ')

    # 화성 수학식 리스트 변수에서 인덱스 0의 값은 계산을 시작할 값이므로 따로 변수로 만들어줍니다.
    num = float(mars_math[0])
    # 화성 수학식 리스트 변수에서 인덱스 1부터 끝까지의 값은 연산자로서 따로 리스트 변수로 만들어줍니다.
    operators = mars_math[1:]

    # 연산자 리스트 변수에서 연산자들을 하나씩 반복해봅니다.
    for operator in operators:
        # 현재 연산자가 @이라면
        if operator == '@':
            # 현재 값에 3을 곱해줍니다.
            num *= 3
        # 현재 연산자가 %라면
        elif operator == '%':
            # 현재 값에 5를 더해줍니다.
            num += 5
        # 현재 연산자가 #이라면
        else:
            # 현재 값에 7을 빼줍니다.
            num -= 7

    # 결과에서 소수점 둘째자리까지만 출력합니다.
    print(format(num, ".2f"))
