# https://www.acmicpc.net/problem/13877

# 첫 번째 줄에는 테스트 케이스의 개수 T를 입력합니다.
# 자연수이고, 1 <= T <= 10000
T = int(input())

# 테스트 케이스의 개수만큼 돌려봅니다.
for i in range(0, T):
    # 테스트 데이터의 번호 K와 10진수로 표현된 문자열을 입력합니다.
    # 문자열의 길이는 7보다 작거나 같고, 0으로 시작할 수 있습니다.
    test_id, ten_num = map(int, input().split(' '))

    # 10진수로 입력된 수를 8진법과 16진법으로 변환해서 저장하는 변수입니다.
    # oct 함수에 의해 앞에 붙는 '0o'와
    # hex 함수에 의해 앞에 붙는 '0x'는 떼어줍니다.
    oct_num = oct(ten_num)[2:]
    hex_num = hex(ten_num)[2:]

    # 결과를 출력합니다.
    print(f"{test_id} {oct_num} {ten_num} {hex_num}")