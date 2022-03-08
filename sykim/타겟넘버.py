def dfs_stack(graph, target):
    stack = []
    stack.append((0, -graph[0]))
    stack.append((0, +graph[0]))
    cnt = 0
    result = 0
    while stack:

        idx, temp = stack.pop()

        if (idx+1)== len(graph):
            # sum(result.append(1)) --> none type object
            if (temp) == target:
                cnt+=1

        else:
            stack.append((idx+1,temp-graph[idx+1]))
            stack.append((idx+1, temp+graph[idx+1]))

    return cnt

def solution(numbers, target):
    # numbers.sort(reverse=True)
    answer = dfs_stack(numbers, target)
    print(answer)
    return answer