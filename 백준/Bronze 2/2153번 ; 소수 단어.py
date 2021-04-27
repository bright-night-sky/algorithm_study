# https://www.acmicpc.net/problem/2153

# 입력한 영어 단어의 숫자가 소수인지 판별하는 함수를 구현합니다.
# 숫자 하나를 받는 함수로 만듭니다.
def is_prime(num):
    # 받은 숫자가 1이 아니라면
    if num != 1:
        # 2부터 받은 숫자의 절반까지 반복해봅니다.
        for i in range(2, num // 2 + 1):
            # 받은 숫자를 현재 반복 중인 숫자로 나누어 떨어진다면
            if num % i == 0:
                # 소수가 아니므로 False를 반환합니다.
                return False
        # 위의 반복문 중간에 반환되지 않는다면 소수이므로, True를 반환합니다.
        return True
    # 받은 숫자가 1이라면
    else:
        # 이 문제에서는 1도 소수로 취급하기로 했으므로
        # True를 반환합니다.
        return True

# 단어를 하나 입력합니다.
# 길이는 20자 이하이며, 알파벳 대소문자로만 이루어져 있습니다.
word = input()

# 입력받은 영단어의 숫자를 저장하는 변수를 선언합니다.
word_num = 0

# 영단어의 알파벳 하나씩 반복해봅니다.
for alphabet in word:
    # 현재 알파벳의 아스키 코드를 저장하는 변수를 선언합니다.
    alphabet_ascii = ord(alphabet)

    # 현재 알파벳이 A ~ Z라면
    if ord('A') <= alphabet_ascii <= ord('Z'):
        # 대문자에 일치하는 숫자를 더해주기 위해
        # 대문자의 아스키 코드에 38을 빼서 word_num에 더해줍니다.
        word_num += alphabet_ascii - 38
    # 현재 알파벳이 a ~ z라면
    elif ord('a') <= alphabet_ascii <= ord('z'):
        # 소문자에 일치하는 숫자를 더해주기 위해
        # 소문자의 아스키 코드에 96을 빼서 word_num에 더해줍니다.
        word_num += alphabet_ascii - 96

# 영단어 숫자가 소수라면
if is_prime(word_num):
    # It is a prime word.를 출력합니다.
    print("It is a prime word.")
# 영단어 숫자가 소수가 아니라면
else:
    # It is not a prime word.를 출력합니다.
    print("It is not a prime word.")