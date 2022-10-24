import heapq
from time import time
import random


def bubble_sort(lst):
    start_time = time()
    for endpoint in range(len(lst)-1, 0, -1):
        for bubble in range(endpoint):
            if lst[bubble] > lst[bubble+1]:
                lst[bubble], lst[bubble+1] = lst[bubble+1], lst[bubble]
    end_time = time()
    print(f'bubble sort: {end_time-start_time}')
    return lst


def heappush_sort(lst):
    start_time = time()
    heap = []
    for component in lst:
        heapq.heappush(heap, component)
    middle_time = time()
    rtn = list()
    while heap:
        rtn.append(heapq.heappop(heap))
    end_time = time()
    print(f'heappush sort: {end_time-start_time}')
    print(f'heappush: {middle_time-start_time}')
    return rtn


def heapify_sort(lst):
    start_time = time()
    heapq.heapify(lst)
    middle_time = time()
    rtn = list()
    while lst:
        rtn.append(heapq.heappop(lst))
    end_time = time()
    print(f'heapify sort: {end_time - start_time}')
    print(f'heapify: {middle_time - start_time}')
    return rtn


RANGE = 100000000
number = 1000000
sample_start_time = time()
sample = random.sample(range(RANGE), number)
sample_end_time = time()
print(f'sample: {sample_end_time - sample_start_time}')
# bubble_sort(sample[:])
heappush_sort(sample[:])
heapify_sort(sample[:])
multiply_start_time = time()
m = [10000000] * 1000000
multiply_end_time = time()
print(f'multiply: {multiply_end_time - multiply_start_time}')
for_start_time = time()
f = [10000000 for _ in range(1000000)]
for_end_time = time()
print(f'for: {for_end_time - for_start_time}')
append_start_time = time()
a = []
for _ in range(1000000):
    a.append(10000000)
append_end_time = time()
print(f'append: {append_end_time - append_start_time}')
pop_start_time = time()
for _ in range(1000000):
    a.pop()
pop_end_time = time()
print(f'pop: {pop_end_time - pop_start_time}')
copy_start_time = time()
b = a[:]
copy_end_time = time()
print(f'copy: {copy_end_time - copy_start_time}')