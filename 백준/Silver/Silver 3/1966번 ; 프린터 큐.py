# https://www.acmicpc.net/problem/1966

from sys import stdin

test_case = int(stdin.readline())

for test_case_idx in range(test_case):
    N, M = map(int, stdin.readline().split(' '))
    important_queue = list(map(int, stdin.readline().split(' ')))
    marked_document = [important_queue[M], True]
    important_queue[M] = marked_document

    count = 0
    while True:
        if important_queue.count(marked_document) == 0:
            print(count + 1)
            break
        else:
            important_len = len(important_queue)
            for idx in range(1, important_len):
                if important_queue[0] == marked_document:
                    if marked_document[0] < important_queue[idx]:
                        important_queue.append(marked_document)
                        important_queue.pop(0)
                        count += 1
                    else:
                        important_queue.pop(0)
                else:
                    if important_queue[0] < important_queue[idx]:
                        important_queue.append(important_queue[0])
                        important_queue.pop(0)
                        count += 1
                    else:
                        important_queue.pop(0)