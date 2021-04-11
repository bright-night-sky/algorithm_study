# https://www.acmicpc.net/problem/10174

# 첫째 줄에는 테스트 케이스의 수 n을 입력합니다.
n = int(input())

# 테스트 케이스의 수만큼 반복합니다.
for i in range(n):
    # 팰린드롬을 판별할 한 줄의 텍스트를 입력합니다.
    # 공백은 구분하지만, 대소문자는 구분하지 않으므로 소문자 처리를 해줍니다.
    text = input().lower()

    # 만약 팰린드롬이 맞다면
    if text == text[::-1]:
        # Yes를 출력합니다.
        print("Yes")
    # 만약 팰린드롬이 아니라면
    else:
        # No를 출력합니다.
        print("No")