N = int(input())
ropes = [int(input()) for _ in range(N)]
ropes.sort(reverse=True)
temp = 0
answer = 0

for i in range(len(ropes)):
    if i == 0 and answer == 0:
        temp = ropes[0]
        answer = temp
    temp = ropes[i]*(i+1)
    if temp > answer:
        answer = temp
    temp = 0
        
print(answer)