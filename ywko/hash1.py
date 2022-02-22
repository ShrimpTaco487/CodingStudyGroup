#42577
import re
def solution(phone_book):
    answer = True
    ha = {}
    for i in phone_book:
        ha[i] = 1
            
    for k in ha:
        temp_an = 0
        temp = str(k)
        for n in phone_book:
            if re.match(temp, n):
                temp_an += 1
        if temp_an > 1:
            answer = False
            break
        else:
            answer = True
    return answer
