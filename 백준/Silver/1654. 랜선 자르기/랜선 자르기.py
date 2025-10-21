k, target = map(int,input().split()) # 가지고 있는 랜선의 개수 k, 필요한 랜선의 개수 target
l = [int(input()) for _ in range(k)] # 랜선 입력받아 리스트로 만들기!

start = 1
end = max(l)
answer = 0

while start<=end:
    total = 0
    mid = (start+end)//2
    for lan in l:
        if lan>=mid:
            total += lan//mid
    if total >= target: # 더 많이 자름 -> 자르는 단위를 늘려야함 -> mid 늘림
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)