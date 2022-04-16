import sys


input = sys.stdin.readline
for tc in range(1, int(input())+1):
    command = input()
    length = int(input())
    array = input()
    if length == 0:
        array = []
    else:
        command.replace('RR', '')
        array = list(map(int, array.strip().lstrip('[').rstrip(']').split(',')))

    now = 0
    for cmd in command:
        if cmd == 'R':
            now = length - now
        elif cmd == 'D':
            if length == 0:
                print('error')
                break
            length -= 1
            now = max(0, now - 1)
            array.pop(now)
    else:
        print(str(array[::-1] if now else array).replace(' ', ''))

