# https://www.acmicpc.net/problem/11949

# 첫 번째 줄에는 학생의 수 N, 카드의 수 M을 공백으로 구분해 입력합니다.
# 1 <= N <= 100
# 1 <= M <= 100
N, M = map(int, input().split(' '))

# 학생들이 갖고 있는 번호표를 저장하는 리스트 변수를 선언합니다.
num_ticket = []

# 두 번째 줄부터 N줄에 걸쳐 각 학생이 가지는 번호표의 값 Ai를 입력합니다.
# 1 <= Ai <= 1000
for i in range(N):
    num_ticket.append(int(input()))

# 1부터 M번 카드까지 게임의 규칙을 반복합니다.
for i in range(1, M+1):
    # 카드를 뽑은 뒤에 게임의 규칙을 반복하기 위해 학생이 가진 번호표마다 반복해봅니다.
    for index in range(1, len(num_ticket)):
        # Aj % i의 값이 Aj+1 % i의 값보다 크면
        if num_ticket[index-1] % i > num_ticket[index] % i:
            # 두 학생의 번호표를 서로 교환합니다.
            num_ticket[index-1], num_ticket[index] = num_ticket[index], num_ticket[index-1]

# 과정을 모두 마친 후 각 학생들이 가진 번호표를 순서대로 출력합니다.
for num in num_ticket:
    print(num)