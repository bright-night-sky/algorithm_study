# https://www.acmicpc.net/problem/12605

# 첫 행에는 전체 케이스의 개수 N을 입력합니다.
# N = 5입니다.
N = int(input())

# 테스트 케이스의 개수 N만큼 반복합니다.
for test_case_num in range(N):
    # L개의 알파벳을 가진 단어들을 입력합니다.
    # 공백으로 구분해 리스트 변수에 넣어줍니다.
    words = input().split(' ')

    # words에 저장되어 있는 단어들을 공백으로 구분해 반대 순서대로 저장한 변수를 선언합니다.
    reverse_words = ' '.join(words[::-1])

    # 출력 형식에 맞게 출력합니다.
    print(f"Case #{test_case_num + 1}: {reverse_words}")