N, r, c = map(int, input().split())
r_bin = str(bin(r))[2:][::-1] + '0' * 16
c_bin = str(bin(c))[2:][::-1] + '0' * 16
index = ''
for i in range(16):
    index += c_bin[i] + r_bin[i]

index = index[::-1]
index = int(index, 2)
print(index)
