# https://www.acmicpc.net/problem/3052

# 42로 나눈 나머지들을 저장할 set를 하나 만듭니다.
# set로 만든 이유는 입력받은 수들을 42로 나누었을 때의 나머지를 set에 추가할 때
# 똑같은 나머지를 추가해도 set 자료형은 중복이 인정되지 않으므로 하나만 남아있기 때문입니다.
remainder = set()

# 수 10개를 입력해야하므로 10번 반복합니다.
for i in range(10):
    # 숫자를 한 번 입력합니다.
    num = int(input())

    # 입력한 숫자를 42로 나누고 그 나머지를 set인 remainder에 추가합니다.
    remainder.add(num % 42)

# remainder에 들어있는 나머지의 개수를 출력합니다.
print(len(remainder))