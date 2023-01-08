'''
linked list
'''
class Present:
    def __init__(self, front, num, rear):
        self.front = front
        self.num = num
        self.rear = rear


def init(signal, n, m, *nums):
    if signal != 100:
        return False
    belt = [{} for _ in range(n)]
    cnt = 1
    for i in range(n):
        if nums[i] == 0:
            belt[i]["front"] = None
            belt[i]["rear"] = None
            belt[i]["num"] = 0
            continue
        belt[i]["num"] = nums[i]
        for j in range(cnt, cnt + nums[i]):
            Present(j-1, j, j+1)


        belt[i]["front"] = cnt
        belt[i]["rear"] = cnt + nums[i] - 1

        cnt += nums[i]


    return belt, belt_meta

q = int(input())
_, n, m,
