# https://www.acmicpc.net/problem/10173

# EOI라는 문장이 입력될 때까지 계속 반복합니다.
while True:
    # 한 문장을 입력합니다.
    # 한 문장은 최대 80개의 글자로 이루어져 있습니다.
    sentence = input()

    # 만약 입력한 문장이 EOI라면
    if sentence == "EOI":
        # 반복문을 탈출합니다.
        break

    # 니모(Nemo)를 찾는데 대소문자는 구별하지 않으므로 입력받은 문장을 대문자로 바꿔줍니다.
    sentence = sentence.upper()

    # 만약 문장에 NEMO가 있다면
    if sentence.find("NEMO") != -1:
        # Found를 출력합니다.
        print("Found")
    # 만약 문장에 NEMO가 없다면
    else:
        # Missing을 출력합니다.
        print("Missing")