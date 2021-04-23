# https://www.acmicpc.net/problem/10987

# 첫째 줄에 단어를 입력합니다.
# 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며
# 알파벳 소문자로만 이루어져 있습니다.
word = input()

# 알파벳 모음 소문자를 저장한 리스트 변수를 선언합니다.
vowel = ['a', 'e', 'i', 'o', 'u']

# 모음의 개수를 저장하는 변수를 선언합니다.
vowel_count = 0

# 입력한 단어에서 한 알파벳씩 반복합니다.
for alphabet in word:
    # 현재 알파벳이 모음에 속한다면 모음의 개수에 1을 더해줍니다.
    vowel_count += vowel.count(alphabet)

# 모음의 개수를 출력합니다.
print(vowel_count)