from collections import deque, defaultdict

def calc_score(arr):
    score = 0
    for idx, cnt in enumerate(arr):
        if cnt > 0:
            score += (10-idx)
    return score


def solution(n, info):
    # n: 라이언이 쏠 수 있는 화살 갯수
    # info: 어피치가 쏜 점수

    # k점을 더 많이 맞힌 선수가 점수 k를 가져감.
    # 대신 동점일 경우 어피치가 가져감
    answer = []
    peach_score = 0
    lion_score = 0
    queue = deque()

    # 남은 횟수, 누적 라이언 득점, 누적 피티 득점 , 현재 위치 idx, 라이언 맞춘 갯수
    queue.append([n, 0, 10, 0, [0]])
    if (n- info[0]-1) >= 0:
        queue.append([n - info[0] - 1, 10, 0, 0, [info[0] + 1]])

    lion_target = defaultdict(list)
    # lion_target = []
    max_score = 0

    while queue:
        left_num, lion, peach, cur_idx, lion_path = queue.popleft()
        # if cur_idx == 10:
        # print(left_num, lion, peach, cur_idx, lion_path)

        if cur_idx == 10:
            if lion > peach:
                # score = calc_score(lion_path)
                if lion-peach >= max_score:
                    print(left_num, lion, peach, cur_idx, lion_path)
                    lion_target[lion-peach ].append(list(reversed(lion_path)))
                    max_score = lion-peach

            continue

        peach_got = info[cur_idx + 1]
        # 피치보다 더 많이 넣거나 -> 이때는 무조건 1개 더 많게 넣는게 이득
        if left_num - (peach_got+1) >= 0:
            queue.append([ left_num - (peach_got + 1), lion + 10 - (cur_idx + 1),
                          peach, cur_idx + 1,lion_path+[peach_got+1]]) # append의 반환값은 None!!

        # 피치보다 같게 넣거나, 덜 넣어서 피치가 1개 이상 넣었으면 점수 먹고 아니면 못먹거나
        for peach_s in range(peach_got+1):
            if left_num - (peach_s) >= 0:
                if peach_got >= 1:
                    queue.append([left_num-peach_s, lion, peach + 10 - (cur_idx + 1), cur_idx + 1, lion_path + [peach_s]])
                else:
                    queue.append([left_num-peach_s, lion, peach, cur_idx + 1, lion_path + [peach_s]])

        # print(lion, peach )
        # breakpoint()
    # 가장 낮은 점수를 더 많이 맞힌 경우 반환
    if lion_target:
        # 가장 큰 점수! 중에서가 아니라 가장 큰 점수 차이!!
        answer = lion_target[max_score]
        # 낮게 맞은 애들이 더 많은 애들 -> reverse 해서 sorting! reverse는 앞에서 처리하자

        return list(reversed(sorted(answer,reverse=True)[0]))
    else:
        return [-1]


n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
result = [0,2,2,0,1,0,0,0,0,0,0]

n = 1
info = [1,0,0,0,0,0,0,0,0,0,0]
result = [-1]

n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]
result = [0,2,2,0,1,0,0,0,0,0,0]

n = 10
info = [0,0,0,0,0,0,0,0,3,4,3]
print(solution(n,info))

# 완전 탐색을 한다? -> bfs, dfs!! 그거말고 또 뭐있는지 문제의 갈래에 따라 정리하자