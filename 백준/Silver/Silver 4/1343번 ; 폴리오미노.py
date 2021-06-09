# https://www.acmicpc.net/problem/1343

from sys import stdin

board = stdin.readline().rstrip()
board_len = len(board)
result = ''

idx = 0
while idx < board_len:
    if board[idx:idx + 4] == 'XXXX':
        result += 'AAAA'
        idx += 4
    elif board[idx:idx + 2] == 'XX':
        result += 'BB'
        idx += 2
    elif board[idx:idx + 2] == 'X.' or board[idx:idx + 4] == 'XXX.':
        result = -1
        break
    elif board[idx] == '.':
        result += '.'
        idx += 1

print(result)