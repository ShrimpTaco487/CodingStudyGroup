from collections import deque

# bfs, dfs
# 1, 2
def solution(numbers, target):
    answer = 0
    # 1 1 1 1 1
    # 숫자의 변형 가능도 : -1, +1
    # 왼쪽부터 오른쪽으로 가면서 경우의 수 == tree 형식으로 경우의 수 세기
    # +1 -1(0)  +1(1)
    #             -1(-1)
    #    +1(2)

    # -1 -1(-2)
    # -1 +1(0)
    org_numbers = numbers
    # bfs나 dfs나 상관없을듯 -> 두개 다른 경우에 쓰는거 다시 찾아보기
    cnt = 0
    cur_sum = 0
    idx = 0
    histories = deque()
    #
    histories.append([numbers[0], numbers[0], idx])
    histories.append([-numbers[0], -numbers[0],idx])


    while histories:
        cur_num, cur_sum, cur_idx = histories.popleft()
        print(cur_num, 'cur sum',cur_sum, 'depth', cur_idx)

        if cur_idx == len(org_numbers)-1:
            if cur_sum == target :
                cnt += 1

        else: # cur_idx+1 <= len(org_numbers)-1:
            histories.append([org_numbers[cur_idx+1], cur_sum+org_numbers[cur_idx+1], cur_idx+1])
            histories.append([org_numbers[cur_idx+1], cur_sum-org_numbers[cur_idx+1], cur_idx+1])

    return cnt
numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))

numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))