# https://www.acmicpc.net/problem/4740

# ***을 입력할 때까지 한 문장씩 입력합니다.
while True:
    # ASCIi 글자로 나타낼 수 있는 단어들로 구성된 한 문장을 입력합니다.
    # 1글자에서 80글자로 이루어져 있습니다.
    sentence = input()

    # 입력한 문장이 ***이라면
    if sentence == '***':
        # 반복문을 탈출해서 종료시킵니다.
        break

    # 입력받은 한 문장을 역순으로 출력합니다.
    print(sentence[::-1])