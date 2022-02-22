# need to check: 이런식의 문제면 해당 아이디의 닉네임이 뭔지 파악할 때 list 끝까지 돌아보고, 그 값으로 프린트 하는 접근이 맞나?

from collections import defaultdict
def solution(record):

    # 닉네임 변경 가능한 경우 
    # 채팅방 나가고, 새로운 닉네임으로 들어감
    # 채팅방에서 닉네임 변경
    inout_dict = defaultdict(list)
    answer = []
        
    # 1 <= N <= 100,000
    for status in record:
        info = status.split(' ')
        if len(info) == 3:
            # key: id / values: (state, name)
            if info[1] in inout_dict.keys():
                if info[0] =='Change' or info[0]=='Enter':
                    inout_dict[info[1]] = info[2]
            else:
                inout_dict[info[1]] = info[2]

    for status in record:
        info = status.split(' ')
        if info[0] == 'Enter':
            answer.append(f'{inout_dict[info[1]]}님이 들어왔습니다.')
        elif info[0] =='Leave':
            answer.append(f'{inout_dict[info[1]]}님이 나갔습니다.')

    return answer
