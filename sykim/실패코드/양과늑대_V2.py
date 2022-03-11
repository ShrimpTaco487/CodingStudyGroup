# https://programmers.co.kr/learn/courses/30/lessons/92343
info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]

def solution(info, edges):
    answer = 0
    maps = {k:[] for k in range(len(info))}
    for node1, node2 in edges:
        maps[node1].append(node2)
        maps[node2].append(node1)

    visited = [False] * len(info)
    # node, sheep, wolf
    stack = [(0, 1, 0)]
    max_val = 1
    visited[0] = True

    while stack:
        node, sheep, wolf = stack.pop()
        if sheep > max_val:
            max_val = sheep

        for new in maps[node]:
            if not visited[new]:

                if info[new] ==1 : # 늑대면
                    if sheep  > wolf +1:
                        visited[new] = True
                        info[new] = -1
                        stack.append((new, sheep, wolf+1))
                elif info[new] ==0:
                    if sheep+1 > wolf:
                        visited[new] = True
                        info[new] = -1
                        stack.append((new, sheep+1, wolf))
                else:
                    stack.append((new,sheep,wolf))
                # print(stack)
                # breakpoint()

    return max_val


print(solution(info,edges))