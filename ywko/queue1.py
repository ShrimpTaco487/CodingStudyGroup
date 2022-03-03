def solution(priorities, location):
    answer = 0
    temp_k = 0
    temp_loca = location
    while 1:
        temp_prior = priorities.pop(0)
        for i in priorities:
            if temp_prior < i:
                priorities.append(temp_prior)
                temp_k = 1
                break
        if temp_k == 1:
            temp_k = 0
            if temp_loca == 0:
                temp_loca = len(priorities) - 1
            else:
                temp_loca -= 1
        else:
            temp_k = 0
            answer += 1
            if temp_loca == 0:
                break
            else:
                temp_loca -= 1
            
    return answer
