# https://www.acmicpc.net/problem/15904

# 첫 번째 줄에 알파벳 대소문자, 공백으로 구성된 문자열을 입력합니다.
# 문자열의 길이는 최대 1,000자입니다.
# 문자열의 맨 앞, 맨 끝에 공백은 없고, 공백이 연속해서 2번 이상 주어지는 경우도 없습니다.
string = input()

words = string.split(' ')

abbreviation = ''

for word in words:
    first_alphabet = word[0]

    if ord('A') <= ord(first_alphabet) <= ord('Z'):
        abbreviation += first_alphabet

if abbreviation == 'UCPC':
    print("I love UCPC")
else:
    print("I hate UCPC")