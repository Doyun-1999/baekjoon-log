# 아이디어는 투포인터! 기존 s부터 시작하여 인덱스를 늘려나가고
# 누적합을 진행함 -> 누적합 total>M 이면 -> s++
# 누적합을 진행함 -> 누적합 total<M 이면 -> e++
N, M = map(int,input().split())
lst = list(map(int,input().split()))

s,e = 0, 1
cnt = 0
total = lst[s]

while True:
    if total >= M:
        if total == M:
            cnt += 1
        total -= lst[s]
        s += 1
    elif e == N:
        break
    else:
        total += lst[e]
        e += 1
        
print(cnt)