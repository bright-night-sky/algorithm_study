# https://codeup.kr/problem.php?id=1254

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 시작 알파벳과 마지막 알파벳을 공백으로 구분해 입력합니다.
# 소문자만 입력되고, 사전순입니다.
# 입력한 알파벳들에 대한 유니코드를 구하고 각각 변수에 저장합니다.
alphabet1_unicode, alphabet2_unicode = map(ord, stdin.readline().rstrip().split())

# 시작 알파벳의 유니코드부터 마지막 알파벳의 유니코드까지 반복해봅니다.
for alphabet in range(alphabet1_unicode, alphabet2_unicode + 1):
    # 현재 유니코드에 해당하는 알파벳을 출력하고, 다음 줄로 내리지 않고 한 칸만 띄어줍니다.
    print(chr(alphabet), end=' ')