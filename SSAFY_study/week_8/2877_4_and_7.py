'''
각 자릿수마다 2^n개의 수가 있다는 것에 주목한다.
특정 자리수에서, 창영 수는 2진수 체계와 동일하게 작동한다.
따라서 초기 숫자만 조절해주면 2진수 표현과 동일하게 사용할 수 있다.
'''
# K = int(input())
# K += 1
# k_str = bin(K)[2:]
# print(k_str.replace('0', '4').replace('1', '7')[1:])

print(bin(int(input())+1)[3:].replace('0', '4').replace('1', '7'))
