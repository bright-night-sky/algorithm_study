# https://www.acmicpc.net/problem/4880

# 0 0 0을 입력할 때까지 테스트
while True:
    # a1, a2, a3 입력
    # -10,000 < a1, a2, a3 < 10,000
    # a1, a2, a3는 서로 같지 않다.
    a1, a2, a3 = map(int, input().split(' '))

    # 만약 a1, a2, a3가 모두 0이면
    if a1 == a2 == a3 == 0:
        # 테스트 종료
        break

    # 다음 항을 저장할 변수
    # 초기화는 일단 다음 항으로 절대로 나올 수 없는 a1으로 지정
    next = a1

    # 만약 a1, a2, a3가 등차수열이라면
    if (a3 - a2) == (a2 - a1):
        # 다음 항 계산
        next = a3 + (a3 - a2)
        # 출력
        print("AP", next)
    # 만약 a1, a2, a3가 등비수열이라면
    else:
        # 다음 항 계산
        next = a3 * (a3 / a2)
        # 출력
        print("GP", int(next))