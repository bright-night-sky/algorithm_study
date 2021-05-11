# https://www.acmicpc.net/problem/17350

# 첫째 줄에 야구팀의 멤버 수 N을 입력합니다.
# 1 <= N <= 1,000
N = int(input())

# 결과를 출력할 변수를 선언합니다.
# 뭐(anj)라는 이름을 가진 선수가 없는 경우 출력할 값인 뭐야?로 초기화해줍니다.
result = "뭐야?"

# 야구팀의 멤버 수 N만큼 반복해봅니다.
for i in range(N):
    # 선수 이름을 입력합니다.
    player = input()

    # 현재 입력받은 선수의 이름이 anj라면
    if player == "anj":
        # 결과를 출력할 변수의 값을 뭐야;로 변경해줍니다.
        result = "뭐야;"
        # anj 선수가 있으므로 뒤에 선수가 더 있더라도 볼 필요가 없으므로 반복문을 탈출합니다.
        break

# 결과를 출력합니다.
print(result)