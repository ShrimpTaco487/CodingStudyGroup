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
    new_c = org_lock_c + 2 * (org_key_c - 1)
    new_r = org_lock_r + 2 * (org_key_r - 1)

    arr = [[0] * new_c for _ in range(new_r)]

    for row in range(org_lock_r):
        for col in range(org_lock_c):
            arr[row + (org_key_r - 1)][col + (org_key_c - 1)] = lock[row][col]
    return arr


def check_all(new_lock, key, start_r, start_c, org_r, org_c):
    for row in range(len(key)):
        for col in range(len(key[0])):
            if new_lock[start_r+row][start_c+col] == 1:
                if key[row][col] == 1:
                    # 돌기인데 또 돌기이면 바로 False
                    # print('돌기',row, col )
                    return False

            else:  # 0일 때
                if key[row][col] == 1:
                    # print_grid(new_lock)
                    new_lock[start_r+row][start_c+col] = 1
                    # print()
                    # print_grid(new_lock)
                    # print('##')
                    # breakpoint()

    # 다 1인지 체크하는것
    check_r = len(key) - 1
    check_c = len(key[0]) - 1
    for row in range(org_r):
        for col in range(org_c):
            if new_lock[check_r + row][check_c + col] == 0:
                # print('not zeroing out')
                # print_grid(new_lock)
                # breakpoint()
                return False
    return True


def solution(key, lock):
    new_lock = get_new_lock(key, lock)
    org_r, org_c = len(lock), len(lock[0])
    for row in range(len(lock)+len(key)-1):
        for col in range(len(lock[0]) + len(key[0])-1):
            for angle in range(3):
                if check_all(new_lock, key, row, col, org_r, org_c):
                    return True
                else:
                    key = rotate(key)
            key = rotate(key)
            # print(row, col)
            # breakpoint()
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key,lock))


## old
# def print_grid(arr):
#     for r in arr:
#         print(r)
#
#
# def move(key, move_r, move_c):
#     new = [[0] * (len(key[0])) for _ in range(len(key))]
#     for r in range(len(key)):
#         for c in range(len(key[0])):
#             if key[r][c] == 1:
#                 # try except 하니까 왜 되는거지;
#                 if ((0 <= r + move_r < len(new)) and (0 <= c + move_c < len(new[0]))):
#                     new[r + move_r][c + move_c] = 1
#
#     return new
#
#
# def check(lock_row, lock_col, lock, key):
#     for _ in range(4):
#         key = list(zip(*key[::-1]))
#         new_lock = copy.deepcopy(lock)
#         for key_row in range(len(key)):
#             for key_col in range(len(key[0])):
#                 if new_lock[lock_row + key_row][lock_col + key_col] == 1:
#                     if key[key_row][key_col] != 0:
#                         print('first')
#                         return False
#
#                 else:
#                     if key[key_row][key_col] != 1:
#                         print('second')
#                         return False
#                     else:
#                         new_lock[lock_row + key_row][lock_col + key_col] += 1
#         row_size = len(lock) // 3
#         col_siz = len(lock[0]) // 3
#         total_sum = 0
#         for r in range(row_size, 2 * row_size):
#             for c in range(col_size, 2 * col_size):
#                 total_sum += new_lock[r][c]
#         if total_sum == (row_size * col_size):
#             return True
#         else:
#             return False
#
#
# def solution(key, lock):
#     # 애초에 lock이 다 채워진 상태면
#     if sum([sum(l for l in row) for row in lock]) == (len(lock[0])) * (len(lock)):
#         return True
#
#     # todo : time complexity
#     # 자물쇠 lock ; 열쇠 key
#     # 자물쇠 영역을 벗어난 부분의 홈과 돌기는 상관 없고
#     # 자물쇠 영역 안에서; 열쇠의 돌기, 자물쇠의 홈은 일치
#     # 자물쇠의 모든 홈을 채워 빈 곳이 없어야함
#
#     # 0 - 홈 ; 1 - 돌기
#     # key를 90도씩 다 돌려보고, 좌우 상하도 다 이동하면서 확인
#     answer = True
#
#     cnt = 0
#     new_lock = [[0] * (3 * len(lock[0])) for _ in range(3 * len(lock))]
#     len_row = len(lock)
#     len_col = len(lock[0])
#
#     play = True
#     if play:
#         for lock_row in range(len(new_lock)):
#             for lock_col in range(len(new_lock[0])):
#                 if check(lock_row, lock_col, new_lock, key):
#                     return True
#
#     return False