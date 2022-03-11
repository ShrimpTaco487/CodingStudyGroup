import copy
# [list(elem) for elem in zip(*a[::-1])]
# list(zip(a[::-1]))

# 자물쇠(lock) : NxN, 열쇠(key): MxM
# 열쇠: 회전, 이동 가능
# 0: 홈 / 1: 돌기
def rotate(arr):
    return [list(ele) for ele in zip(*arr[::-1])]


# lock의 가장 좌측 상단부터 시작
# lock의 빈칸이 없는지, 그리고 key&lock의 돌기끼리 만나는 곳은 없는지 맞춰봄
# 90도씩 3번씩 돌려서 확인하고, 마지막 1번 다시 돌려서 원 위치로 돌리고
# 다음 칸으로 이동.
# row 단위로 (lock_row)+1 만큼 모두 움직이면
# 다음 col으로 움직여서 2번부터 반복

# 일일이 움직이면서 하면 헷갈리기 때문에 lock을 큰 판으로 만들어버림

def print_grid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            print(grid[row][col], end = ' ')
        print()

def get_new_lock(key, lock):
    org_lock_c = len(lock[0])
    org_lock_r = len(lock)
    org_key_c = len(key[0])
    org_key_r = len(key)
    new_c = org_lock_c + 2 * org_key_c
    new_r = org_lock_r + 2 * org_key_r

    arr = [[0] * new_c for _ in range(new_r)]

    for row in range(org_lock_r):
        for col in range(org_lock_c):
            arr[row + (org_key_r)][col + (org_key_c)] = lock[row][col]
    return arr


def attach(new_lock, key, start_r, start_c, org_r, org_c):
    for row in range(len(key)):
        for col in range(len(key[0])):
            new_lock[start_r+row][start_c+col] += key[row][col]

def detach(new_lock, key, start_r, start_c, org_r, org_c):
    for row in range(len(key)):
        for col in range(len(key[0])):
            new_lock[start_r+row][start_c+col] -= key[row][col]


def check_all(new_lock, key, start_r, start_c, org_r, org_c):
    # 다 1인지 체크하는것
    check_r = len(key)
    check_c = len(key[0])
    for row in range(org_r):
        for col in range(org_c):
            if new_lock[check_r + row][check_c + col] != 1:
                # print('not zeroing out')
                # print_grid(new_lock)
                # breakpoint()
                return False
    return True


def solution(key, lock):
    new_lock = get_new_lock(key, lock)
    org_r, org_c = len(lock), len(lock[0])
    for _ in range(4):
        key = rotate(key)
        for row in range(1,len(lock)+len(key)):
            for col in range(1, len(lock) + len(key)):
                attach(new_lock, key, row, col, org_r, org_c)
                if check_all(new_lock, key, row, col, org_r, org_c):
                    return True
                detach(new_lock, key, row, col, org_r, org_c)
    # for row in range(len(lock)+len(key)):
    #     for col in range(len(lock[0]) + len(key[0])):
    #         for angle in range(3):
    #             attach(new_lock, key, row, col, org_r, org_c)
    #             if check_all(new_lock, key, row, col, org_r, org_c):
    #                 return True
    #             detach(new_lock, key, row, col, org_r, org_c)
    #             key = rotate(key)
    #         key = rotate(key)
            # print(row, col)
            # breakpoint()
    return False

# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# print(solution(key,lock))
