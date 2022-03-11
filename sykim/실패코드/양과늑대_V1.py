def backtracking(graph, info, edges, animals):
    if animals[0] < animals[1]:
        return animals
    visited = []
    flag = [True] * len(info)
    stack = [0]
    again = []
    while stack or again:
        if stack:
            cur = stack.pop()
        else:
            cur = again.pop()

        for node in graph[cur]:
            if node not in visited:
                if info[node] == 1 and (animals[0] > animals[1] + 1) and graph[node]:
                    animals[1] += 1
                    visited.append(node)
                    flag[node] = True
                elif info[node] == 0 and animals[0] + 1 > animals[1]:
                    animals[0] += 1
                    visited.append(node)
                    flag[node] = True

                else:
                    if flag[node]:
                        again.append(node)
                        flag[node] = False
                print(animals)
                stack.append(node)
    return animals


def solution(info, edges):
    answer = 0
    # sheep, wolf
    animals = [1, 0]
    graphs = [[] for i in range(len(info))]
    for x, y in edges:
        graphs[x].append(y)

    answer = backtracking(graphs, info, edges, animals)
    return answer