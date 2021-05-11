# https://www.acmicpc.net/problem/4458

# 첫째 줄에는 줄의 수 N을 입력합니다.
N = int(input())

# 테스트 케이스의 수만큼 반복합니다.
for i in range(N):
    # 문장을 입력하고 한 글자씩 리스트 변수에 넣어줍니다.
    # 문장에 들어있는 글자의 수는 30을 넘지 않습니다.
    sentence = list(input())

    # 문장의 첫 글자를 대문자로 바꿔줍니다.
    sentence[0] = sentence[0].upper()

    # 리스트 변수에 있는 글자들을 다시 문자열로 바꿔 출력합니다.
    print(''.join(sentence))