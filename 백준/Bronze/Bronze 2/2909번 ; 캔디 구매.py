# https://www.acmicpc.net/problem/2909

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 사탕의 가격 C,
# 상근이가 가지고 있는 지폐의 액면가에 적혀있는 0의 개수 K를 공백으로 구분해 입력합니다.
# 0 <= C <= 1,000,000,000
# 0 <= K <= 9
# 각각 정수형으로 변환합니다.
C, K = map(int, stdin.readline().split(' '))

# 사탕의 가격의 길이와 지폐의 0의 개수가 같고, 사탕 가격 맨 앞의 숫자가 5라면
if len(str(C)) == K and str(C)[0] == '5':
    # 사탕의 가격 맨 앞의 5에서 반올림한 결과를 출력합니다.
    print('1' + '0' * K)
# 그 외의 경우에는
else:
    # 사탕의 가격 뒤에서부터 세어 K번째 자리에서 반올림한 결과를 출력합니다.
    print(round(C, -K))