'''
linked array
'''
class Gift:
    def __init__(self, num):
        self.front = -1
        self.rear = -1
        self.num = num

    def __str__(self):
        return f"Gift/front: {self.front}/rear: {self.rear}/"


default_gift = Gift(-1)


class Belt:
    def __init__(self):
        self.front = default_gift
        self.rear = default_gift
        self.num = 0

    def __str__(self):
        return f"Belt/front: {self.front.num}/rear: {self.rear.num}/num: {self.num}/"


q = int(input())
for _ in range(q):
    command = list(map(int, input().split()))
    if command[0] == 100:
        n, m = command[1], command[2]
        belt = [Belt() for _ in range(n)]
        gift = [Gift(i) for i in range(m)]
        for gift_num in range(m):
            belt_num = command[gift_num+3]
            gift_now = gift[gift_num]
            belt_now = belt[belt_num]
            belt_now.num += 1
            if belt_now.rear == default_gift:
                belt_now.front = gift_now
            else:
                belt_now.rear.rear = gift_now
                gift_now.front = belt_now.rear
            belt_now.rear = gift_now

    elif command[0] == 200:
        pass
    elif command[0] == 300:
        pass
    elif command[0] == 400:
        pass
    elif command[0] == 500:
        pass
    elif command[0] == 600:
        pass

print(*belt)
print(*gift)