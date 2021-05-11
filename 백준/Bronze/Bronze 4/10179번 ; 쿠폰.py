# https://www.acmicpc.net/problem/10179

# 테스트 케이스의 수 입력
test_case = int(input())

# 테스트 케이스만큼 돌려본다.
for i in range(0, test_case):
    # 소수점 둘째자리까지 주어진 물건의 원래 가격 입력
    production_cost = float(input())

    # 할인된 가격 계산
    # 나누어 떨어지지 않을 때는 소수점 셋째 자리에서 반올림해서 둘째 자리까지 출력
    # 출력 형식을 보면 소수점이 0이 되어도 .00으로 만들어줬다.
    couponed_price = "%.2f" % round(production_cost * 0.8, 2)

    # 앞에 $ 표시를 붙여서 출력
    print(f"${couponed_price}")