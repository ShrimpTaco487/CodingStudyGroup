# https://programmers.co.kr/learn/courses/30/lessons/12899
def get_124(n):
    if n%3 != 0:
        remainder = n%3
        mox = n//3
    else:
        remainder = 4
        mox, _ = get_124(n-1)
    return mox, remainder

def solution(n):
    answer = ''
    mox = n
    while True:
        mox, remainder = get_124(mox)
        answer = str(remainder) + answer
        if mox < 3:
            if mox != 0:
                answer = str(mox) + answer
            break
    return answer
