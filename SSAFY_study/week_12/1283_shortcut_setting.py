'''
그냥 구현
영어 소문자와 대문자는 32의 xor로 구할 수 있다는 점을 사용하고 싶었으나, python의 경우 문자형과 점수형의 bit and 연산이 안 되더라
그래서 해쉬 느낌으로다 ASCII 값을 32로 나눈 나머지를 index로 이용, visited 사용
'''
def char_to_idx(char):
    return ord(char) % NUMBER


def bracket(word, idx):
    return word[:idx] + '[' + word[idx] + ']' + word[idx+1:]


def word_check():
    for i, word in enumerate(string):
        if visited[char_to_idx(word[0])]:
            continue
        visited[char_to_idx(word[0])] = True
        string[i] = bracket(string[i], 0)
        return True
    return False


def string_check():
    for i, word in enumerate(string):
        for j, char in enumerate(word):
            if visited[char_to_idx(char)]:
                continue
            visited[char_to_idx(char)] = True
            string[i] = bracket(word, j)
            return True
    return False


NUMBER = 32
N = int(input())
visited = [False] * NUMBER
for _ in range(N):
    string = input().split()
    if word_check():
        pass
    elif string_check():
        pass
    print(' '.join(string))
