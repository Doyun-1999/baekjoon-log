n = int(input())
l = list(map(int, input().split()))
cnt = 0

for i in l:
    if i < 2:
        continue
    isPrime = True
    for j in range(2,int(i/2)+1):
        if(i%j ==0):
            isPrime = False
            break;
    if isPrime :
        cnt += 1

print(cnt)