# https://www.acmicpc.net/problem/7785

# 첫째 줄에 로그에 기록된 출입 기록의 수 n을 입력합니다.
# 2 <= n <= 10^6
n = int(input())

in_company_people = []

for log_index in range(n):
    person_name, enter_or_leave = input().split(' ')

    if enter_or_leave == 'enter':
        in_company_people.append(person_name)
    else:
        in_company_people.remove(person_name)

in_company_people.sort(reverse=True)

for person in in_company_people:
    print(person)