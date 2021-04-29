# https://www.acmicpc.net/problem/10814

# 첫째 줄에는 온라인 저지 회원의 수 N을 입력합니다.
# 1 <= N <= 100,000
N = int(input())

# 회원들의 정보를 넣을 리스트 변수를 선언합니다.
members = []

# 회원의 수 N만큼 반복해봅니다.
for order in range(N):
    # 회원 한 명의 정보를 저장하는 리스트 변수를 선언합니다.
    # 가입 순서가 필요하므로 넣어줍니다.
    member = [order]

    # 회원의 나이와 이름을 공백으로 구분해 입력합니다.
    age, name = input().split(' ')

    # member 리스트 변수에 나이와 이름을 넣어줍니다.
    # 나이는 정수형으로 변환해서 넣어줍니다.
    member.append(int(age))
    member.append(name)

    # 이번 회원의 정보를 저장한 member 리스트 변수를 members 리스트 변수에 넣어줍니다.
    members.append(member)

# members 내부의 리스트들을 첫 번째로 나이순, 두 번째로 가입 순서순 기준으로 오름차순 정렬을 해줍니다.
members.sort(key=lambda member: (member[1], member[0]))

# 정렬된 회원들의 나이와 이름을 출력 형식에 맞게 차례대로 출력합니다.
for member in members:
    print(member[1], member[2])