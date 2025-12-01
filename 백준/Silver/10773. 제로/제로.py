# 그냥 전형적인 스택 문제 -> 배열에 append, pop을 반복하면서 최종합을 구하는 문제이다
N = int(input())
num = [int(input()) for _ in range(N)]
answer = []

for i in num:
    if i != 0:
        answer.append(i)
    else:
        answer.pop(len(answer)-1)

print(sum(answer))