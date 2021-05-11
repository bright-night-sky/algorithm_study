# https://www.acmicpc.net/problem/2547

# 테스트 케이스 개수 T 입력
T = int(input())
# 테스트 케이스를 입력하고 난 뒤의 빈 줄 입력을 처리하기 위한 코드
blank = input()

for i in range(0, T):
    # 학생 수 N 입력 : 1 <= N <= 100000의 자연수
    N = int(input())
    # 학생들이 가져온 총 사탕 개수를 저장할 변수
    sum = 0

    # 학생마다 사탕의 개수 입력
    # 사탕 개수는 0보다 크거나 같은 정수
    # 각 사탕 개수는 10^18보다 작거나 같다.
    for j in range(0, N):
        candy = int(input())
        # 각 사탕 개수를 총합한다.
        sum += candy

    # 모든 학생들이 가져온 사탕을 합쳐서 학생마다 똑같이 나눌 수 있다면
    if sum % N == 0:
        # YES 출력
        print("YES")
    # 똑같이 못 나누면
    else:
        # NO 출력
        print("NO")

    # 각 테스트 케이스 사이마다 빈 줄로 구분되어 있다.
    # 다만 마지막 테스트 케이스 다음에는 빈 줄 입력이 없으므로 if문으로 처리했다.
    if i != T-1:
        blank = input()
