# https://www.acmicpc.net/problem/10769

# 첫 줄에 최소 1개에서 최대 255개의 문자들을 입력합니다.
message = input()

# 행복한 얼굴 이모티콘 :-)의 개수를 저장하는 변수를 선언합니다.
happy_emoticon_count = 0
# 슬픈 얼굴 이모티콘 :-(의 개수를 저장하는 변수를 선언합니다.
sad_emoticon_count = 0

# 입력한 문자들을 한 글자씩 반복합니다.
for index in range(len(message)):
    # 현재 문자가 :라면
    if message[index] == ':':
        # :로부터 뒤의 2개의 글자까지를 하나의 이모티콘으로 저장하는 변수를 선언합니다.
        emoticon = message[index:index+3]

        # 현재 이모티콘이 :-)이라면
        if emoticon == ':-)':
            # :-) 개수 변수에 1을 더해줍니다.
            happy_emoticon_count += 1
        # 현재 이모티콘이 :-(이라면
        elif emoticon == ':-(':
            # :-( 개수 변수에 1을 더해줍니다.
            sad_emoticon_count += 1

# 어떤 이모티콘도 포함되어 있지 않으면
if happy_emoticon_count == 0 and sad_emoticon_count == 0:
    # none을 출력합니다.
    print("none")
# 행복한 이모티콘이 슬픈 이모티콘보다 많이 포함되어 있으면
elif happy_emoticon_count > sad_emoticon_count:
    # happy를 출력합니다.
    print("happy")
# 행복한 이모티콘이 슬픈 이모티콘보다 적게 포함되어 있으면
elif happy_emoticon_count < sad_emoticon_count:
    # sad를 출력합니다.
    print("sad")
# 행복한 이모티콘과 슬픈 이모티콘의 수가 1개 이상이며 동일하게 포함되어 있으면
elif happy_emoticon_count >= 1 and sad_emoticon_count >= 1 and happy_emoticon_count == sad_emoticon_count:
    # unsure를 출력합니다.
    print("unsure")