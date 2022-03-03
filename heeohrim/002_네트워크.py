def solution(n, computers):
    answer = 0
    visited=[]
    stack=[]
    for i in range(n):
        if i not in visited:
            stack.append(computers[i])
            visited.append(i)
            while stack:
                node = stack.pop()
                for j in range(len(node)):
                    if node[j]:
                        if j not in visited:
                            stack.append(computers[j])
                            visited.append(j)
            answer += 1
    return answer
