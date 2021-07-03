# https://www.acmicpc.net/problem/17502

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 번째 줄에 문자열의 길이 N을 입력합니다.
# 1 <= N <= 100
# 정수형으로 변환합니다.
N = int(stdin.readline())
# 두 번째 줄에는 일부 문자들이 지워진 길이가 N인 팰린드롬 문자열을 입력합니다.
# 각 문자는 알파벳 소문자이거나 '?'입니다.
# 맨 끝의 \n은 떼어주고 리스트 변수로 만들어줍니다.
palindrome = list(stdin.readline().rstrip())

# 팰린드롬의 길이 N의 절반만큼 반복합니다.
for idx in range(N // 2):
    # 팰린드롬의 현재 인덱스의 문자는 ?가 아닌데, 현재 인덱스를 끝부터 세었을 때의 문자는 ?라면
    if palindrome[idx] != '?' and palindrome[-idx-1] == '?':
        # 현재 인덱스를 끝부터 세었을 때의 문자를 현재 인덱스의 문자로 바꿔줍니다.
        palindrome[-idx-1] = palindrome[idx]
    # 팰린드롬의 현재 인덱스의 문자는 ?인데, 현재 인덱스를 끝부터 세었을 때의 문자는 ?가 아니라면
    elif palindrome[idx] == '?' and palindrome[-idx-1] != '?':
        # 현재 인덱스의 문자를 현재 인덱스를 끝부터 세었을 때의 문자로 바꿔줍니다.
        palindrome[idx] = palindrome[-idx-1]
    # 팰린드롬의 현재 인덱스의 문자와 현재 인덱스를 끝부터 세었을 때의 문자 모두 ?라면
    elif (palindrome[idx], palindrome[-idx-1]) == ('?', '?'):
        # 현재 인덱스의 문자와 현재 인덱스를 끝부터 세었을 때의 문자를 모두 a로 바꿔줍니다.
        palindrome[idx] = 'a'
        palindrome[-idx-1] = 'a'

# 팰린드롬의 길이가 홀수일 때, 가운데 글자가 ?라면
if palindrome[N // 2] == '?':
    # 가운데 글자를 a로 바꿔줍니다.
    palindrome[N // 2] = 'a'

# 팰린드롬이 된 문자열을 출력합니다.
print(''.join(palindrome))