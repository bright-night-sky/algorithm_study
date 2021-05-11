# https://www.acmicpc.net/problem/5704

# *을 입력할 때까지 반복합니다.
while True:
    # 단어는 공백 하나로 구분되어 있고 소문자로만 이루어진 한 문장을 입력합니다.
    # 길이는 200글자 미만입니다.
    sentence = input()

    # 입력한 문장이 팬그림인지의 여부를 저장하는 변수를 선언합니다.
    # 처음에는 팬그램이 맞다는 뜻인 문자열 Y로 초기화합니다.
    is_pangram = 'Y'

    # 입력한 문장이 *이라면
    if sentence == '*':
        # 반복문을 탈출하고 종료시킵니다.
        break
    # 입력한 문장이 다른 문장이라면
    else:
        # 알파벳 소문자 a에서 z까지 반복해봅니다.
        for alphabet in range(97, 123):
            # 입력한 문장에서 현재 알파벳 소문자가 없다면
            if sentence.find(chr(alphabet)) == -1:
                # 팬그램 여부를 N으로 바꿉니다.
                is_pangram = 'N'
                # 알파벳을 검사하고 있는 반복문을 탈출합니다.
                break

        # 입력한 문장의 팬그램 여부를 출력합니다.
        print(is_pangram)