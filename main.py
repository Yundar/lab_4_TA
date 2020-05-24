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


def read_from_file(path):
    with open(path, 'rt') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].replace('\n', '')
            lines[i] = list(map(int, lines[i].split('\t')))
    return lines


def heuristic(a, b):
    g = read_from_file('straight.txt')
    n = g[a][b]
    return n


def a_star_search(graph, start, goal):
    queue = PriorityQueue()
    queue.add(start, 0)
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    while not queue.is_empty():
        current = queue.get()

        if current == goal:
            break

        for next in range(len(graph)):

            if next != current:
                new_cost = cost_so_far[current] + graph[current][next]
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + heuristic(current, next)
                    queue.add(next, priority)
                    came_from[next] = current
    fl = 0
    current = goal
    way = [current]
    while fl != 1:
        current = came_from[current]
        if current == start:
            fl = 1
        way.append(current)
    way.reverse()
    cost = cost_so_far[goal]
    return way, cost


cities = ['Белград', 'Нови-Сад', 'Приштина', 'Ниш', 'Крагуевац', 'Суботица', 'Лесковац', 'Зренянин', 'Панчево',
          'Чачак', 'Кралево', 'Смедерево', 'Валево', 'Крушевац', 'Шабац']
start = int(input('Оберіть номер початкового міста: ')) - 1
goal = int(input('Оберіть номер кінцевого міста: ')) - 1
a_search = a_star_search(read_from_file('roads.txt'), start, goal)
print(cities[start] + ' - ' + cities[goal] + '  ' + 'Відстань: ' + str(a_search[1]))
