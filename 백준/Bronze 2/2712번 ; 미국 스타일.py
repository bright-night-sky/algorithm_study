# https://www.acmicpc.net/problem/2712

# 테스트 케이스의 개수 T 입력
# 1 <= T <= 1000
T = int(input())

# 각 테스트 케이스 돌려보기
for i in range(0, T):
    # 한 테스트 케이스에 값과 단위 입력
    value, measure = input().split(' ')
    value = float(value)

    # 출력할 때 주의해야 할 점
    # 4.2000 처럼 소숫점 넷째 자리 이전에 소수가 끝난다고 해도 무조건 소숫점 넷째 자리까지 출력시킨다.

    # 단위가 킬로그램(kg)일 경우
    if measure == 'kg':
        # 파운드(lb)로 변경
        print('%.4f' % round(value * 2.2046, 4), 'lb')
    # 단위가 파운드(lb)일 경우
    elif measure == 'lb':
        # 킬로그램(kg)으로 변경
        print('%.4f' % round(value * 0.4536, 4), 'kg')
    # 단위가 리터(l)일 경우
    elif measure == 'l':
        # 갤런(g)으로 변경
        print('%.4f' % round(value * 0.2642, 4), 'g')
    # 단위가 갤런(g)일 경우
    else:
        # 리터(l)로 변경
        print('%.4f' % round(value * 3.7854, 4), 'l')
