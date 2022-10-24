'''
구리디
'''
N = int(input())
arr = list(map(int, input().split()))
S = int(input())
result = []
while S > 0 and (length := len(arr)) > 1:
    max_num = arr[0]
    max_num_idx = 0
    for num_idx in range(1, min(length, S+1)):
        num = arr[num_idx]
        if num > max_num:
            max_num_idx = num_idx
            max_num = num
    result.append(arr.pop(max_num_idx))
    S -= max_num_idx
result.extend(arr)
print(*result)
