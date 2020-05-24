def read_from_file(path):
    with open(path, 'rt') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].replace('\n', '')
            lines[i] = list(map(int, lines[i].split('\t')))
    return lines


def Dijkstra(graph, start, goal):
    inf = 10 ** 9
    seen = [False] * len(graph)
    distances = [inf] * len(graph)
    distances[start] = 0
    dist = 0
    current = start
    ways = [[]] * len(graph)
    while dist < inf:
        ways.append([])
        c = current
        seen[c] = True
        for i in range(len(graph)):
            if distances[c] + graph[c][i] < distances[i]:
                distances[i] = distances[c] + graph[c][i]
        dist = inf
        for i in range(len(graph)):
            if not seen[i] and distances[i] < dist:
                dist = distances[i]
                current = i
    return distances

Dijkstra(read_from_file('roads.txt'), 4, 2)



# cities = ['Белград', 'Нови-Сад', 'Приштина', 'Ниш', 'Крагуевац', 'Суботица', 'Лесковац', 'Зренянин', 'Панчево',
#           'Чачак', 'Кралево', 'Смедерево', 'Валево', 'Крушевац', 'Шабац']
# start = int(input('Оберіть номер початкового міста: ')) - 1
# goal = int(input('Оберіть номер кінцевого міста: ')) - 1