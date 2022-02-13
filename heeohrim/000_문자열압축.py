# -*- coding: utf-8 -*-
# https://programmers.co.kr/learn/courses/30/lessons/60057

def writeCode(count,unitStr,code):
    if count > 1:
        code.extend(str(count))
        code.extend(unitStr)
    else:
        code.extend(unitStr)
    count = 1
    return code, count


def solution(s):
    answer = len(s)
    shortestCode =[]
    shortestCode.extend(s)
    for unitNum in range(1,len(s)+1):
        code = []
        count = 1
        unitString = s[0:unitNum]
        remainder = s[unitNum:]
        # print('unitString:',unitString)
        for round in range(int(len(s)/unitNum)):
            unitRemainder = remainder[0:unitNum]
            if unitString == unitRemainder:
                count+=1
                if len(remainder) <= unitNum:
                    code, count = writeCode(count, unitString, code)
                    # print('code:',code)
                    break
                else:
                    unitString = remainder[0:unitNum]
                    remainder = remainder[unitNum:]
            else:
                if len(remainder) <= unitNum:
                    code, count = writeCode(count, unitString, code)
                    # print('code:',code)
                    code.extend(remainder)
                    break
                else:
                    code, count = writeCode(count, unitString, code)
                    # print('code:',code)
                    unitString = remainder[0:unitNum]
                    remainder = remainder[unitNum:]
        if (len(code) != 0) and (len(code) < answer):
            answer = len(code)
            shortestCode = code
    print('shortestCode:',shortestCode)
    return answer


if __name__ == '__main__':
    TEST_CASES = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede",
    "abcabcabcabcdededededede", "xababcdcdababcdcd"]
    for TEST_CASE in TEST_CASES:
        print(TEST_CASE)
        print(solution(TEST_CASE))
