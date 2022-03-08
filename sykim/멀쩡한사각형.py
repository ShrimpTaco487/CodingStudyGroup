


# 시간초과 코드 -> 1억인거 생각안했음
# import math
#
# def solution(w, h):
#     # 원래 넓이에서 잘려져나간 것만큼의 갯수
#     # 직사각형 \in 정사각형 -> 정사각형일 경우 딱 딱 한개씩만 못쓰는데
#
#     # 기울기 만큼
#     total = 0
#     if h >= w:
#         coeff = h / w
#         for idx, move_w in enumerate(range(1, w + 1)):
#             prev = coeff * (move_w - 1)
#             now = coeff * move_w
#             total += math.ceil(now) - math.floor(prev)
#         return w * h - total
#     else:
#         coeff = w / h
#         for idx, move_h in enumerate(range(1, h + 1)):
#             prev = coeff * (move_h - 1)
#             now = coeff * move_h
#             total += math.ceil(now) - math.floor(prev)
#         return w * h - total
