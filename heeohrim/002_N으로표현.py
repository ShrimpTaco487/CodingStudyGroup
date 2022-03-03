def countN(N, number):
    numN = 0
    flag = False
    remainder = number
    if remainder>=(11111*N):
        mox = remainder//(11111*N)
        remainder = remainder%(11111*N)
        numN += mox*5
    if remainder>=11111:
        mox = remainder//11111
        remainder = remainder%11111
        numN += mox*5
        flag = True
    if remainder>=(1111*N):
        mox = remainder//(1111*N)
        remainder = remainder%(1111*N)
        numN += mox*4
    if remainder>=1111:
        mox = remainder//1111
        remainder = remainder%1111
        numN += mox*4
        flag = True
    if remainder>=(111*N):
        mox = remainder//(111*N)
        remainder = remainder%(111*N)
        numN += mox*3
    if remainder>=111:
        mox = remainder//111
        remainder = remainder%111
        numN += mox*3
        flag = True
    if remainder>=(11*N):
        mox = remainder//(11*N)
        remainder = remainder%(11*N)
        numN += mox*2
    if remainder>=11:
        mox = remainder//11
        remainder = remainder%11
        numN += mox*2
        flag = True
    if remainder>=(1*N):
        mox = remainder//(1*N)
        remainder = remainder%(1*N)
        numN += mox*1

    if flag==True:
        numN += remainder
        numN += 1
    else:
        numN += remainder*2
    print('numN:' + str(numN))
    return numN

def solution(N, number):
    answer = 0
    answer = countN(N, number)

    if answer > 8:
        answer = -1
    return answer
