N = int(input())
numbers = list(map(int,input().split()))
target = int(input())

numbers.sort()
s, e = 0, N-1
tmp = 0
cnt = 0
while s<e:
    tmp = numbers[s] + numbers[e]
    if tmp<target:
        s += 1
    elif tmp>target:
        e -=1
    else:
        cnt += 1
        s+=1
print(cnt)