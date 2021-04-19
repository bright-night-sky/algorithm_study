# https://www.acmicpc.net/problem/11091

# 첫 번째 줄은 문장의 개수 N을 입력합니다.
# 1 <= N <= 50
N = int(input())

# 문장의 개수 N개만큼 반복해봅니다.
for i in range(N):
    # 한 문장을 입력합니다.
    # 알파벳의 대소문자, 공백, 숫자, 문장부호들(. , ? ! ' ")이 포함될 수 있습니다.
    # 팬그램 구별 시 대소문자를 구별하지 않고 출력 형식에는 소문자가 나오므로
    # 입력한 문자를 소문자로 처리해줍니다.
    sentence = input().lower()

    # 입력한 문장이 팬그램이 아닐 경우 문장에 나타나지 않은 알파벳을 출력하기 위해
    # 나타나지 않은 알파벳들을 저장할 변수를 선언합니다.
    missing_alphabet = ''

    # 소문자 알파벳 a부터 z까지 반복해봅니다.
    for alphabet_ascii in range(ord('a'), ord('z')+1):
        # 입력한 문장에서 현재 소문자 알파벳이 없다면
        if sentence.find(chr(alphabet_ascii)) == -1:
            # 나타나지 않은 알파벳 변수에 현재 알파벳을 추가해줍니다.
            missing_alphabet += chr(alphabet_ascii)

    # 나타나지 않은 알파벳이 하나도 없다면
    if missing_alphabet == '':
        # 팬그램이므로 pangram을 출력해줍니다.
        print("pangram")
    # 나타나지 않은 알파벳이 하나라도 있다면
    else:
        # 출력 형식에 맞게 나타나지 않은 알파벳을 출력해줍니다.
        print(f"missing {missing_alphabet}")