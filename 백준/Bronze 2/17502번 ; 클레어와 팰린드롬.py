# https://www.acmicpc.net/problem/17502

# 첫 번째 줄에 문자열의 길이 N을 입력합니다.
# 1 <= N <= 100
N = int(input())

# 두 번째 줄에는 일부 문자들이 지워진 길이가 N인 팰린드롬 문자열을 입력합니다.
# 알파벳 소문자이거나 ?입니다.
palindrome = input()

if N % 2 == 1 and palindrome[int(len(palindrome) / 2)] == '?':
    palindrome[int(len(palindrome) / 2)] = 'a'

for index in range(int(len(palindrome) / 2)):
    if palindrome[index] == '?' and palindrome[-(index+1)] == '?':
        
        palindrome[index] = 'a'
        palindrome[-(index+1)] = 'a'
    elif palindrome[index] == '?':
        palindrome[-(index+1)] = palindrome[index]
    elif palindrome[-(index+1)] == '?':
        palindrome[index] = palindrome[-(index+1)]

print(palindrome)