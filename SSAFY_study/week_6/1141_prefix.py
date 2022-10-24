'''
무지성 brute force -> 정렬 방식을 응용
정렬 시 a가 어느 문자열의 prefix라면, a 다음에 오는 문자열은 a를 prefix로 가진다.
'''
N = int(input())
words = []
for _ in range(N):
    words.append(input().strip())

answer = N
for i in range(N):
    if words[i] == words[i+1][:len(words[i])]:
        answer -= 1
        break
print(answer)
