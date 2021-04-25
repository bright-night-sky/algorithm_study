# https://www.acmicpc.net/problem/20112

# 첫째 줄에 단어의 길이 N을 입력합니다.
# 2 <= N <= 100
N = int(input())

# 사토르 마방진인지 아닌지 판단할 단어 집합들을 저장하는 리스트 변수를 선언합니다.
wordset = []

# 사토르 마방진인지 아닌지 결과를 저장하는 변수를 선언합니다.
# 사토르 마방진이 아닌 결과를 찾을 것이므로 YES로 초기화합니다.
is_Sator_Square = "YES"

# 단어의 길이 N만큼 반복합니다.
for i in range(N):
    # 단어 하나를 입력합니다.
    word = input()
    # 입력한 단어를 wordset 변수에 넣어줍니다.
    wordset.append(word)

# 단어의 길이 N만큼 반복합니다.
for i in range(N):
    # 가로로 읽었을 때의 단어를 저장하는 변수를 선언합니다.
    row_word = ""
    # 세로로 읽었을 때의 단어를 저장하는 변수를 선언합니다.
    column_word = ""

    # wordset에서 i번째 가로 단어를 row_word에 저장합니다.
    row_word = wordset[i]

    # 위의 i번째 단어와 같은 순서인 세로 단어를 읽어봅니다.
    # 단어의 길이 N만큼 반복합니다.
    for j in range(N):
        # i번째 가로 단어일 때, 각 가로 단어들의 i번째 한 글자를 세로 단어 변수에 넣어줍니다.
        column_word += wordset[j][i]

    # 가로로 읽은 단어와 세로로 읽은 단어가 다르다면
    if row_word != column_word:
        # 사토르 마방진이 아니므로 결과 변수에 NO를 저장합니다.
        is_Sator_Square = "NO"

# 사토르 마방진인지 아닌지의 결과를 출력합니다.
print(is_Sator_Square)