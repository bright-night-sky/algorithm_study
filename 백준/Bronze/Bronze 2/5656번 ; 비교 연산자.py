# https://www.acmicpc.net/problem/5656

case = 1

while True:
    a, compare, b = input().split(' ')

    compare_result = None

    if compare == 'E':
        break
    elif compare == '>':
        if a > b:
            compare_result = "true"
        else:
            compare_result = "false"
    elif compare == '>=':
        if a >= b:
            compare_result = "true"
        else:
            compare_result = "false"
    elif compare == '<':
        if a < b:
            compare_result = "true"
        else:
            compare_result = "false"
    elif compare == '<=':
        if a <= b:
            compare_result = "true"
        else:
            compare_result = "false"
    elif compare == '==':
        if a == b:
            compare_result = "true"
        else:
            compare_result = "false"
    else:
        if a != b:
            compare_result = "true"
        else:
            compare_result = "false"

    print(f"Case {case}: {compare_result}")

    case += 1