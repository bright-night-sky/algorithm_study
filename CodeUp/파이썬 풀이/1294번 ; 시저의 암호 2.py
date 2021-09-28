# https://codeup.kr/problem.php?id=1294

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 평문을 입력합니다.
# 맨 끝의 \n은 떼어줍니다.
plain = stdin.readline().rstrip()
# 입력한 평문을 시저 암호를 통해 변경한 암호문을 저장할 변수를 선언합니다.
# 빈 문자열로 초기화합니다.
cryptogram = ''

# 평문의 한 문자씩 반복해봅니다.
for char in plain:
    # 현재 문자가 공백이라면
    if char == ' ':
        # cryptogram에 공백을 추가합니다.
        cryptogram += ' '
        # 다음 문자로 넘어갑니다.
        continue

    # 현재 문자를 유니코드로 변경하고 3을 더해
    # 현재 문자의 암호 문자의 유니코드로 만들어 변수에 저장합니다.
    crypto_char_ascii = ord(char) + 3

    # 현재 문자가 알파벳 x, y, z인 경우 유니코드에 3을 더하면 소문자 알파벳의 유니코드 범위를 초과합니다.
    # 암호 문자의 유니코드가 알파벳 'z'의 유니코드보다 크다면
    if crypto_char_ascii > ord('z'):
        # 암호 문자의 유니코드에 26을 빼 알파벳 순서를 한 바퀴 돌게 만듭니다.
        crypto_char_ascii -= 26

    # 암호 문자의 유니코드를 다시 문자로 만들고 cryptogram에 넣어줍니다.
    cryptogram += chr(crypto_char_ascii)

# 암호문을 저장하고 있는 cryptogram의 값을 출력합니다.
print(cryptogram)