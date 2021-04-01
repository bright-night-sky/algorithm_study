# https://www.acmicpc.net/problem/2596

# 첫 줄에는 문자의 개수를 입력합니다.
# 10보다 작습니다.
char_num = int(input())

# 두 번째 줄에는 문자의 개수의 여섯 배만큼의 숫자를 입력합니다.
string = input()

# A ~ H와 대응되는 숫자 여섯 개를 dictionary로 만듭니다.
AtoH = {
    '000000': 'A',
    '001111': 'B',
    '010011': 'C',
    '011100': 'D',
    '100110': 'E',
    '101001': 'F',
    '110101': 'G',
    '111010': 'H'
}

# 결과를 저장하는 변수입니다.
result = ''

# 입력받은 01 형태의 문자열을 6개 단위로 자르면서 돌려봅니다.
for i in range(0, len(string), 6):
    cur_char = string[i:i+6]

    result += AtoH[cur_char]

print(result)