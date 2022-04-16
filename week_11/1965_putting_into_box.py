# index of dp is size of largest box
# value of dp is number of boxes
n = int(input())
boxes = list(map(int, input().split()))
dp = [1] + [0] * 1000
for box in boxes:
    for size in range(box):
        if dp[size]:
            dp[box] = max(dp[box], dp[size] + 1)

print(max(dp) - 1)


# # index of dp is number of boxes
# # value of dp is size of largest box
# n = int(input())
# boxes = list(map(int, input().split()))
# dp = [0]
# for box in boxes:
#     for num, size in enumerate(dp):
#