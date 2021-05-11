# https://www.acmicpc.net/problem/5026

# 첫째 줄에 문제의 개수 N을 입력합니다.
N = int(input())

# 문제의 개수 N만큼 반복합니다.
for i in range(N):
    # 문제를 입력합니다.
    # a, b는 0에서 1000까지의 정수입니다.
    question = input()

    # 입력한 문제가 P=NP라면
    if question == 'P=NP':
        # skipped를 출력합니다.
        print('skipped')
        # 이번 문제는 결과를 출력했으니 다음 문제로 넘어갑니다.
        continue

    # P=NP가 아닌 문제인 경우 +로 구분해서 a, b 변수에 값을 저장합니다.
    a, b = map(int, question.split('+'))

    # a와 b를 더한 값을 출력합니다.
    print(a + b)