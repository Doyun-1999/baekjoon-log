n = int(input())
score = list(map(int, input().split()))
newscore = []
m = max(score)
for i in score:
    newscore.append(i/m*100)
print(sum(newscore)/n)