# people의 범위가 1<=people<=50,000 이니까 시간복잡도는 꽤 널널함.
# 정렬을 해서 투포인터로 가자
# 가장 돼지랑 가장 멸치랑 같이 태우면 효율 올라감
#

def solution(people, limit):
    people.sort()
    i = 0
    j = len(people) - 1
    boat = 0

    while i <= j:
        # 둘이 함께 탈 수 있으면
        if people[i] + people[j] <= limit:
            i += 1  # 가벼운 사람도 탑승
        # 무거운 사람은 항상 탑승 (짝을 못 찾았거나 혼자 탑승)
        j -= 1
        boat += 1

    return boat