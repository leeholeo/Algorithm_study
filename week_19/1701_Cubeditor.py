import sys
import time
import random
import string as STR


# string = sys.stdin.readline().rstrip()    # input
string = [random.choice(STR.ascii_lowercase) for _ in range(5000)]  # input for test
# string = [random.choice("12") for _ in range(5000)]   # input for test 2
string = ''.join(string)    # input join for tests

# # solve 1
# start_time = time.time()
# length = len(string)
# max_length = 0
# for sub_start_idx in range(length):
#     pi_array = [0] * (length-sub_start_idx)
#     source_idx = sub_start_idx + 1
#     target_idx = 0
#     while source_idx < length:
#         while string[source_idx] != string[target_idx+sub_start_idx] and target_idx > 0:
#             target_idx = pi_array[target_idx-1]
#         if string[source_idx] == string[target_idx+sub_start_idx]:
#             target_idx += 1
#             max_length = max(max_length, target_idx)
#         pi_array[source_idx-sub_start_idx] = target_idx
#         source_idx += 1
# end_time = time.time()
# print(max_length)
# print(end_time-start_time)  # 4.5초 정도 소요

# # solve 2
# dict with complicated key / nested dict
# string = sys.stdin.readline().rstrip()
start_time = time.time()
length = len(string)
min_length = 0
max_length = length
while min_length < max_length:
    now_length = (max_length+min_length) // 2 + 1
    repetition = {}
    for start_idx in range(length-now_length+1):
        substring = string[start_idx:start_idx+now_length]
        if repetition.get(substring):
            min_length = now_length
            break
        else:
            repetition[substring] = True
    else:
        max_length = now_length - 1
end_time = time.time()
print(min_length)
print(end_time-start_time)  # 0.03초대
