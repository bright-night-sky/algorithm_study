# https://www.acmicpc.net/problem/2386

# #을 입력할 때까지 반복합니다.
while True:
    # 문제를 입력합니다.
    # 하나의 소문자와 영어 문장이 공백으로 구분해 입력합니다.
    # 문장의 길이는 1에서 250입니다.
    question = input()

    # 입력한 문제가 #이라면
    if question == '#':
        # 반복문을 탈출해 종료합니다.
        break

    # 입력한 문제에서 알파벳과 문장을 분리해서 각각 변수에 저장합니다.
    alphabet, sentence = question[0], question[1:].lower()

    # 문장에서 알파벳이 나타나는 횟수를 저장하는 변수를 선언합니다.
    alphabet_count = sentence.count(alphabet)

    # 출력 형식에 맞게 출력합니다.
    print(f"{alphabet} {alphabet_count}")