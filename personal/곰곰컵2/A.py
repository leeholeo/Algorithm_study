N = int(input())
number = 0
for _ in range(N):
    if int(input().lstrip("D-")) <= 90:
        number += 1
print(number)