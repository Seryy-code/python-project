class Tile:
    """Pojedyncze pole na mapie"""
    def __init__(self, x, y, terrain_type="grass"):
        # TODO: Zaimplementuj konstruktor
        # terrain_type: "grass", "city", "forest", "water", "ruins"
        pass

    def is_passable(self):
        # TODO: Zwróć czy można przejść przez pole
        # water = False, reszta = True
        pass

class GameMap:
    """Mapa gry jako siatka"""
    def __init__(self, width=20, height=20):
        # TODO: Stwórz siatkę Tile'ów
        pass

    def generate_terrain(self):
        # TODO: Wygeneruj losowy teren
        # 50% grass, 20% forest, 15% city, 10% ruins, 5% water
        pass

    def get_tile(self, x, y):
        # TODO: Zwróć tile na pozycji x,y
        pass

    def get_neighbors(self, x, y):
        # TODO: Zwróć listę sąsiednich pól (8 kierunków)
        pass

    def find_path(self, start_x, start_y, end_x, end_y):
        # TODO: Prosty pathfinding - zwróć True jeśli istnieje ścieżka
        # Użyj BFS lub prostszego algorytmu
        pass

    def visualize(self):
        # TODO: Wyświetl mapę jako siatkę znaków
        # g=grass, C=city, f=forest, w=water, R=ruins
        pass

# Testy do wykonania:
# 1. Stwórz mapę 10x10
# 2. Wygeneruj losowy teren
# 3. Wyświetl mapę
# 4. Znajdź ścieżkę między dwoma punktami