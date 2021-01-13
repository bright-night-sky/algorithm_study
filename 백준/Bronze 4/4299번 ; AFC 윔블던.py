# https://www.acmicpc.net/problem/4299

# 두 팀 점수의 합과 차를 빈 칸으로 구분되어 입력
# 축구 점수는 항상 음이 아닌 정수
# 합과 차 : 1000보다 작거나 같은 음이 아닌 정수
plus, minus = map(int, input().split(' '))

# 두 팀의 각 점수를 저장하는 변수
MK = -1
AFC = -1

# 0부터 두 팀 점수의 합의 1/2까지 돌려보면 된다.
for i in range(0, int(plus / 2) + 1):
    # 만약 두 팀 점수의 차와 같은 결과도 얻을 수 있는 경우라면
    if ((plus - i) - i) == minus:
        # 두 팀의 점수를 각 변수에 저장
        MK = i
        AFC = plus - i
        # 반복문을 더 돌릴 필요가 없으므로 반복문 탈출
        break

# MK와 AFC에 -1말고 아무런 값도 지정되지 않았다면, 입력으로 받은 합과 차를 갖는 경기 결과가 없는 것이다.
if MK == -1 and AFC == -1:
    # -1 출력
    print(-1)
# MK와 AFC에 0 외의 값이 저장되어 있다면
else:
    # 큰 값 순서대로 출력
    # 위의 경우 AFC의 점수가 MK보다 무조건 크게 저장되므로 AFC, MK 순서대로 출력하면 된다.
    print(AFC, MK)
