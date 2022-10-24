N = int(input())
battery = 0
now = 0
last = 0
for phone in map(int, input().split()):
    if now != phone:
        now = phone
        last = 2
        battery += 2
    else:
        last *= 2
        battery += last
    if battery >= 100:
        now = 0
        last = 0
        battery = 0
print(battery)
