# -*- coding: utf-8 -*-
# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    uidNickname = {}
    messages = []
    for rcrd in record:
        a=rcrd.split()
        if (a[0] == "Enter") or (a[0] == "Change"):
            messages.append([a[0],a[1]])
            uidNickname[a[1]] = a[2]
        elif a[0] == "Leave":
            messages.append([a[0],a[1]])
    for message in messages:
        if message[0] == "Enter":
            answer.append(uidNickname[message[1]]+"님이 들어왔습니다.")
        elif message[0] == "Leave":
            answer.append(uidNickname[message[1]]+"님이 나갔습니다.")
    return answer


if __name__ == '__main__':
    TEST_CASE = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234",
    "Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(TEST_CASE)
    print(solution(TEST_CASE))
