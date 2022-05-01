num_of_weights = int(input())
weights = list(map(int, input().split()))
num_of_marbles = int(input())
marbles = list(map(int, input().split()))

MAXIMUM = sum(weights)
# -MAXIMUM ~ MAXIMUM
dp = [[False] * (2*MAXIMUM + 1) for _ in range(num_of_weights+1)]
dp[0][0] = True
# queue를 사용하여 속도 개선 가능할 듯
# 추를 구슬 위치에 놓거나(빼기), 놓지 않거나, 구슬 반대편에 놓거나(더하기)
for weight_idx in range(num_of_weights):
    for now_weight in range(-MAXIMUM, MAXIMUM+1):
        if dp[weight_idx][now_weight]:
            dp[weight_idx+1][now_weight] = True
            weight = weights[weight_idx]
            if now_weight + weight <= MAXIMUM:
                dp[weight_idx+1][now_weight+weight] = True
            if now_weight - weight >= -MAXIMUM:
                dp[weight_idx+1][now_weight-weight] = True

for marble_idx in range(num_of_marbles):
    marble = marbles[marble_idx]
    # 범위를 넘어가는 경우 IndexError
    if not (-MAXIMUM <= marble <= MAXIMUM):
        marbles[marble_idx] = 'N'
        continue
    if dp[-1][marble]:
        marbles[marble_idx] = 'Y'
    else:
        marbles[marble_idx] = 'N'

print(*marbles)
