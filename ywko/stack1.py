#S42586
def solution(progresses, speeds):
    answer = []
    end_job = 0
    while len(progresses) != 0:
        for index in range(len(progresses)):
            progresses[index] += speeds[index]
        for i in progresses:
            if i >= 100:
                end_job += 1
            else:
                break
        if end_job != 0:
            for i in range(end_job):
                progresses.pop(0)
                speeds.pop(0)
            answer.append(end_job)
            end_job = 0

    return answer