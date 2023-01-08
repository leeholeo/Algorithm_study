N = int(input())
dancing = {"ChongChong"}
for _ in range(N):
    a, b = input().split()
    if a in dancing or b in dancing:
        dancing.add(a)
        dancing.add(b)
print(len(dancing))
