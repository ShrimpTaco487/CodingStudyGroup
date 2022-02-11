# -*- coding: utf-8 -*-
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s)
    for unitNum in range(1,len(s)+1):
        shortestCode = []
        count = 1
        currentUnitStr = s[0:unitNum]
        remainder = s[unitNum:]
        print('unitString:',currentUnitStr)
        while True:
            if len(remainder) < unitNum:
                break
            print('remainderlength,unitlength:',len(remainder), unitNum)
            print('unitString,remainderunit,count:',currentUnitStr,remainder[0:unitNum],count)
            if remainder[0:unitNum] == currentUnitStr:
                count += 1
                remainder = remainder[unitNum:]
                print('remainder:',remainder)
            else:
                if count>1:
                    shortestCode.extend(str(count))
                    print('shortcode:',shortestCode)
                shortestCode.extend(currentUnitStr)
                print('shortcode:',shortestCode)
                print('unitString,remainderuint:',currentUnitStr,remainder[0:unitNum])
                currentUnitStr = remainder[0:unitNum]
                remainder = remainder[unitNum:]
                print('remainder:',remainder)
                print('unitString,remainder:',currentUnitStr,remainder)
                count = 1
        shortestCode.extend(remainder)
        print('shortcode:',shortestCode)
    if len(shortestCode)!=0 and len(shortestCode)<answer:
        answer = len(shortestCode)
    return answer

if __name__ == '__main__':
    TEST_CASES = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede",
    "abcabcabcabcdededededede", "xababcdcdababcdcd"]
    print('string:',TEST_CASES[0])
    print('solution:',solution(TEST_CASES[0]))
    # for TEST_CASE in TEST_CASES[0]:
    #     print(TEST_CASE)
    #     print(solution(TEST_CASE))
