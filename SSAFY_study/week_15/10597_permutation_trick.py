'''
backtracking
'''
def backtracking(now):
    if now >= length:
        print(*answer)
        quit()

    one_number = int(sequence[now])
    if one_number == 0:
        return
    if one_number <= N and not visited[one_number]:
        visited[one_number] = True
        answer.append(one_number)
        backtracking(now+1)
        answer.pop()
        visited[one_number] = False
    two_number = int(sequence[now:now+2])
    if two_number <= N and not visited[two_number]:
        visited[two_number] = True
        answer.append(two_number)
        backtracking(now+2)
        answer.pop()
        visited[two_number] = False


sequence = input()
length = len(sequence)
N = 9 + (length-9)//2
visited = [False] * (N+1)
visited[0] = True
answer = []
backtracking(0)
