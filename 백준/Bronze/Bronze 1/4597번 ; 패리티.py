# https://www.acmicpc.net/problem/4597

# #을 입력할 때까지 반복합니다.
while True:
    # 비트 스트링 하나를 입력합니다.
    # 길이는 1 ~ 31비트입니다.
    # 마지막 문자는 e 또는 o입니다.
    bit_string = input()

    # 입력한 비트 스트링이 #이라면
    if bit_string == '#':
        # 반복문을 탈출하고 종료합니다.
        break
    # 입력 형식에 맞게 비트 스트링을 입력했다면
    else:
        # 비트 스트링에서 1의 개수를 저장하는 변수를 선언합니다.
        one_count = bit_string.count('1')

        # 비트 스트링의 마지막 글자가 e라면
        if bit_string[-1] == 'e':
            # 비트 스트링에서 1의 개수가 홀수라면
            if one_count % 2 == 1:
                # 비트 스트링의 마지막 글자를 1로 바꿔줍니다.
                bit_string = bit_string[:-1] + '1'
            # 비트 스트링에서 1의 개수가 짝수라면
            else:
                # 비트 스트링의 마지막 글자를 0으로 바꿔줍니다.
                bit_string = bit_string[:-1] + '0'
        # 비트 스트링의 마지막 글자가 o라면
        else:
            # 비트 스트링에서 1의 개수가 홀수라면
            if one_count % 2 == 1:
                # 비트 스트링의 마지막 글자를 0으로 바꿔줍니다.
                bit_string = bit_string[:-1] + '0'
            # 비트 스트링에서 1의 개수가 짝수라면
            else:
                # 비트 스트링의 마지막 글자를 1로 바꿔줍니다.
                bit_string = bit_string[:-1] + '1'

        # 올바른 비트로 바꾼 비트 스트링을 출력합니다.
        print(bit_string)