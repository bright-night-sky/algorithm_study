# https://www.acmicpc.net/problem/4892

# 케이스 번호를 저장하는 변수
case_num = 1

# 0을 입력할 때까지 테스트는 계속한다.
while True:
    # 한 테스트 케이스 입력
    # 0 < n0 < 1,000,000
    n0 = int(input())

    # n1이 짝수인지 홀수인지를 저장하는 변수
    n1_is = ''

    # 0을 입력하면 테스트 종료
    if n0 == 0:
        break
    # 숫자를 입력했다면
    else:
        # n1 계산
        n1 = 3 * n0

        # n1이 짝수라면
        if n1 % 2 == 0:
            # 밑의 식으로 n2 계산
            n2 = n1 / 2
            # n1은 짝수라고 표시
            n1_is = 'even'
        # n1이 홀수라면
        else:
            # 밑의 식으로 n2 계산
            n2 = (n1 + 1) / 2
            # n1은 홀수라고 표시
            n1_is = 'odd'

        # n3 계산
        n3 = 3 * n2

        # n4 계산
        n4 = n3 // 9

    # 한 케이스의 결과를 출력
    print(f"{case_num}. {n1_is} {int(n4)}")

    # 다음 케이스 번호를 출력해야하므로 케이스 번호에 1 추가
    case_num += 1