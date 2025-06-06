from collections import deque


def attack(coordinate_x, coordinate_y, max_x, max_y, nations, geomap):
    queue = deque([(coordinate_x, coordinate_y)])
    geomap[coordinate_x][coordinate_y] = 0
    while queue:
        nations -= 1
        u, v = queue.popleft()
        for du, dv in neighbors:
            new_u, new_v = u + du, v + dv
            if 0 <= new_u < max_x and 0 <= new_v < max_y and geomap[new_u][new_v]:
                queue.append((new_u, new_v))
                geomap[new_u][new_v] = 0
    return nations


neighbors = ((-1, 0), (0, 1), (1, 0), (0, -1))
n, m, q = map(int, input().strip().split())
countries = 0
cells = []
for _ in range(n):
    places = list(map(int, input().strip().split()))
    countries += places.count(1)
    cells.append(places)
for _ in range(q):
    x, y = map(int, input().strip().split())
    x -= 1
    y -= 1
    if cells[x][y]:
        countries = attack(x, y, n, m, countries, cells)
    print(countries)
