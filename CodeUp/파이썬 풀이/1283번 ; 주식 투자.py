# https://codeup.kr/problem.php?id=1283

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 투자한 액수 a를 입력합니다.
# 100 <= a <= 10,000
# int형으로 변환합니다.
a = int(stdin.readline())
# 둘째 줄에 투자 일수 b를 입력합니다.
# 1 <= b <= 10
b = stdin.readline()
# 날짜 개수 b개만큼 일별 변동폭을 퍼센트 정수로 공백으로 구분해 입력합니다.
# -100 ~ 100
# 각각 int형으로 변환합니다.
fluctuations = map(int, stdin.readline().split())
# 투자 후 최종 수익을 저장할 변수를 선언합니다.
# 투자한 액수 a로 초기화합니다.
gain = a

# 일별 변동폭을 하나씩 반복해봅니다.
for fluctuation in fluctuations:
    # 현재 수익인 gain의 값에 현재 변동폭에 대한 계산을 하고 그 값을 다시 gain에 저장합니다.
    gain = gain + gain * fluctuation * 0.01

# 최중 수익인 gain의 값에서 처음 투자한 액수 a의 값을 빼 순수익을 구하고 변수에 저장합니다.
net_gain = gain - a
# 순수익인 net_gain의 값을 소수점 첫째 자리에서 반올림하여 출력합니다.
print('%.0f' % net_gain)

# 순수익이 0보다 크다면
if net_gain > 0:
    # 이득이므로 문자열 'good'을 출력합니다.
    print('good')
# 순수익이 0이라면
elif net_gain == 0:
    # 본전이므로 문자열 'same'을 출력합니다.
    print('same')
# 그 외의 경우인 순수익이 0보다 작다면
else:
    # 손해이므로 문자열 'bad'를 출력합니다.
    print('bad')