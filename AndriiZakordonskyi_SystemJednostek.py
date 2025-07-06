# Szablon startowy dla zadania
class Entity:
    """Bazowa klasa dla wszystkich jednostek w grze"""
    def __init__(self, x, y, hp):
        # TODO: Zaimplementuj konstruktor
        pass

    def move(self, new_x, new_y):
        # TODO: Zmień pozycję jednostki
        pass

    def take_damage(self, damage):
        # TODO: Obsłuż otrzymywanie obrażeń
        pass

class Human(Entity):
    """Klasa reprezentująca człowieka"""
    def __init__(self, x, y, role="survivor"):
        # TODO: Zainicjuj człowieka z HP=100, morale=85
        # role może być: "warrior", "scavenger", "medic", "builder", "leader"
        pass

    def consume_resources(self, food, water):
        # TODO: Konsumuj zasoby, zmniejsz morale jeśli brak
        pass

class Zombie(Entity):
    """Klasa reprezentująca zombie"""
    def __init__(self, x, y, zombie_type="normal"):
        # TODO: Zainicjuj zombie z HP=50
        # zombie_type może być: "normal", "walker", "runner", "howler"
        pass

    def can_infect(self):
        # TODO: Zwróć True jeśli zombie może zarazić (np. jest żywe)
        pass

# Testy do wykonania:
# 1. Stwórz 3 ludzi o różnych rolach
# 2. Stwórz 2 zombie różnych typów
# 3. Przetestuj ruch jednostek
# 4. Przetestuj system obrażeń