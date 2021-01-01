# https://www.acmicpc.net/problem/18258

order_num = int(input())
queue = []

for i in range(0, order_num):
    order = input().split(' ')

    if order[0] == 'push':
        queue.append(int(order[1]))
    elif order[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.pop(0)
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
