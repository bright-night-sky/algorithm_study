# https://www.acmicpc.net/problem/1251

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 영어 소문자로 이루어진 단어를 입력합니다.
# 맨 끝에 붙는 \n은 떼줍니다.
# 길이는 3 이상 50 이하입니다.
word = stdin.readline().rstrip()
# 입력한 단어의 길이를 저장하는 변수를 선언합니다.
word_len = len(word)
# 문제에 나온 과정을 지나고 나온 단어들을 저장할 리스트 변수를 선언합니다.
divided_words = []

# 입력한 단어를 세 부분으로 나눌 때 더 앞부분에 있는 나누는 인덱스를 반복해봅니다.
# 인덱스  1부터 단어의 길이보다 2 작은 인덱스까지 반복합니다.
for first_cut in range(1, word_len - 2):
    # 입력한 단어를 세 부분으로 나눌 때 더 뒷부분에 있는 나누는 인덱스를 반복해봅니다.
    # first_cut + 1부터 단어의 길이 끝까지 반복합니다.
    for second_cut in range(first_cut + 1, word_len):
        # 세 단어로 나누고 나서 각 단어들을 저장하는 변수를 선언합니다.
        first_section = word[:first_cut]
        center_section = word[first_cut:second_cut]
        last_section = word[second_cut:]

        # 세 단어들을 각각 뒤집고 난 뒤 이어붙인 값을 저장하는 변수를 선언합니다.
        concatenation = first_section[::-1] + center_section[::-1] + last_section[::-1]
        # 과정을 지나고 나온 단어를 divided_words 리스트 변수에 넣어줍니다.
        divided_words.append(concatenation)

# divided_words에 있는 단어들을 사전순으로 오름차순 하고 난 뒤
# 맨 앞에 있는 단어를 출력해줍니다.
print(sorted(divided_words)[0])

