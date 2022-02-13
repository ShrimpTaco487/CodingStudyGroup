# key idea: s 범위 생각했을 때 2번 for 돌아도 시간안에 풀 수 있을 것 같았음 -> string의 반쪽길이만큼 완전 탐색 + 비교하는 string을 업데이트

def solution(s):
    final = ''
    min_len = len(s)
    for k in range(1,len(s)//2 +1):
        answer = ''
        store = s[:k]
        cnt = 1
        for i in range(k,len(s)+k, k):
            
            if store == s[i:i+k]:
                cnt +=1
            else:
                if cnt >1:
                    answer += f'{cnt}{store}'
                else:
                    answer += store
                # print(i, cnt, store, s[i:i+k])
                store = s[i:i+k]
                cnt = 1
        if min_len > len(answer):
            min_len = len(answer)
            final = answer
    return min_len
