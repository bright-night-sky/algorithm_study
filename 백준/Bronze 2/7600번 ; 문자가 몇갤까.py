# https://www.acmicpc.net/problem/7600

# 마지막 줄의 #이 입력될 때까지 계속 한 문장씩 입력받고
# 알파벳의 개수를 출력하는 것을 반복합니다.
while True:
    # 한 문장을 입력합니다.
    # 250자를 넘지 않는 문장입니다.
    # 대문자와 소문자는 같은 알파벳으로 처리해야하므로
    # 입력받은 문장에서 알파벳은 모두 대문자로 바꿔줍니다.
    sentence = input().upper()

    # 입력받은 문장이 #인 경우에는
    if sentence == '#':
        # 반복문을 탈출하고 종료합니다.
        break

    # 알파벳 종류의 개수를 저장할 변수를 선언합니다.
    alphabet_count = 0

    # 입력한 문장에서 A부터 Z까지 반복해보면서 있는지 판단해봅니다.
    for i in range(ord('A'), ord('Z')+1):
        # 문장에서 현재 있는지 판단 중인 알파벳이 있다면
        if sentence.find(chr(i)) != -1:
            # 알파벳 종류의 개수에 1을 더해줍니다.
            alphabet_count += 1

    # 알파벳 종류의 개수를 출력합니다.
    print(alphabet_count)