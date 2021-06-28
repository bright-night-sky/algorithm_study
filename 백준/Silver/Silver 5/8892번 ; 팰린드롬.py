# https://www.acmicpc.net/problem/8892

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 테스트 케이스의 개수 T를 입력합니다.
# 정수형으로 변환합니다.
T = int(stdin.readline())

# 테스트 케이스의 개수 T만큼 반복합니다.
for test_case_idx in range(T):
    # 공책에 적혀져있는 단어의 수 k를 입력합니다.
    # 1 <= k <= 100
    # 정수형으로 변환합니다.
    k = int(stdin.readline())
    # 입력한 단어들을 저장할 리스트 변수를 선언합니다.
    words = [None] * k
    # 팰린드롬이 있는지 없는지 여부를 저장하는 변수를 선언합니다.
    # 처음에는 팰린드로이 없다는 뜻인 False로 초기화합니다.
    is_palindrome = False

    # 단어의 수 k만큼 반복합니다.
    for word_idx in range(k):
        # 알파벳 소문자로 이루어진 단어를 입력합니다.
        # 맨 끝의 \n은 떼어줍니다.
        # 단어는 words 리스트 변수에 넣어줍니다.
        words[word_idx] = stdin.readline().rstrip()

    # words에 있는 단어 2개 뽑는 것을 반복합니다.
    for i in range(0, k-1):
        for j in range(i+1, k):
            # 뽑은 단어를 입력한 순서대로 합친 것을 저장하는 변수를 선언합니다.
            word_set1 = words[i] + words[j]
            # 뽑은 단어를 입력한 순서 반대로 합친 것을 저장하는 변수를 선언합니다.
            word_set2 = words[j] + words[i]

            # word_set1이 팰린드롬이라면
            if word_set1 == word_set1[::-1]:
                # word_set1 팰린드롬을 출력합니다.
                print(word_set1)
                # 팰린드롬을 찾았으므로 is_palindrome의 값을 True로 저장합니다.
                is_palindrome = True
                # 반복문을 탈출합니다.
                break
            # word_set2이 팰린드롬이라면
            elif word_set2 == word_set2[::-1]:
                # word_set2 팰린드롬을 출력합니다.
                print(word_set2)
                # 팰린드롬을 찾았으므로 is_palindrome의 값을 True로 저장합니다.
                is_palindrome = True
                # 반복문을 탈출합니다.
                break

        # 팰린드롬을 찾았다면
        if is_palindrome:
            # 바깥 반복문도 탈출합니다.
            break

    # 팰린드롬을 만들 수 없다면
    if not is_palindrome:
        # 0을 출력합니다.
        print(0)