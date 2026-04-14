def solution(arr):
    temp = 0
    answer = [] # 일단 넣고 생각해야함, 넣고 뒤에꺼가 앞에꺼랑 같다면 넣지않는식으로 수정
    for i in range(len(arr)):
        if len(answer) == 0 or (arr[i-1]!=arr[i]):
            answer.append(arr[i])
    return answer