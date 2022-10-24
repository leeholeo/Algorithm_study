N = int(input())
conferences = [list(map(int, input().split())) for _ in range(N)]
conferences.sort(key=lambda x: (x[1], x[0]))
end_time = 0
cnt = 0
for conf in conferences:
    if conf[0] >= end_time:
        end_time = conf[1]
        cnt += 1

print(cnt)