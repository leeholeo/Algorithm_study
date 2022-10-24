'''
모두고려, 실패
'''
# A, B = input().split()
# A_len = len(A)
# B_len = len(B)
# B_maxi = 1 << B_len
# A_maxi = 1 << A_len
# cnt = (B_maxi << 1) - 2
# for i in range(A_len):
#     now = int(A[i])
#     if now < 4:
#         cnt -= (A_maxi >> i) - 2
#         break
#     elif now == 4:
#         pass
#     elif now < 7:
#         cnt -= (A_maxi >> (i+1)) + (A_maxi >> i) - 2
#         break
#     elif now == 7:
#         cnt -= (A_maxi >> (i+1)) + (A_maxi >> i) - 2
#         pass
#     else:
#         cnt -= (A_maxi >> i) + (A_maxi >> i) - 2
#         break
#
# for i in range(B_len):
#     now = int(B[i])
#     if now > 7:
#         break
#     elif now == 7:
#         pass
#     elif now > 4:
#         cnt -= (B_maxi >> (i+1)) + (B_maxi >> i) - 2
#         break
#     elif now == 4:
#         cnt -= (B_maxi >> (i+1)) + (B_maxi >> i) - 2
#         pass
#     else:
#         cnt -= (B_maxi >> i)
#
# print(cnt)


'''
브뤁ㅎ 폴ㅅ
'''
A, B = input().split()
length = len(B)
A, B = int(A), int(B)
permutation = ['']
cnt = 0
result = 0
while cnt < length:
    new_permutation = []
    for comb in permutation:
        a = comb + '4'
        b = comb + '7'
        if A <= int(a) <= B:
            result += 1
        if A <= int(b) <= B:
            result += 1
        new_permutation.append(a)
        new_permutation.append(b)
    permutation = new_permutation
    cnt += 1
print(result)
