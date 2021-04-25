# https://www.acmicpc.net/problem/14730

# 첫째 줄에 항의 개수 N을 입력합니다.
# 1 <= N <= 100
N = int(input())

# f'(1)의 결과를 저장하는 변수를 선언합니다.
result = 0

# 항의 개수 N만큼 반복합니다.
for term in range(N):
    # 항의 계수 C, 항의 차수 K를 입력합니다.
    # -100 <= C <= 100, C는 0이 아닙니다.
    # 0 <= K <= 1000
    # 항의 차수가 큰 순서대로 입력하며, 항의 차수가 같은 항은 2개 이상 존재하지 않습니다.
    C, K = map(int, input().split(' '))

    # 문제의 힌트에서처럼 3x^3 항을 미분하면 9x^2이므로
    # 여기 x에 1을 대입하면 9 * 1^2입니다.
    # 따라서 각 항마다의 계산 결과는 단순히 C와 K의 곱이므로
    # 이것을 차례대로 더하면 됩니다.
    result += C * K

# f'(1) 결과를 출력합니다.
print(result)