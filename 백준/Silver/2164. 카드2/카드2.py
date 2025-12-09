from collections import deque

N = int(input())
cards = deque()
tmp = 0

for i in range(1,N+1):
    cards.append(i)

while len(cards) > 1:
    cards.popleft()
    tmp = cards.popleft()
    cards.append(tmp)
    
print(cards[0])