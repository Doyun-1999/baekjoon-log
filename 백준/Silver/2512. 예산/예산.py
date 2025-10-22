n = int(input())
budget = list(map(int,input().split()))
m = int(input())
answer = 0
start = 0
end = max(budget)

if(sum(budget)<=m):
    print(end)
else:
    while start<=end:
        total = 0
        mid = (start+end)//2
        for b in budget: 
            if b>mid:
                total += mid
            else:
                total += b
        if total <= m: # mid값을 낮추면 -> total값도 낮아짐
            answer = mid
            start = mid + 1 # start를 높이면 -> total값도 높아짐
        else:
            end = mid - 1
    print(answer)    