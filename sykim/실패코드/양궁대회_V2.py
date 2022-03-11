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
        # print(left_num, lion, peach, cur_idx, lion_path)

        if cur_idx == 10:
            if lion > peach:
                score = calc_score(lion_path)
                if score >= max_score:
                    lion_target[score].append(lion_path)
                    max_score = score

            continue

        peach_got = info[cur_idx + 1]
        # 피치보다 더 많이 넣거나
        if left_num - (peach_got+1) >= 0:
            queue.append([ left_num - (peach_got + 1), lion + 10 - (cur_idx + 1),
                          peach, cur_idx + 1,lion_path+[peach_got+1]]) # append의 반환값은 None!!

        # 라이언은 안맞춤! 그럼 peach가 넣었느냐 아니냐에 따라서 점수 이득 발생
        if peach_got >= 1:
            queue.append([left_num, lion, peach + 10 - (cur_idx + 1), cur_idx + 1, lion_path+[0]])
        else:
            queue.append([left_num, lion, peach , cur_idx + 1, lion_path + [0]])
        # print(lion, peach )
        # breakpoint()
    # 가장 낮은 점수를 더 많이 맞힌 경우 반환
    if lion_target:
        # 가장 큰 점수!
        breakpoint()
        return sorted(lion_target[max_score])[0]
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