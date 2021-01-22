# https://www.acmicpc.net/problem/4690

for a in range(6, 101):
    for b in range(2, 98):
        for c in range(b+1, 99):
            for d in range(c+1, 100):
                if (a * a * a) == (b * b * b) + (c * c * c) + (d * d * d):
                    print(f"Cube = {a}, Triple = ({b},{c},{d})")
                elif (a * a * a) < (b * b * b) + (c * c * c) + (d * d * d):
                    break
