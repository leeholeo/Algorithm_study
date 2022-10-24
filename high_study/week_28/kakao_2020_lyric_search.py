import sys


sys.setrecursionlimit(10**7)


def trie_input(trie, string, index, length):
    trie['total'][length] = trie['total'].get(length, 0) + 1
    if index == 0:
        return
    if not trie.get(string[index]):
        trie[string[index]] = {
            'total': {}
        }
    trie_input(trie[string[index]], string, index+1, length)


def trie_find(trie, string, index, length):
    if string[index] == '?':
        return trie['total'].get(length, 0)
    if trie.get(string[index]):
        return trie_find(trie[string[index]], string, index+1, length)
    else:
        return 0


def solution(words, queries):
    answer = []
    trie = {'total': {}}
    reverse_trie = {'total': {}}
    for word in words:
        length = len(word)
        trie_input(trie, word, -length, length)
        trie_input(reverse_trie, word[::-1], -length, length)
    for query in queries:
        length = len(query)
        if query[0] == '?':
            answer.append(trie_find(reverse_trie, query[::-1], 0, length))
        else:
            answer.append(trie_find(trie, query, 0, length))
    return answer


a = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
b = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(a, b))
