# https://www.acmicpc.net/problem/9933

# 첫째 줄에 단어의 수 N을 입력합니다.
# 2 <= N <= 100
N = int(input())

# 입력한 단어들을 저장하는 리스트 변수를 선언합니다.
words = []

# 단어 중 비밀번호의 길이를 저장하는 변수를 선언합니다.
password_length = None
# 단어 중 비밀번호의 가운데 글자를 저장하는 변수를 선언합니다.
password_center = None

# 단어의 수 N만큼 반복합니다.
for word_index in range(N):
    # 단어를 하나 입력합니다.
    # 알파벳 소문자로만 이루어져 있으며, 길이는 2보다 크고 14보다 작은 홀수입니다.
    word = input()

    # 입력한 단어를 words에 넣어줍니다.
    words.append(word)

# words에서 단어 하나씩 반복해봅니다.
for word in words:
    # 현재 단어의 역순인 단어가 words에 있다면
    if word[::-1] in words:
        # 그 단어가 비밀번호이므로
        # 비밀번호의 길이를 저장합니다.
        password_length = len(word)
        # 비밀번호의 가운데 글자를 저장합니다.
        password_center = word[password_length // 2]
        # 정답은 하나뿐이므로 정답을 찾았으니 반복문을 탈출합니다.
        break

# 출력 형식에 맞게 비밀번호의 길이와 가운데 글자를 출력합니다.
print(password_length, password_center)