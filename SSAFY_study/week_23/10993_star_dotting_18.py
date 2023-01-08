'''
implement
'''
def dotting(r, c, n, h):
    if n <= 0:
        return
    dr = -1
    if n % 2:
        dr = 1
    for i in range(h-1):
        picture[r + i*dr][c+i] = '*'
        picture[r + i*dr][c-i] = '*'
    for j in range(-h+1, h):
        picture[r + (h-1)*dr][c+j] = '*'
    dotting(r + (h-2)*dr, c, n-1, h//2)


N = int(input())
height = 0
for _ in range(N):
    height = 2*height + 1
width = 2*height - 1
center = height - 1
picture = [[' '] * width for _ in range(height)]
dotting(0 if N%2 else height-1, center, N, height)
for pic in picture:
    print(''.join(pic).rstrip())
