N, K = map(int,input().split())
numbers = list(map(int,input().split()))

s,e = 0,K-1
total = 0
answer = 0

for i in range(s,K):
    total += numbers[i]
answer = total

while e+1 < N:
    total -= numbers[s]
    s += 1
    e += 1
    total += numbers[e]
    if total > answer:
        answer = total

print(answer)