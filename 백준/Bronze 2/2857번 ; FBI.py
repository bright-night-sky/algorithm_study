# https://www.acmicpc.net/problem/2857

# 결과를 저장할 변수를 선언합니다.
result = ""

# 5명의 요원을 반복해봅니다.
for agent_num in range(5):
    # 요원의 첩보원명을 입력합니다.
    # 알파벳 대문자, 숫자 0~9, 대시(-)로만 이루어져 있고, 최대 10글자입니다.
    agent = input()

    # 첩보원명에 FBI가 있다면
    if agent.find("FBI") != -1:
        # 결과 변수에 현재 요원의 숫자와 공백을 저장합니다.
        result += str(agent_num + 1) + " "

# 결과 변수의 값이 빈 문자열이라면
if result == "":
    # HE GOT AWAY!를 출력합니다.
    print("HE GOT AWAY!")
# 결과 변수의 값이 빈 문자열이 아니라면
else:
    # 결과 변수에 저장된 값을 출력합니다.
    print(result)