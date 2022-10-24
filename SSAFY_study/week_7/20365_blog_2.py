N = int(input())
blogs = input()
probe = None    # 색 타입 기록
color_cnt = 0
# 순회하면서 색 타입이 몇 번 변하는지 기록
for blog in blogs:
    if probe != blog:
        color_cnt += 1
    probe = blog

share, remainder = divmod(color_cnt+1, 2)
print(share+remainder)
