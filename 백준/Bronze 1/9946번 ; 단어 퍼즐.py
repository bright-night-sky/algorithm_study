# https://www.acmicpc.net/problem/9946

case = 1

while True:
    origin = input()

    if origin == 'END':
        print('END')
        break
    else:
        origin = list(origin)
        drop_word = list(input())

        is_collect = 'same'

        for alphabet in origin:
            if alphabet in drop_word:
                origin.remove(alphabet)
                drop_word.remove(alphabet)
            else:
                is_collect = 'different'

        if origin == drop_word == []:
            print(f"Case {case}: {is_collect}")
        else:
            is_collect = 'different'
            print(f"Case {case}: {is_collect}")

        case += 1