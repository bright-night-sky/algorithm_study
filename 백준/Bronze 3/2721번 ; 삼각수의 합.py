# https://www.acmicpc.net/problem/2721

# 첫째 줄에 테스트 케이스의 개수 T를 입력합니다.
T = int(input())

# n번째 삼각수, T(n) = 1 + ... + n을 계산하는 함수를 따로 만듭니다.
# 1부터 n까지 모두 더하는 공식은 n(n+1)/2입니다.
def Tn(n):
    # int형 처리를 통해 소숫점 출력을 없앱니다.
    return int(n * (n + 1) / 2)

# 테스트 케이스의 개수만큼 실행합니다.
for i in range(0, T):
    # 정수 n을 입력합니다.
    # 1 <= n <= 300
    n = int(input())

    # W(n)의 결과를 저장하는 변수입니다.
    Wn_result = 0

    # 1부터 n까지 W(n)의 식에 부합하도록 더해나갑니다.
    for j in range(1, n+1):
        Wn_result += j * Tn(j+1)

    # 현재 테스트 케이스의 W(n)의 결과를 출력합니다.
    print(Wn_result)