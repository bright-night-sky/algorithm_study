# https://www.acmicpc.net/problem/5217

# 첫째 줄에 테스트 케이스의 수 입력
# 테스트 케이스 수 < 100
test_cases = int(input())

# 각 테스트 케이스 돌려보기
for case in range(0, test_cases):
    # n 입력
    n = int(input())
    # 이번 테스트 케이스의 결과를 저장할 변수
    result = ""
    # 각 쌍을 저장할 리스트 변수
    pair = []

    # 쌍을 찾을 때 n의 반까지 돌려보면 된다.
    for i in range(1, int(n/2)+1):
        # 쌍의 두 수를 저장할 변수
        first = i
        second = n - i

        # 쌍의 두 수가 다른 경우
        if first != second:
            # 리스트에 그 쌍을 저장
            pair.append(str(first) + " " + str(second))

    # 쌍이 여러 개일 경우 출력될 쌍의 사이에 ', '을 추가
    result = ', '.join(pair)

    # 이번 케이스의 결과 출력
    print(f"Pairs for {n}: {result}")