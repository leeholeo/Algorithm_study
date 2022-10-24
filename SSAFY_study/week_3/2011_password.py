password = input() + "00"
dp = [0] * len(password)
dp[-2] = 1
for i in range(len(password)-3, -1, -1):
    if password[i] != '0':
        dp[i] += dp[i+1]
    if 9 < int(password[i:i+2]) <= 26:
        dp[i] += dp[i+2]
print(dp[0] % 1000000)


# c=input()
# d,p=1 if c[0] != '0' else 0,0
# for i in range(1,len(c)):
#     ch = int(c[i-1]+c[i])
#     if ch>0 and ch<27:
#         if c[i]=='0':d,p=0,d
#         else:d,p=d+p,d
#     elif c[i]=='0':
#         d,p=0,0
#         break
#     else:d,p=d+p,0
# print((d+p)%1000000)