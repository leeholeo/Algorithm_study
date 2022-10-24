import sys
#
#
# def add(sett, number):
#     return sett | number
#
#
# def remove(sett, number):
#     return sett & (full - number)
#
#
# def check(sett, number):
#     print(int(bool(number & sett)))
#     return sett
#
#
# def toggle(sett, number):
#     return sett ^ number


input = sys.stdin.readline
M = int(input())
full = 2 ** 20 - 1
empty = 0
S = empty
# commands = ('add', 'remove', 'check', 'toggle')
# operations = (add, remove, check, toggle)
for _ in range(M):
    line = input().strip()
    if ord(line[-1]) > 64:  # ord('A') == 65
        if line == 'all':
            S = full
        else:
            S = empty

        continue

    cmd, num = line.split()
    num = 2 ** (int(num) - 1)
    # for command, operation in zip(commands, operations):
    #     if cmd == command:
    #         S = operation(S, num)
    if cmd == 'add':
        S |= num
    elif cmd == 'remove':
        S &= full - num
    elif cmd == 'check':
        print(1) if num & S else print(0)
    else:
        S ^= num



# import sys
# TESTCASE = int(sys.stdin.readline())
# S = 0
# for _ in range(TESTCASE):
#     try:
#         command_line = sys.stdin.readline()
#         command, num = command_line.split()
#         num = int(num) - 1
#     except ValueError:
#         command = command_line
#
#     if command == 'add':
#         S = S | (1 << num)
#     elif command == 'remove':
#         S = (S ^ (1 << num)) & S
#     elif command == 'check':
#         if S & (1 << num):
#             print(1)
#         else:
#             print(0)
#     elif command == 'toggle':
#         S = S ^ (1 << num)
#     elif command == 'all':
#         S = (1 << 21) - 1
#     elif command == 'empty':
#         S = 0


    # if command[0:3] == 'add':
    #     num = int(command[4:])
    #     S[num] = S[num] | 1
    # elif command[0:6] == 'remove':
    #     num = int(command[7:])
    #     S[num] = S[num] & 0
    # elif command[0:5] == 'check':
    #     num = int(command[6:])
    #     print(S[num])
    # elif command[0:6] == 'toggle':
    #     num = int(command[7:])
    #     S[num] = S[num] ^ 1
    # elif command == 'all':
    #     S = 1 << 21 - 1
    # elif command == 'empty':
    #     S = 0

