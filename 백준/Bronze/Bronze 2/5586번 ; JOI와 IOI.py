# https://www.acmicpc.net/problem/5586

# 첫째 줄에 알파벳 10000자 이내의 문자열을 입력합니다.
string = input()

# 문자열에서 JOI의 개수를 저장할 변수를 선언합니다.
JOI_count = 0
# 문자열에서 IOI의 개수를 저장할 변수를 선언합니다.
IOI_count = 0

# 입력한 문자열의 첫 번째 글자에서 뒤에서 3번째 글자까지 반복합니다.
for index in range(0, len(string)-2):
    # 현재 글자에서 뒤의 두 글자까지의 단어가 JOI라면
    if string[index:index+3] == "JOI":
        # JOI의 개수에 1을 더해줍니다.
        JOI_count += 1
    # 현재 글자에서 뒤의 두 글자까지의 단어가 IOI라면
    elif string[index:index+3] == "IOI":
        # IOI의 개수에 1을 더해줍니다.
        IOI_count += 1
    # 다른 단어라면
    else:
        # 그냥 다음 글자로 넘어갑니다.
        continue

# JOI의 개수를 출력합니다.
print(JOI_count)
# IOI의 개수를 출력합니다.
print(IOI_count)