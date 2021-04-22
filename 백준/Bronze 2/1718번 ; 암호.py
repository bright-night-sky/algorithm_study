# https://www.acmicpc.net/problem/1718

# 첫째 줄에 평문을 입력합니다.
plain_text = input()

# 둘째 줄에 암호화 키를 입력합니다.
cipher_key = input()

PLAIN_TEXT_LENGTH = len(plain_text)
CIPHER_KEY_LENGTH = len(cipher_key)

ciphered_text = ""

for i in range(0, PLAIN_TEXT_LENGTH, CIPHER_KEY_LENGTH):
    for j in range(CIPHER_KEY_LENGTH):
        if plain_text[j] != " ":
            plain_alphabet = plain_text[i+j]
            cipher_alphabet = cipher_key[j]

            ciphered_alphabet = ord(plain_alphabet) - (ord(plain_alphabet) - ord(cipher_alphabet))

            if ciphered_alphabet < 91:
                ciphered_alphabet += 26
                ciphered_text += chr(ciphered_alphabet)
            else:
                ciphered_text += chr(ciphered_alphabet)
        else:
            ciphered_text += " "

print(ciphered_text)