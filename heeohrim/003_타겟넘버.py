from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.extendleft([1, -1])
    visited = []
    while queue:
        node = queue.popleft()
        if visited:
            if  abs(node) <= abs(visited[-1]):
                for _ in range(abs(visited[-1])-abs(node)+1):
                    visited.pop()
        visited.append(node)
        if abs(node) < len(numbers):
            queue.extendleft([abs(node)+1, -abs(node)-1])
        else:
            sum=0
            for i in visited:
                sum += numbers[abs(i)-1] * int(i/abs(i))
            if sum == target:
                answer += 1
    return answer
