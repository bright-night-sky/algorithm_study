# https://www.acmicpc.net/problem/4673

# 문제의 d(n)을 구현합니다.
def d(n):
    # 매개변수로 받은 n을 문자열로 바꿔줍니다.
    n = str(n)

    # 리턴할 결과를 저장하는 변수를 선언합니다.
    result = 0

    # 매개변수로 받은 숫자 형태의 문자열의 각 자리수만큼 반복합니다.
    for position in n:
        # 결과 변수에 각 자리 숫자를 더해줍니다.
        result += int(position)

    # 결과 변수에 매개변수로 받은 숫자 자체를 더해줍니다.
    result += int(n)

    # 결과를 리턴해줍니다.
    return result

# 셀프 넘버를 저장하는 리스트 변수를 선언해줍니다.
# 처음에는 1부터 10000까지 초기화해줍니다.
self_numbers = [num for num in range(1, 10001)]

# 1부터 10000까지 반복해봅니다.
for number in range(1, 10001):
    # 현재 숫자를 d(n) 함수에 넣어 결과를 반환한 변수를 선언합니다.
    dn = d(number)

    # dn이 10000보다 작고, self_numbers에 한 개 있다면
    if dn <= 10000 and self_numbers.count(dn) == 1:
        # self_numbers에서 dn을 지워줍니다.
        self_numbers.remove(dn)
    # 개수도 세어야하는 이유는 101과 같이 생성자가 2개 있는 경우에는
    # number가 91일 때 이미 self_numbers에서 101이 삭제되어 있으므로
    # number가 100일 때 오류가 뜨기 때문입니다.

# self_numbers에 있는 숫자를 한 줄에 하나씩 출력해줍니다.
for number in self_numbers:
    print(number)
