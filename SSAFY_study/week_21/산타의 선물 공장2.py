'''
linked list
'''
class Dumb:
    def __init__(self):
        self.num = -2


default_dumb = Dumb()


class Gift:
    def __init__(self, num):
        self.front = default_dumb
        self.rear = default_dumb
        self.num = num

    def __str__(self):
        return f"Gift/front: {self.front.num}/rear: {self.rear.num}/num: {self.num}"

    def fronts(self, n):
        if n == 0:
            return self
        return self.front.fronts(n-1)

    def rears(self, n):
        if n == 0:
            return self
        return self.rear.rears(n-1)


default_gift = Gift(-2)


class Belt:
    def __init__(self):
        self.front = default_gift
        self.rear = default_gift
        self.num = 0

    def init(self):
        self.front = default_gift
        self.rear = default_gift
        self.num = 0

    def __str__(self):
        return f"Belt/front: {self.front.num}/rear: {self.rear.num}/num: {self.num}/"

    def copy(self):
        b = Belt()
        b.front = self.front
        b.rear = self.rear
        b.num = self.num
        return b

    def pop_front(self, n):
        if n == 0:
            return Belt()
        elif n >= self.num:
            b = self.copy()
            self.init()
            return b
        else:
            end = self.front.rears(n-1)
            start = end.rear
            end.rear = default_gift
            start.front = default_gift
            b = Belt()
            b.front = self.front
            b.rear = end
            b.num = n
            self.front = start
            self.num -= n
            return b

    def append_front(self, b):
        if b.num == 0:
            return self.num
        if self.num == 0:
            self.rear = b.rear
        else:
            end = b.rear
            start = self.front
            end.rear = start
            start.front = end
        self.front = b.front
        self.num += b.num
        return self.num


q = int(input())
for _ in range(q):
    command = list(map(int, input().split()))
    if command[0] == 100:
        n, m = command[1], command[2]
        belt = [Belt() for _ in range(n)]
        gift = [Gift(i) for i in range(m)]
        for gift_num in range(m):
            belt_num = command[gift_num+3] - 1
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
        src, dst = command[1]-1, command[2]-1
        belt_src = belt[src]
        belt_dst = belt[dst]
        src_front = belt_src.pop_front(belt_src.num)
        print(belt_dst.append_front(src_front))
    elif command[0] == 300:
        src, dst = command[1]-1, command[2]-1
        belt_src = belt[src]
        belt_dst = belt[dst]
        src_front = belt_src.pop_front(1)
        dst_front = belt_dst.pop_front(1)
        belt_src.append_front(dst_front)
        print(belt_dst.append_front(src_front))
    elif command[0] == 400:
        src, dst = command[1]-1, command[2]-1
        belt_src = belt[src]
        belt_dst = belt[dst]
        src_front = belt_src.pop_front(belt_src.num//2)
        print(belt_dst.append_front(src_front))
    elif command[0] == 500:
        p_num = command[1]-1
        gift_now = gift[p_num]
        print((gift_now.front.num+1) + 2*(gift_now.rear.num+1))
    elif command[0] == 600:
        b_num = command[1]-1
        belt_now = belt[b_num]
        print((belt_now.front.num+1) + 2*(belt_now.rear.num+1) + 3*belt_now.num)
