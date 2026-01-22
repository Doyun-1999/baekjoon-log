import sys
S = sys.stdin.readline().rstrip()
q = int(sys.stdin.readline().rstrip())
question = []
for _ in range(q):
    alpha, l, r = sys.stdin.readline().rstrip().split()
    temp = S[int(l) : int(r) + 1]
    count = 0
    for t in temp:
        if t == alpha:
            count += 1
    print(count)