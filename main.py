class PriorityQueue:
    def __init__(self):
        self.elements = list()

    def add(self, top, priority):
        self.elements.append((top, priority))

    def get(self):
        priority = []
        for i in range(len(self.elements)):
            priority.append(self.elements[i][1])
        index = priority.index(min(priority))
        return self.elements.pop(index)[0]

    def show(self):
        print(self.elements)

    def is_empty(self):
        return len(self.elements) == 0


def read_from_file(adress):
    inp = open(adress)
    f = inp.readlines()
    for i in range(len(f)):
        f[i] = f[i].replace('\n', '')
        f[i] = list(map(int, f[i].split('\t')))
    return f
