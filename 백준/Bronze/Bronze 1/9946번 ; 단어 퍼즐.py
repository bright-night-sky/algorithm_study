# https://www.acmicpc.net/problem/9946

from sys import stdin

while True:
    junha_word = stdin.readline().rstrip()
    collect_word = stdin.readline().rstrip()

    case_index = 1
    is_complete_collect = "same"

    if junha_word == collect_word == 'END':
        break
    else:
        junha_word = list(junha_word)
        collect_word = list(collect_word)

        for alphabet in junha_word:
            if alphabet in collect_word:
                collect_word.remove(alphabet)
            else:
                is_complete_collect = "different"
                break

        if collect_word != []:
            is_complete_collect = "different"
            print(f"Case {case_index}: {is_complete_collect}")
        else:
            print(f"Case {case_index}: {is_complete_collect}")

        case_index += 1