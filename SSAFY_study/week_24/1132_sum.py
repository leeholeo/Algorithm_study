'''
greedy
'''
N = int(input())
words = [input() for _ in range(N)]
alpha = {}
for a in range(10):
    a = chr(ord('A')+a)
    alpha[a] = 0

heads = set()
for word in words:
    heads.add(word[0])
    length = len(word)
    for i in range(length):
        alpha[word[i]] += 10 ** (length-1-i)

to_sort = []
for a, v in alpha.items():
    to_sort.append((v, a))
to_sort.sort()

answer = 0
for i in range(len(to_sort)):
    v, a = to_sort[i]
    if a in heads:
        continue
    to_sort.pop(i)
    break

for i in range(len(to_sort)):
    v, a = to_sort[i]
    answer += v * (i+1)
print(answer)
