# https://www.acmicpc.net/problem/1371

from sys import stdin

sentences = ''

while True:
    try:
        sentence = stdin.readline()
        sentences += sentence
    except EOFError:
        break

alphabet_count = []

for alphabet_ascii in range(ord('a'), ord('z') + 1):
