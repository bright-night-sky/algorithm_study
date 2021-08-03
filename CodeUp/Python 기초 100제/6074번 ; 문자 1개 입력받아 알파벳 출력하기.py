# https://codeup.kr/problem.php?id=6074

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 영어 소문자 1개를 입력합니다.
# 맨 끝의 \n은 떼어줍니다.
eng_char = stdin.readline().rstrip()
# 입력한 영어 소문자의 다음 영어 소문자에 해당하는 유니코드를 저장하는 변수를 선언합니다.
next_eng_char_code = ord(eng_char) + 1
# 영어 소문자 유니코드 숫자를 a의 유니코드부터 입력한 영어 소문자의 유니코드까지
# 차례로 저장할 변수를 선언합니다.
# 처음에는 a의 유니코드로 초기화합니다.
alphabet_code = ord('a')

# 현재 영어 소문자의 유니코드와 next_eng_char_code에 저장된 유니코드가 같지 않으면 계속 반복합니다.
while alphabet_code != next_eng_char_code:
    # alphabet_code에 저장된 유니코드에 해당하는 영어 소문자를 출력합니다.
    # 출력 형식에 맞게 다음 줄로 내리지 않고 다음 한 칸을 띄어줍니다.
    print(chr(alphabet_code), end=' ')
    # 다음 영어 소문자를 표현하기 위해 alphabet_code에 저장된 유니코드에 1을 더합니다.
    alphabet_code += 1