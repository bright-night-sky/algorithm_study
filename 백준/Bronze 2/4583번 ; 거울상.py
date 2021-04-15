# https://www.acmicpc.net/problem/4583

# 거울상 관계 알파벳들을 리스트 변수에 넣어줍니다.
reflect = ['b', 'd', 'p', 'q', 'i', 'o', 'v', 'w', 'x']

# #을 입력할 때까지 반복합니다.
while True:
    # 소문자로만 이루어진 단어를 입력합니다.
    # 단어의 길이는 10을 넘지 않습니다.
    word = input()

    # 입력한 단어가 #이라면
    if word == '#':
        # 끝내기 위해 반복문을 탈출합니다.
        break

    # 결과를 저장하는 변수를 선언합니다.
    result = ''

    # 입력받은 단어의 알파벳 한 글자씩 반복합니다.
    for alphabet in word:
        # 현재 알파벳이 거울상 관계 알파벳이 아니라면
        if alphabet not in reflect:
            # 결과 변수에 INVALID를 저장합니다.
            result = "INVALID"
            # 이 단어는 거울에 비춰지기 전 모습을 표현할 수 없으므로 반복문을 탈출합니다.
            break
        # 현재 알파벳이 거울상 관계 알파벳이라면
        else:
            # 거울상 관계 알파벳 중 b라면
            if alphabet == 'b':
                # b와 거울상 관계인 d를 결과 변수에 넣어줍니다.
                result += 'd'
            # 거울상 관계 알파벳 중 d라면
            elif alphabet == 'd':
                # d와 거울상 관계인 b를 결과 변수에 넣어줍니다.
                result += 'b'
            # 거울상 관계 알파벳 중 p라면
            elif alphabet == 'p':
                # p와 거울상 관계인 q를 결과 변수에 넣어줍니다.
                result += 'q'
            # 거울상 관계 알파벳 중 p라면
            elif alphabet == 'q':
                # q와 거울상 관계인 p를 결과 변수에 넣어줍니다.
                result += 'p'
            # 그 외의 거울상 관계 알파벳이라면
            else:
                # 자신과 거울상 관계이므로 그대로 결과 변수에 넣어줍니다.
                result += alphabet

    # 결과 변수에 INVALID가 아닌 다른 문자가 저장되어 있으면
    # 현재 단어는 거울에 비춰지기 전 모습을 표현할 수 있습니다.
    if result != 'INVALID':
        # 결과 변수의 값을 역순으로 출력하여 그 거울상의 모습을 출력합니다.
        print(result[::-1])
    # 결과 변수에 INVALID가 저장되어 있다면
    else:
        # INVALID를 출력합니다.
        print(result)
