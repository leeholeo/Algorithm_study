def go_front():
    if not front:
        return

    global now
    back.append(now)
    now = front.pop()


def go_back():
    if not back:
        return

    global now
    front.append(now)
    now = back.pop()


def compress():
    temp = {}
    global cache
    len_b = len(back)
    for i in range(len_b - 1, -1, -1):
        b = back[i]
        if i == temp.get(b, 0) - 1:
            back.pop(i)
            cache -= caches[b]

        temp[b] = i


def access(page):
    global cache
    for p in front:
        cache -= caches[p]

    front.clear()
    global now
    if now != 0:
        back.append(now)

    now = page
    cache += caches[page]
    global C
    while cache > C:
        cache -= caches[back.pop(0)]


N, Q, C = map(int, input().split())
caches = [None] + list(map(int, input().split()))
front = []
back = []
now = 0
cache = 0
for _ in range(Q):
    command = input()
    if command[0] == 'A':
        access(int(command[2:]))
    elif command[0] == 'F':
        go_front()
    elif command[0] == 'B':
        go_back()
    elif command[0] == 'C':
        compress()

if not back:
    back = [-1]

if not front:
    front = [-1]
print(now)
print(*back[::-1])
print(*front[::-1])
