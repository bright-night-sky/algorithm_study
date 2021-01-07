# https://www.acmicpc.net/problem/2490

# 윷짝을 3번 던진다.
for i in range(0, 3):
    # 한 줄에 입력한 윷짝의 결과를 yuut 리스트에 저장한다.
    yuut = list(map(int, input().split(' ')))

    # 윷을 던져서 나온 배와 개수를 세고 변수에 저장한다.
    # 던져서 나온 것이 도개걸윷모 중 어떤 것인지 알기 위해서는 배나 등의 개수 중 하나만 알고 있어도 된다.
    bae_count = yuut.count(0)

    # 배가 1개면
    if bae_count == 1:
        # 도 출력
        print('A')
    # 배가 2개면
    elif bae_count == 2:
        # 개 출력
        print('B')
    # 배가 3개면
    elif bae_count == 3:
        # 걸 출력
        print('C')
    # 배가 4개면
    elif bae_count == 4:
        # 윷 출력
        print('D')
    # 그 외의 경우 : 배가 0개인 경우뿐이다.
    else:
        # 모 출력
        print('E')