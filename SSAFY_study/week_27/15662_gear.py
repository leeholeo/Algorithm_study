'''
implementation
'''
class Gear:
    def __init__(self, status: str):
        self.status = status
        self.left = 0
        self.right = 4

    def rotate(self, w):
        self.left = (self.left + w) % 8
        self.right = (self.right + w) % 8

    def answer(self):
        if self.status[(self.left+2) % 8] == 1:
            return 1
        else:
            return 0


T = int(input())
cw = 1
ccw = -1
gears = [Gear(input()) for _ in range(T)]
K = int(input())
for _ in range(K):
    i, w = map(int, input().split())
    i -= 1
    r, l = i+1, i-1
    rw, lw = -w, -w
    while r < T:
        if gears[r-1].right != gears[r].left:
            gears[r].rotate(rw)
            rw = -rw
    while 0 < l:
        if gears[l+1].left != gears[l].right:
            gears[l].rotate(lw)
            lw = -lw
    gears[i].rotate(w)
print()
