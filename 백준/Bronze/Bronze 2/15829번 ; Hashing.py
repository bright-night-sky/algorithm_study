# https://www.acmicpc.net/problem/15829

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 줄에는 문자열의 길이 L을 입력합니다.
# 1 <= L <= 50
# 정수형으로 변환합니다.
L = int(stdin.readline())
# 둘째 줄에는 영문 소문자로만 이루어진 문자열을 입력합니다.
# 맨 끝의 \n은 떼어줍니다.
string = stdin.readline().rstrip()
# 해시 값을 계산할 때 필요한 r, M의 값을 저장하는 변수를 선언합니다.
r = 31
M = 1234567891
# mod M을 구하기 전의 ai * r^i의 합계를 저장할 변수를 선언합니다.
ar_sum = 0

# 입력한 문자열에서 한 글자씩 반복합니다.
for idx in range(L):
    # 현재 글자의 고유 번호를 저장하는 변수를 선언합니다.
    ai = ord(string[idx]) - ord('a') + 1
    # 현재 글자의 ai * r^i 값을 ar_sum에 더해줍니다.
    ar_sum += ai * (r ** idx)

# 해시 값인 ar_sum을 M으로 나눈 뒤의 나머지의 값을 출력합니다.
print(ar_sum % M)