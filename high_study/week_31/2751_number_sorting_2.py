# import sys
#
#
# def set_pivot(left, right):
#     return (sequence[left] + sequence[right])//2
#
#
# def quick_sort(left, right):
#     start = left
#     end = right
#     if left >= right:
#         return
#
#     pivot = set_pivot(left, right)
#     while left <= right:
#         while left <= end and sequence[left] <= pivot:
#             left += 1
#         while right > start and sequence[right] >= pivot:
#             right -= 1
#         if left < right:
#             sequence[left], sequence[right] = sequence[right], sequence[left]
#             left += 1
#             right -= 1
#
#     quick_sort(start, right)
#     quick_sort(right+1, end)
#
#
# input = sys.stdin.readline
# sequence = [int(input()) for _ in range(int(input()))]
# quick_sort(0, len(sequence)-1)
# print(*sequence, sep='\n')




# import sys
#
#
# CENTER = 1
#
#
# def set_pivot(left, right):
#     def select_pivot():
#         mid = (left + right) // 2
#         pivot_candidate = [
#             (sequence[left], left),
#             (sequence[mid], mid),
#             (sequence[right], right),
#         ]
#         pivot_candidate.sort()
#         return pivot_candidate[CENTER]
#
#
#     def pivot_to_left():
#         sequence[left], sequence[pivot_idx] = sequence[pivot_idx], sequence[left]
#
#     pivot_value, pivot_idx = select_pivot()
#     pivot_to_left()
#     return pivot_value
#
#
# def quick_sort(left, right):
#     start = left
#     end = right
#     if left >= right:
#         return
#
#     pivot = set_pivot(left, right)
#     left += 1
#     while left < right:
#         while left <= end and sequence[left] <= pivot:
#             left += 1
#         while right > start and sequence[right] >= pivot:
#             right -= 1
#         if left < right:
#             sequence[left], sequence[right] = sequence[right], sequence[left]
#             left += 1
#             right -= 1
#     sequence[start], sequence[right] = sequence[right], sequence[start]
#
#     quick_sort(start, right-1)
#     quick_sort(right+1, end)
#
#
# input = sys.stdin.readline
# sequence = [int(input()) for _ in range(int(input()))]
# quick_sort(0, len(sequence)-1)
# print(*sequence, sep='\n')


import sys
import random

CENTER = 1


def set_pivot(left, right):
    def select_pivot():
        return random.randint(left, right)

    def pivot_to_left():
        sequence[left], sequence[pivot_idx] = sequence[pivot_idx], sequence[left]

    pivot_idx = select_pivot()
    pivot_to_left()
    return sequence[left]


def quick_sort(left, right):
    start = left
    end = right
    if left >= right:
        return

    pivot = set_pivot(left, right)
    left += 1
    while left <= right:
        while left <= end and sequence[left] <= pivot:
            left += 1
        while right > start and sequence[right] >= pivot:
            right -= 1
        if left < right:
            sequence[left], sequence[right] = sequence[right], sequence[left]
            left += 1
            right -= 1
    sequence[start], sequence[right] = sequence[right], sequence[start]

    quick_sort(start, right - 1)
    quick_sort(right + 1, end)


input = sys.stdin.readline
sequence = [int(input()) for _ in range(int(input()))]
quick_sort(0, len(sequence) - 1)
print(*sequence, sep='\n')
