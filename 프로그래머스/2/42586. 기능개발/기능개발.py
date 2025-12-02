# 1. progresses[i] = progresses[i] + speeds[i]
# 2. 100이상이 되면 popleft() 해주고? cnt해서 answer.append(cnt)
from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []
    
    while progresses:
        cnt = 0
        
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
        if progresses[0] >= 100:
            while progresses and progresses[0] >= 100:
                progresses.popleft()
                speeds.popleft()
                cnt += 1
            answer.append(cnt)

    return answer