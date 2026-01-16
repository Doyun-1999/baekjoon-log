from collections import deque
# 결국 문제는 진실을 아는사람 = 좀비 정도로 생각하고
# 감염되어 퍼진다고 생각해야함!
# 그래서 진실을 아는사람과 붙은 사람이 있으면 그사람은 다 진실을 아는사람으로 변경됨
# 약간 0,1을 사용하는 bfs/dfs 탐색문제 같은 느낌을 받아야한다.

N , M = map(int,input().split()) # N = 사람수 , M = 파티의 개수 
temp = list(map(int, input().split()))

if temp[0] == 0:
    truth_people = [] # 아무도 모름
else:
    truth_people = temp[1:] # 첫 번째 숫자는 '수'니까 제외하고 나머지 번호만 저장

parties = [list(map(int, input().split()))[1:] for _ in range(M)]

# 이제부터 진실을 아는사람과 같은 파티에 있는사람은 -> truth_people.append()
# not in truth_people 이면 cnt += 1 하는거 어떤가..? 약간 그래프가아닌가이러면
# 이방법은 순서가 잘못됌 ㅠㅠ 나중에 만나더라도 구라친거 걸리네..
# 그니까 미리 접촉할애들을 다 노드로 만들어놓고? 이후에 cnt 하는게 정확함

# 2. 인접 리스트(접촉 지도) 구축
# 누가 누구랑 만났는지 기록합니다.
adj = [[] for _ in range(N + 1)]
for party in parties:
    # 한 파티 내의 모든 사람들을 서로 연결
    for i in range(len(party)):
        for j in range(i + 1, len(party)):
            p1, p2 = party[i], party[j]
            adj[p1].append(p2)
            adj[p2].append(p1)

# 3. BFS를 이용한 진실 전염
know_truth = [False] * (N + 1)
queue = deque(truth_people)

# 초기 감염자 설정
for p in truth_people:
    know_truth[p] = True

while queue:
    curr = queue.popleft()
    for neighbor in adj[curr]:
        if not know_truth[neighbor]:
            know_truth[neighbor] = True
            queue.append(neighbor)

# 4. 거짓말 할 수 있는 파티 카운트
ans = 0
for party in parties:
    can_lie = True
    for p in party:
        if know_truth[p]: # 이 파티에 좀비(진실을 아는 자)가 한 명이라도 있으면
            can_lie = False
            break
    if can_lie:
        ans += 1

print(ans)         