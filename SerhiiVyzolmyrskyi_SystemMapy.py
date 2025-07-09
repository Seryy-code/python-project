import random

class Tile:
    """Pojedyncze pole na mapie"""
    def __init__(self, x, y, terrain_type="grass"):
        self.x = x
        self.y = y
        self.terrain_type = terrain_type
        pass

    def is_passable(self):
        return self.terrain_type != "water"

class GameMap:
    """Mapa gry jako siatka"""
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.grid = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append(Tile(x, y, "grass"))
            self.grid.append(row)

    def generate_terrain(self):
        # TODO: Wygeneruj losowy teren
        # 50% grass, 20% forest, 15% city, 10% ruins, 5% water
        for row in self.grid:
            for tile in row:
                r = random.randint(0, 99)
                if r < 50:
                    tile.terrain_type = "grass"
                elif r < 70:
                    tile.terrain_type = "forest"
                elif r < 85:
                    tile.terrain_type = "city"
                elif r < 95:
                    tile.terrain_type = "ruins"
                else:
                    tile.terrain_type = "water"
        pass

    def get_tile(self, x, y):
        # TODO: Zwróć tile na pozycji x,y
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return None

    def get_neighbors(self, x, y):
        # TODO: Zwróć listę sąsiednich pól (8 kierunków)
        neighbors = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    neighbors.append(self.grid[ny][nx])
        return neighbors

    def find_path(self, start_x, start_y, end_x, end_y):
        # TODO: Prosty pathfinding - zwróć True jeśli istnieje ścieżka
        # Użyj BFS lub prostszego algorytmu
        from collections import deque
        visited = set()
        queue = deque()
        queue.append((start_x, start_y))
        while queue:
            x, y = queue.popleft()
            if (x, y) == (end_x, end_y):
                return True
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for neighbor in self.get_neighbors(x, y):
                if neighbor.is_passable() and (neighbor.x, neighbor.y) not in visited:
                    queue.append((neighbor.x, neighbor.y))
        return False

    def visualize(self):
        # TODO: Wyświetl mapę jako siatkę znaków
        # g=grass, C=city, f=forest, w=water, R=ruins
        symbol = {
            "grass": "g",
            "city": "c",
            "forest": "f",
            "water": "w",
            "ruins": "r"
        }
        for row in self.grid:
            print(" ".join(symbol[tile.terrain_type] for tile in row))

# Testy do wykonania:
# 1. Stwórz mapę 10x10
# 2. Wygeneruj losowy teren
# 3. Wyświetl mapę
# 4. Znajdź ścieżkę między dwoma punktami