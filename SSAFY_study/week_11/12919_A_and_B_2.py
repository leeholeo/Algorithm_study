'''
귀찮은데 그냥 완탐해도 되지 않을까? -> 역시 안된다~
(kmp로) 동일 문자열 찾고 (우측 B 개수) - (좌측 B 개수) in (0, 1) -> 귀찮음
아니 그냥 역순으로 제거하면 되지 않을까? -> 됏당
'''
# # 완탐
# def recur(string, a, b, reversed):
#     if a == 0 and b == 0:
#         if reversed:
#             if string == T_reverse:
#                 print(1)
#                 quit()
#         elif string == T:
#             print(1)
#             quit()
#         return
#     if reversed:
#         if a > 0:
#             next_string = 'A'+string
#             recur(next_string, a-1, b, reversed)
#         if b > 0:
#             next_string = 'B'+string
#             recur(next_string, a, b-1, not reversed)
#     else:
#         if a > 0:
#             next_string = string+'A'
#             recur(next_string, a-1, b, reversed)
#         if b > 0:
#             next_string = string+'B'
#             recur(next_string, a, b-1, not reversed)
#
#
# S = input()
# T = input()
# T_reverse = T[::-1]
# a = T.count('A') - S.count('A')
# b = T.count('B') - S.count('B')
# if a < 0 or b < 0:
#     print(0)
# else:
#     recur(S, a, b, False)
#     print(0)

# 역순 제거
# def recur(left, right, cnt):
#     if cnt == 0:
#         if left > right:
#             if T[right:left+1] == S_reverse:
#                 print(1)
#                 quit()
#         else:
#             if T[left:right+1] == S:
#                 print(1)
#                 quit()
#         return
#
#     if visited.get((left, right)):
#         return
#
#     if T[left] == 'B':
#         if left > right:
#             recur(right, left-1, cnt-1)
#         else:
#             recur(right, left+1, cnt-1)
#     if T[right] == 'A':
#         if left > right:
#             recur(left, right+1, cnt-1)
#         else:
#             recur(left, right-1, cnt-1)
#     visited[(left, right)] = True
#
#
# S = input()
# S_reverse = S[::-1]
# T = input()
# visited = {}
# recur(0, len(T)-1, len(T)-len(S))
# print(0)


# refactoring
def recur(left, right, cnt):
    # pruning
    if visited.get((left, right)):
        return

    # reversed
    if left > right:
        # termination
        if cnt == 0:
            if T[right:left+1] == S_reverse:
                print(1)
                quit()
            return

        # recursion
        if T[left] == 'B':
            recur(right, left-1, cnt-1)
        if T[right] == 'A':
            recur(left, right+1, cnt-1)
    # not reversed
    else:
        # termination
        if cnt == 0:
            if T[left:right+1] == S:
                print(1)
                quit()
            return

        # recursion
        if T[left] == 'B':
            recur(right, left+1, cnt-1)
        if T[right] == 'A':
            recur(left, right-1, cnt-1)

    # for pruning
    visited[(left, right)] = True


S = input()
S_reverse = S[::-1]
T = input()
visited = {}
recur(0, len(T)-1, len(T)-len(S))
print(0)
