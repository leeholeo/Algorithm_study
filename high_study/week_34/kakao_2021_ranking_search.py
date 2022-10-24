'''
partial caching
binary search
'''
# item_to_index = {
#     '-': 0,
#     'cpp': 1, 'java': 2, 'python': 3,
#     'backend': 1, 'frontend': 2,
#     'junior': 1, 'senior': 2,
#     'chicken': 1, 'pizza': 2
# }
class DB:
    def __init__(self):
        self.data = {}
        self.db_initialize()

    def db_initialize(self):
        for lang in ('cpp', 'java', 'python', '-'):
            self.data[lang] = {}
            for job in ('backend', 'frontend', '-'):
                self.data[lang][job] = {}
                for career in ('junior', 'senior', '-'):
                    self.data[lang][job][career] = {}
                    for soul_food in ('chicken', 'pizza', '-'):
                        self.data[lang][job][career][soul_food] = []

    def insert(self, lang, job, career, soul_food, score):
        for l in (lang, '-'):
            for j in (job, '-'):
                for c in (career, '-'):
                    for s in (soul_food, '-'):
                        self.data[l][j][c][s].append(score)

    def sort(self):
        for lang in ('cpp', 'java', 'python', '-'):
            for job in ('backend', 'frontend', '-'):
                for career in ('junior', 'senior', '-'):
                    for soul_food in ('chicken', 'pizza', '-'):
                        self.data[lang][job][career][soul_food].sort()

    def binary_search(self, lang, job, career, soul_food, score):
        data = self.data[lang][job][career][soul_food]
        length = len(data)
        left, right = 0, length-1
        while left <= right:
            center = (left+right) // 2
            if data[center] < score:
                left = center + 1
            else:
                right = center - 1
        return length - left


def info_parsing(info: str) -> [str]*4 + [int]:
    splited_info = info.split()
    splited_info[-1] = int(splited_info[-1])
    return splited_info


def info_inserting(db, informations):
    for info in informations:
        db.insert(*info_parsing(info))
    db.sort()


def query_parsing(query: str) -> [str]*4 + [int]:
    splited_query = query.split()
    return splited_query[0], splited_query[2], splited_query[4], splited_query[6], int(splited_query[7])


def solution(info, query):
    db = DB()
    info_inserting(db, info)
    answer = []
    for q in query:
        answer.append(db.binary_search(*query_parsing(q)))
    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
solution(info, query)
