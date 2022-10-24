def dfs(down, now=-1, char_i=-1):
    if char_i < -len_word:
        return

    if now < -len_bridge:
        return
    
    cnt = 0

    for i in range(now, len_bridge-1, -1):
        if bridge[down][i] == word[char_i]:
            dfs(down, i-1, char_i-1)



    return cnt


word = input()
len_word = len(word)
bridge = [input() for _ in range(2)]
len_bridge = len(bridge[0])
print(dfs(0) + dfs(1))