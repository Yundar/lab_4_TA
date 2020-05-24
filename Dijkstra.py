def read_from_file(path):
    with open(path, 'rt') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].replace('\n', '')
            lines[i] = list(map(int, lines[i].split('\t')))
    return lines


def Dijkstra(graph, start):
    inf = 10 ** 9
    seen = [False] * len(graph)
    distances = [inf] * len(graph)
    distances[start] = 0
    dist = 0
    current = start
    ways = dict()
    while dist < inf:
        c = current
        seen[c] = True
        for i in range(len(graph)):
            if distances[c] + graph[c][i] < distances[i]:
                distances[i] = distances[c] + graph[c][i]
                ways[i] = c
        dist = inf
        for i in range(len(graph)):
            if not seen[i] and distances[i] < dist:
                dist = distances[i]
                current = i
    return distances, ways


def way(dictionary, start, goal):
    fl = 0
    current = goal
    way = [current]
    while fl != 1:
        current = dictionary[current]
        if current == start:
            fl = 1
        way.append(current)
    way.reverse()
    return way

cities = ['Белград', 'Нови-Сад', 'Приштина', 'Ниш', 'Крагуевац', 'Суботица', 'Лесковац', 'Зренянин', 'Панчево',
          'Чачак', 'Кралево', 'Смедерево', 'Валево', 'Крушевац', 'Шабац']
start = int(input('Оберіть номер початкового міста: ')) - 1
goal = int(input('Оберіть номер кінцевого міста: ')) - 1
D = Dijkstra(read_from_file('roads.txt'), start)
print(cities[start] + ' - ' + cities[goal] + '  ' + 'Відстань: ' + str(D[0][goal]))
way_to_city = way(D[1], start, goal)
for i in range(len(way_to_city)):
    way_to_city[i] = cities[way_to_city[i]]
way_to_city = ' -> '.join(way_to_city)
print('Маршрут: ' + way_to_city)
