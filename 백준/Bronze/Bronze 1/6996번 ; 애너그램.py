# https://www.acmicpc.net/problem/6996

# 첫째 줄에 테스트 케이스의 개수를 입력합니다.
test_case = int(input())

# 테스트 케이스의 수만큼 반복해봅니다.
for i in range(test_case):
    # 두 단어를 공백으로 구분해서 입력합니다.
    # 단어의 길이는 100을 넘지 않고, 알파벳 소문자로만 이루어져 있습니다.
    word1, word2 = input().split(' ')

    # 두 단어가 애너그램인지 여부를 저장하는 변수를 선언합니다.
    # 애너그램이 맞다는 뜻인 anagrams로 초기화합니다.
    is_anagram = "anagrams"

    # 두 단어의 길이가 다르다면 일단 애너그램이 될 수 없습니다.
    if len(word1) != len(word2):
        # 애너그램의 여부 변수의 값을 애너그램이 아니라는 값인 NOT anagrams로 저장합니다.
        is_anagram = "NOT anagrams"
        # 출력 형식에 맞게 출력합니다.
        print(f"{word1} & {word2} are {is_anagram}.")
    # 두 단어의 길이가 같다면 애너그램이 될 수도 있습니다.
    else:
        # 첫 번째 단어에서 한 글자씩 반복해봅니다.
        for alphabet in word1:
            # 첫 번째 단어의 현재 알파벳 개수와 두 번째 단어의 알파벳 개수가 다르다면
            if word1.count(alphabet) != word2.count(alphabet):
                # 애너그램이 될 수 없으므로 애너그램 여부 변수의 값을 애너그램이 아니라는 값인 NOT anagrams로 저장합니다.
                is_anagram = "NOT anagrams"
                # 반복문을 탈출합니다.
                break
            # 반복문을 중간에 탈출하지 않고 끝까지 반복하고 난 뒤에 나온다면 두 단어는 애너그램 관계가 맞습니다.

        # 출력 형식에 맞게 출력합니다.
        print(f"{word1} & {word2} are {is_anagram}.")