def subtract(i):
    human[i], coupon[i] = max(0, human[i] - coupon[i]), max(0, coupon[i] - human[i])


human = list(map(int, input().split()))
coupon = list(map(int, input().split()))
number = sum(human)
for i in range(3):
    subtract(i)
for i in range(3):
    if human[i]:
        coupon[i] += coupon[i-1] // 3
        coupon[i-1] %= 3
        subtract(i)
print(number - sum(human))
